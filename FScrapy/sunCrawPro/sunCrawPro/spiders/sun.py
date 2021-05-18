import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunCrawPro.items import SuncrawproItem, Detail_item


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 实例化了一个连接提取器对象
    # 作用：根据指定规则（allow='正则表达式'）进行指定连接的提取
    link = LinkExtractor(allow=r'type=4&page=\d+')  # 获取页码链接
    # 获取新闻详情页的链接
    link_detail = LinkExtractor(allow=r"question/\d+/\d+.shtml")
    rules = (
        # 将link作用到了Rule的构造方法的参数中
        # 作用：将连接提取器提取到的连接进行请求发送且根据指定规则对请求到的数据进行数据解析
        Rule(link, callback='parse_item', follow=False),
        # follow=True:将连接提取器继续作用到连接提取器提取到的 连接 对应的 页面中
        Rule(link_detail, callback='parse_detail'),
    )

    def parse_item(self, response):
        # xpath表达式中是不可以出现tbody标签
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/text()').extract_first()
            num = tr.xpath('./td[1]/text()').extract_first()
            item = SuncrawproItem()
            item['title'] = title
            item['num'] = num

            yield item

    def parse_detail(self, response):
        content = response.xpath('/html/body/div[9]/table[2]//tr[1]/td/text()').extract_first()
        num = response.xpath('/html/body/div[9]/table[1]//tr/td[2]/span[2]/text()').extract_first()
        item = Detail_item()
        item['content'] = content
        item['num'] = num

        yield item