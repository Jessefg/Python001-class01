# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.utils.project import get_project_settings  # 导入settings
import pandas as  pd


class FilmtopspiderPipeline:
    def __init__(self):
        """ 获取sql配置 """
        settings = get_project_settings()

        try:
            self.connect = pymysql.connect(
                host=settings['MYSQL_HOST'],
                port=settings['MYSQL_PORT'],
                user=settings['MYSQL_USER'],
                password=settings['MYSQL_PASSWORD'],
                db=settings['MYSQL_DB'],
                charset=settings['MYSQL_CHARTSET']
            )
            """
                开启游标
            """
            self.cursor = self.connect.cursor()

            # 测试连接
            # self.cursor.execute(' select count(*) from bangs; ')
            # print(f'------- count : {self.cursor.fetchone()}')

            ## 创建爬虫表
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS maoyantop ( id int auto_increment primary key not null, name varchar(100), catename varchar(50), showtime datetime ) ;')

            # self.close_spider()  # 若此处关闭连接，则以后的数据不能提交了

        except Exception as ex:
            self.close_spider()
            print(ex)

    def process_item(self, item, spider):
        name = item['name']
        cate = item['cate']
        showtime = item['showtime']

        self.cursor.execute(
            f' INSERT maoyantop (name, catename, showtime) VALUES ( "{name}","{cate}","{showtime}" )')
        self.connect.commit()
        # self.close_spider()

        return item

    def close_spider(self):
        """
            关闭游标
            关闭连接
        """
        self.cursor.close()
        self.connect.close()


class CSVPipeline:
    def process_item(self, item, spider):
        name = item['name']
        cate = item['cate']
        showtime = item['showtime']
        txt = f'{name},{cate},{showtime}'
        moviepd = pd.DataFrame(data=[txt])
        # moviepd = pd.DataFrame(data=[name, cate, showtime])
        moviepd.to_csv('./maoyanmovietop10_item.csv', encoding='utf8', mode='a', index=False, header=False)
        return item
