# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from redis import Redis


class HuyaproPipeline:
    fp = None

    def open_spider(self, spider):
        print('i am open_spider()')
        self.fp = open('./huyazhibo.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):  # item就是接收到爬虫类提交过来的item对象
        self.fp.write(item['title'] + ':' + item['author'] + ':' + item['hot'])
        print(item['title'], '写入成功!!!')
        return item

    def close_spider(self, spider):
        print('i am close_spider()')
        self.fp.close()


# 将数据写入数据库
class mysqlPipeLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Spider', charset='utf8')
        print(self.conn)

    def process_item(self, item, spider):
        sql = 'insert into huya values("%s","%s","%s")' % (item['title'], item['author'], item['hot'])
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item  # 写上return item表明下个类可以拿到item数据

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class RedisPipeLine(object):
    conn = None

    def open_spider(self, spider):
        self.conn = Redis(host='127.0.0.1', port=6379)

    def process_item(self, item, spider):  # item表示一个字典
        self.conn.lpush('huyaList', item)
        return item
