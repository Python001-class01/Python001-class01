import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd
import re

ua = UserAgent()
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592845237; _lxsdk_cuid=172dcf97ca5c8-0fd5444e050b77-143f6257-13c680-172dcf97ca5c8; _lxsdk=E386DAC0B4A911EAACB6BBD781D89938787DFDB6AB144B8BB7BCDA252EE20E80; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592968645; __mta=175526813.1592845237500.1592968635455.1592968646052.7; _lxsdk_s=172e44f7d6d-805-f2d-7ad%7C%7C9',
    'Host': 'maoyan.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':ua.random
}

def crawl_film(count):
    url = 'https://maoyan.com/films?showType=3'

    response = requests.get(url, headers=header)

    bs_info = bs(response.text, 'html.parser')
    movie_list = []
    film_count = 0
    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
        for atag in tags.find_all('a',):
            # print(atag.find('herf'))

            movie_link = 'https://maoyan.com' + atag.get('href')
            movie_list.append(atag.get_text())
            movie_class, plan_date = get_film_info(movie_link)
            movie_list.append(movie_class)
            movie_list.append(plan_date)
            
        film_count += 1
        if film_count >= count:
            break

    movie = pd.DataFrame(data=movie_list)
    movie.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

# 获取分类、上映日期
def get_film_info(link):
    regex = r"\d\d\d\d-\d\d-\d\d"
    movie_class = []
    response = requests.get(link, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('li', attrs={'class':'ellipsis'}):
        if tags.find_all('a', ) != []:
            for atags in tags.find_all('a',):
                movie_class.append(atags.get_text())
            continue
        film_info = tags.get_text()
        # 上映日期
        pattern = re.compile(regex)
        match_list = pattern.findall(film_info)
    
        if match_list:
            film_time = film_info

    return (movie_class, film_time)

crawl_film(10)