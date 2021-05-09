import scrapy
from firstBlood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称: 爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名:
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表: 列表中的列表元素会被scrapy自动的进行请求发送
    start_urls = ['https://dig.chouti.com/']

    # # 解析数据
    # # 基于终端指令的持久化存储
    # def parse(self, response):
    #     data_list = []
    #     div_list = response.xpath('/html/body/main/div/div/div[1]/div/div[2]/div[1]')
    #     for div in div_list:
    #         # 注意: xpath返回的列表中的列表元素是Selector对象,我们要解析获取的字符串数据存储在该对象中
    #         # 必须经过一个extract()的操作才可以将该对象中存储的客串的数据获取
    #         # content = div.xpath('./div/div/div[1]/a/text()')[0].extract()
    #         content = div.xpath('./div/div/div[1]/a/text()').extract_first()
    #         # xpath返回的列表中的列表元素有多个(Selector对象),想要将每一个列表元素对应的Selector中的字符串
    #         # 提取出来该如何操作? response.xpath('/div//text()').extract()
    #         print(content)  # <Selector xxx='dsdsd' dada="字符串">
    #         data_list.append(content)
    #     return data_list

    # 解析数据
    # 基于管道的持久化存储
    def parse(self, response):
        div_list = response.xpath('/html/body/main/div/div/div[1]/div/div[2]/div[1]')
        for div in div_list:
            # 注意: xpath返回的列表中的列表元素是Selector对象,我们要解析获取的字符串数据存储在该对象中
            # 必须经过一个extract()的操作才可以将该对象中存储的客串的数据获取
            # content = div.xpath('./div/div/div[1]/a/text()')[0].extract()
            content = div.xpath('./div/div/div[1]/a/text()').extract_first()
            item = FirstbloodItem()
            item['content'] = content
            # xpath返回的列表中的列表元素有多个(Selector对象),想要将每一个列表元素对应的Selector中的字符串
            # 提取出来该如何操作? response.xpath('/div//text()').extract()
            print(content)  # <Selector xxx='dsdsd' dada="字符串">

            yield item  # 将item对象提交给管道
