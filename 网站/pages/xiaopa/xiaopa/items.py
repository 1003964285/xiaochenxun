# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaopaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    serial_number = scrapy.Field()
    #电影的名称
    movie_name = scrapy.Field()
    #电影的介绍
    introduce = scrapy.Field()
    #星级
    star = scrapy.Field()
    #电影的评论
    evaluate = scrapy.Field()
    #电影的描述
    describe = scrapy.Field()
