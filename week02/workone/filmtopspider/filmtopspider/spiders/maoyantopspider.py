# -*- coding: utf-8 -*-
import scrapy
from ..items import FilmtopspiderItem
from scrapy.selector import Selector

"""
1. 为 Scrapy 增加代理 IP 功能。
2. 将保存至 csv 文件的功能修改为保持到 MySQL，
3. 并在下载部分增加异常捕获和处理机制。
备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。

"""


class MaoyantopspiderSpider(scrapy.Spider):
    name = 'maoyantopspider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        items = []
        contents = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for content in contents[:10]:
            item = FilmtopspiderItem()
            item['name'] = content.xpath('./div[@class="movie-hover-title"]/span/text()').extract_first().strip()
            item['cate'] = content.xpath('./div[@class="movie-hover-title"][2]/text()').extract()[1].strip()
            item['showtime'] = content.xpath('./div[contains(@class,"movie-hover-brief")]/text()').extract()[1].strip()
            items.append(item)
            print('-----item - name :', item['name'])
        return items
