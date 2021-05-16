import scrapy
from selenium import webdriver
from wangyipeo.items import WangyipeoItem


# 爬取网易新闻
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com']
    model_urls = []
    bro = webdriver.Chrome(executable_path='chromedriver.exe')

    def parse(self, response):
        # 解析5个板块的对应的url
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        model_index = [3, 4, 6, 7, 8]
        for index in model_index:
            # li依次表示的是5个板块对应的li标签
            li = li_list[index]
            # 5个板块对应的url
            model_url = li.xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
            # 对每一个版块的url进行手动请求的发送
            yield scrapy.Request(model_url, callback=self.parse_model)

    def parse_model(self, response):
        """
        用作于解析每一个版块对应页面数据中的新闻标题和新闻详情页的url
        :param response:
        :return:
        """
        # 该方法中获取的response对象是没有包含动态加载出的新闻数据（是一个不满足需要的response）
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')  # 1+5+n
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            detail_url = div.xpath('./a/@href').extract_first()
            item = WangyipeoItem()
            item['title'] = title
            yield scrapy.Request(detail_url, callback=self.parse_new_detail, meta={'item': item})

    def parse_new_detail(self, response):
        """
        解析新闻内容
        :param response:
        :return:
        """
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]/text()').extract()
        content = ''.join(content)
        item['content'] = content

        yield item

    # 该方法只会在整个程序结束时执行一次
    def close(self, spider):
        self.bro.quit()
