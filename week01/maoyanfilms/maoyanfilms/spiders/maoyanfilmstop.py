# -*- coding: utf-8 -*-
"""
 1. 使用 Scrapy 框架和 XPath
 2. 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间
 3. 并以 UTF-8 字符集保存到 csv 格式的文件中。

    猫眼电影网址： https://maoyan.com/films?showType=3

    要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
 """

import scrapy
from scrapy.selector import Selector
from ..items import MaoyanfilmsItem


class MaoyanfilmstopSpider(scrapy.Spider):
    name = 'maoyanfilmstop'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        listItem = []
        contents = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for content in contents[:10]:
            item = MaoyanfilmsItem()
            item['name'] = content.xpath('./div[1]/span/text()').extract_first()
            item['cate'] = content.xpath('./div[2]/text()[2]').extract_first().strip()
            item['showtime'] = content.xpath('./div[4]/text()[2]').extract_first().strip()
            listItem.append(item)
        return listItem
