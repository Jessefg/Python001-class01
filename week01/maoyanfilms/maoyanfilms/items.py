# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanfilmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    cate = scrapy.Field()
    showtime = scrapy.Field()
