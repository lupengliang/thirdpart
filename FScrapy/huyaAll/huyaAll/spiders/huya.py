import scrapy

from huyaAll.items import HuyaallItem


class HuyaSpider(scrapy.Spider):
    name = 'huya'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.huya.com/g/xingxiu']
    # 通用的url模板
    url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&page=%d'

    # 基于管道的持久化存储
    def parse(self, response):
        li_list = response.xpath('//*[@id="js-live-list"]/li')
        for li in li_list:
            title = li.xpath('./a[2]/text()').extract_first()
            author = li.xpath('./span/span[1]/i/text()').extract_first()
            hot = li.xpath('./span/span[2]/i[2]/text()').extract_first()

            # 实例化item类型的对象
            item = HuyaallItem()
            item['title'] = title
            item['author'] = author
            item['hot'] = hot

            yield item  # 提交给管道
        # 手动请求的发送
        for page in range(2, 5):
            new_url = format(self.url % page)
            # 发起的get请求
            yield scrapy.Request(url=new_url, callback=self.parse_other)

    # 所有的解析方法都必须模拟parse进行定义:必须要有和parse同样的参数
    def parse_other(self, response):
        print(response.json())
