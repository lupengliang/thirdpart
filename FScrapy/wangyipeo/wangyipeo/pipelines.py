# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class WangyipeoPipeline:
    conn = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='Spider',
            charset='utf8'
        )
        print(self.conn)

    def process_item(self, item, spider):
        print(item)
        sql = 'insert into wangyi values ("%s","%s")' % (item['title'], item['content'])
        self.curse = self.conn.cursor()
        try:
            self.curse.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.curse.close()
        self.conn.close()
