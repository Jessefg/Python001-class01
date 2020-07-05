# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmtopspiderItem(scrapy.Item):
    name = scrapy.Field()
    cate = scrapy.Field()
    showtime = scrapy.Field()
