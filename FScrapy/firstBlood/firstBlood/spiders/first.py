import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称: 爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名:
    allowed_domains = ['www.xxx.com']
    # 起始的url列表: 列表中的列表元素会被scrapy自动的进行请求发送
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com']

    # 解析数据
    def parse(self, response):
        pass
39.04