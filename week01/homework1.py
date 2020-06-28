import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd



user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
myurl = 'https://maoyan.com/films?showType=3'
Cookies = r'_lxsdk_cuid=172fa2440c1c8-00c12e2c7c14d-f7d123e-144000-172fa2440c2c8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593334579; uuid_n_v=v1; iuuid=33A1FC00B91F11EAA88EED20607A9D691AC71F4EF6184B61A70B3553A77CDFC8; webp=true; ci=963%2C%E9%9B%86%E7%BE%8E; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172fa312f5e382-0f468bd0313aa7-2076244f-2646588-172fa312f5f2e1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172fa312f5e382-0f468bd0313aa7-2076244f-2646588-172fa312f5f2e1%22%7D; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593335431; _lxsdk=3AF953B0B91D11EA842AD7B3BE0152F2F305CA8818BF4DF9858CEAD1A281BFE9; __mta=140998925.1593334580166.1593335295182.1593335431113.3; _lxsdk_s=172fa5dd3b7-52f-404-ded%7C%7C1'

header = {'user-agent': user_agent, 'Cookie': Cookies}
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')

movies_info = {'title': [], 'type': [], 'date': []}
for tags in bs_info.find_all('div', attrs={'class': 'classic-movies'}):
    sleep(1)

    for atag in tags.find_all('a'):
        sleep(1)
        title = atag.find('div', attrs={'class': 'title line-ellipsis'}).get_text()
        MovieType = atag.find('div', attrs={'class': 'actors line-ellipsis'}).get_text()
        date = atag.find('div', attrs={'class': 'show-info line-ellipsis'}).get_text()
        movies_info['title'].append(title)
        movies_info['type'].append(MovieType)
        movies_info['date'].append(date)


ten_movies = pd.DataFrame(movies_info)
ten_movies.to_csv('./TopTen_movies.csv', encoding='UTF-8', index=False, header=False)