# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HuyaproPipeline:
    fp = None

    def open_spider(self, spider):
        print('i am open_spider()')
        self.fp = open('./huyazhibo.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):  # item就是接收到爬虫类提交过来的item对象
        self.fp.write(item['title'] + ':' + item['author'] + ':' + item['hot'])
        print(item['title'], '写入成功!!!')
        return item

    def close_spider(self, spider):
        print('i am close_spider()')
        self.fp.close()