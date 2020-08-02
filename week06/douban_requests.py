"""
此处请求豆瓣《触不可及》短评，并将短评内容存储到mysql。以供web展示用
"""

from multiprocessing.dummy import Pool as ThreadPool
import os
from fake_useragent import UserAgent
import requests
from scrapy.selector import Selector
import pymysql
from snownlp import SnowNLP
import math

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://movie.douban.com/subject/6786002/',
    'Cookie': 'll="108288"; bid=qSXzRL0hvrg; __utmz=30149280.1594550604.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); douban-fav-remind=1; __gads=ID=388d77592b291a1f:T=1594550605:S=ALNI_MY5D4SnSbEuxuutvbzLbQsvVbqxQQ; ap_v=0,6.0; __yadk_uid=vfNvGpUA3Nb3IfL5vuIgl5fVdRBtG5oH; __utmc=30149280; __utmc=223695111; __utmz=223695111.1596093958.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=D2837B3451C2507BF1BF3B677214D582F|48cada44f4a15da7f2b2e36154349e77; _pk_id.100001.4cf6=b7bd7fe2eec5720d.1596093955.2.1596098148.1596095660.; _pk_ses.100001.4cf6=*; __utma=30149280.1120724558.1594550604.1596093958.1596098148.4; __utmb=30149280.0.10.1596098148; __utma=223695111.412969446.1596093958.1596093958.1596098148.2; __utmb=223695111.0.10.1596098148'
}


def getcomment(url):
    """
    爬取豆瓣电影短评
    存入数据库
    :param url:  短评地址
    :return: None
    """
    try:
        response = requests.get(url=url, headers=headers)
        contents = Selector(response=response).xpath('//*[@id="comments"]/div[@class="comment-item"]')

        for content in contents:
            # avatar = content.xpath('./div[2]/h3/span[2]/a/text()').extract_first()
            c_stars = content.xpath('./div[2]/h3/span[2]/span[2][contains(@class,"rating")]').extract_first()
            stars = 0
            if c_stars is not None:
                stars = content.xpath('./div[2]/h3/span[2]/span[2][contains(@class,"rating")]/@class').extract_first()[
                        7:10]
            stars = math.floor(int(stars) / 10)
            comment = content.xpath('./div[2]/p/span/text()').extract_first().strip()
            sentiment = SnowNLP(comment).sentiments
            # print(f'星级：{stars},评论内容：{comment},sentiment:{sentiment}')
            insert(stars, comment, sentiment)

    except Exception as ex:
        print(ex)


def insert(stars, comment, sentiment):
    """
    插入数据库
    :param stars: 星级
    :param comment:评论内容
    :param sentiment: 情感倾向
    :return:
    """
    try:
        connent = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='guoliang123',
            db='filmdb',
            charset='utf8')

        cur = connent.cursor()
        sql = 'insert into comments (stars,comment,sentiment) values({},"{}",{})'.format(stars, comment, sentiment)
        cur.execute(sql)
        connent.commit()
        print(sql)

    except Exception as ex:
        print(f'insert ERROR:{ex}')

    finally:
        cur.close()
        connent.close()


if __name__ == '__main__':
    urls = []
    for p in range(10):
        url = f'https://movie.douban.com/subject/6786002/comments?start={p * 20}&limit=20&sort=new_score&status=P'
        urls.append(url)

    pool = ThreadPool(os.cpu_count())
    pool.map(getcomment, urls)

    pool.close()
    pool.join()
