# -*- coding=utf-8 -*-
# Auth:gonghongyuan
# Time:2020/6/27 23:50
# File:maoyan_request.py
# IDE:PyCharm
# 安装并使用 requests、bs4 库，
# 爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
# 并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd


def get_film_info(url):
    # 设置头部信息
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
    cookie = 'uuid_n_v=v1; uuid=9F53B300B8DC11EA974289B279A7041D040C4C6CDF4A4A61B93345EAC6C37EF8; ' \
             '_csrf=d1c035716a86cf40dabf1fa663c3bfaea112821551378e7f58421c4a32e3b504; ' \
             'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593306830; ' \
             'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593306830; mojo-uuid=f6e5312dedc4a243b7eda91c56dbddee; ' \
             'mojo-trace-id=1; mojo-session-id={"id":"bf459469135ee9bbdeb997f92d08fa0a","time":1593306830501}; ' \
             '_lxsdk_cuid=172f87cdc16c8-03f6cebb1e3777-4c302a7b-144000-172f87cdc16c8; ' \
             '_lxsdk_s=172f87cdc16-f17-485-b6b%7C%7C2; ' \
             '_lxsdk=9F53B300B8DC11EA974289B279A7041D040C4C6CDF4A4A61B93345EAC6C37EF8; ' \
             '__mta=222204199.1593306831928.1593306831928.1593306831928.1 '
    header = {'user-agent': user_agent, 'cookie': cookie}
    response = requests.get(url, headers=header)
    info = bs(response.text, 'html.parser')

    # 创建影片列表
    flim_info = []

    # for循环查找元素
    for tags in info.find_all('div', attrs={'class': 'movie-hover-info'}):
        for tag in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
            for i in tag.find_all('span', attrs={'class': 'hover-tag'}):
                if i.text == '类型:':
                    movie_category = (i.find_parent('div').text.strip())  # 获取节点的父节点的内容
                if i.text == '上映时间:':
                    movie_date = (i.find_parent('div').text.strip())
                    movie_title = i.find_parent('div').get('title')  # 获取父节点的 属性内容
                    movie_info = [movie_title, movie_category, movie_date]
                    flim_info.append(movie_info)

    sleep(5)

    # 通过 pandas 转csv，只存10个电影即可
    df = pd.DataFrame(flim_info[:10], columns=['movie-title', 'movie-category', 'movie-date'])
    df.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)


get_film_info('https://maoyan.com/films?showType=3')
