import scrapy

from huyaPro.items import HuyaproItem


class HuyaSpider(scrapy.Spider):
    name = 'huya'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.huya.com/g/xingxiu']

    # # 基于终端指令的持久化存储
    # def parse(self, response):
    #     li_list = response.xpath('//*[@id="js-live-list"]/li')
    #     all_data = []
    #     for li in li_list:
    #         title = li.xpath('./a[2]/text()').extract_first()
    #         author = li.xpath('./span/span[1]/i/text()').extract_first()
    #         hot = li.xpath('./span/span[2]/i[2]/text()').extract_first()
    #         dic = {
    #             'title': title,
    #             'author': author,
    #             'hot': hot
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 基于管道的持久化存储
    def parse(self, response):
        li_list = response.xpath('//*[@id="js-live-list"]/li')
        for li in li_list:
            title = li.xpath('./a[2]/text()').extract_first()
            author = li.xpath('./span/span[1]/i/text()').extract_first()
            hot = li.xpath('./span/span[2]/i[2]/text()').extract_first()

            # 实例化item类型的对象
            item = HuyaproItem()
            item['title'] = title
            item['author'] = author
            item['hot'] = hot

            yield item  # 提交给管道