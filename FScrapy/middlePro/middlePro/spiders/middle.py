import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http123://www.baidu.com/s?wd=ip1234']

    def parse(self, response):
        page_text = response.text
        with open('ip.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)
