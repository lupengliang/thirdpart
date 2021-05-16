import scrapy
from moviePro.items import MovieproItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/class/%E5%96%9C%E5%89%A7/id/1.html']
    url = 'https://www.4567tv.tv/index.php/vod/show/class/喜剧/id/%d.html'
    page = 1

    # 解析电影
    def parse(self, response):
        print('正在爬取第{}页的电影数据......'.format(self.page))
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            item = MovieproItem()
            name = li.xpath('./div/a/@title').extract_first()
            item['name'] = name
            detail_url = 'https://www.4567tv.tv' + li.xpath('./div/a/@href').extract_first()
            # 可以对详情页的url进行手动请求的发送
            # 请求传参： 让Request将一个数据值（字典）传递给回调函数
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
        if self.page < 6:
            self.page += 1
            new_url = format(self.url % self.page)
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_detail(self, response):
        # 接收请求传参的数据（字典）
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[3]/a/text()').extract_first()
        item['desc'] = desc

        yield item
