# -*- coding: utf-8 -*-

"""
    1. 安装并使用 requests、bs4 库
    2. 爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
    3. 并以 UTF-8 字符集保存到 csv 格式的文件中。
"""

"""
1. 安装 requests ：  pip install requests
2.安装bs4库：pip install BeautifulSoup4

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


class RequestSpider(object):

    def spider_maoyan_films(self):
        headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Cookie': 'uuid_n_v=v1; uuid=D69DF2D0B7C411EA85DD839D6F814C7AD49C8FE718C04881A2DC116B6933A43F; _csrf=a8cd7e3c6ac7d377458ae2a9cb742ee4140a27585cb680c11a996a06360755a8; _lxsdk_cuid=172f15337eac8-043408b6ca7052-31617402-1fa400-172f15337eac8; _lxsdk=D69DF2D0B7C411EA85DD839D6F814C7AD49C8FE718C04881A2DC116B6933A43F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593186662; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593186662; mojo-uuid=4423726c10a373925a822026b609f786; __mta=156130180.1593186662828.1593186662828.1593186662828.1; mojo-session-id={"id":"b337b1dbbf697a693ded16f1938256c8","time":1593186662842}; mojo-trace-id=1; _lxsdk_s=172f15335f0-85-e-acf%7C%7C3'
        }
        url = 'https://maoyan.com/films?showType=3'
        """ 请求url """
        req = requests.get(url=url, headers=headers)
        print(f'请求url:{url}，请求返回状态码：{req.status_code}')

        """ 使用bs4封装 """
        soup = BeautifulSoup(req.text, 'html.parser')
        contents = soup.find_all('div', attrs={'class': 'movie-hover-info'})

        listItem = []
        for content in contents[:10]:
            name = content.find_all('div', attrs={'class': 'movie-hover-title'})[0].find('span').text.strip()
            tag = content.find_all('div', attrs={'class': 'movie-hover-title'})[1].find_all(text=True)[2].strip()
            showtime = content.find_all('div', attrs={'class': 'movie-hover-brief'})[0].find_all(text=True)[2].strip()

            listItem.append([name, tag, showtime])

        """ 生成csv文件 """
        movieData = pd.DataFrame(data=listItem)
        movieData.to_csv('./maoyantop.csv', mode='a', encoding='utf-8', index=False, header=False)


if __name__ == '__main__':
    req = RequestSpider()
    req.spider_maoyan_films()
