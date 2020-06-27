# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd


class MaoyanfilmsPipeline:
    def process_item(self, item, spider):
        film = pd.Series({
            'name': item['name'],
            'cate': item['cate'],
            'showtime': item['showtime']
        })
        df_films = pd.DataFrame(data=[film])
        df_films.to_csv('./maoyanfilmstop.csv', mode='a', encoding='utf-8', index=False, header=False)
        return item
