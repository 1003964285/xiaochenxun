# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    #爬虫的名称
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']  #允许爬虫爬取域名范围
    start_urls = ['http://movie.douban.com/top250']   #入口URL

    #
    def parse(self, response):
        print(response.text)
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i in movie_list:
            doubanItem = DoubanItem()
            doubanItem['serial_number'] = i.xpath(".//div[@class='pic']//em//text()").extract_first()
            doubanItem['movie_name'] = i.xpath(".//div[@class='info']//div[@class='hd']/a//span[1]/text()").extract_first()
            content = i.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for item in content:
                s = ''.join(item.split())
                doubanItem['introduce'] = s
            doubanItem['star'] = i.xpath(".//span[@class='rating_num']/text()").extract_first()
            doubanItem['evaluate'] = i.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            doubanItem['describe'] = i.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield doubanItem
        nexturls = response.xpath("//span[@class='next']//a/@href").extract()

        if nexturls:
            nexturl = 'https://movie.douban.com/top250'+ nexturls[0]
            print(nexturl)
            yield scrapy.Request(nexturl,callback=self.parse)
















































