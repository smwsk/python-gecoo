# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IcomicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 漫画名称
    comicName = scrapy.Field()
    # 漫画主页
    comicHomeImage = scrapy.Field()
    # 漫画主页url
    comicHomeUrl = scrapy.Field()
    pass
