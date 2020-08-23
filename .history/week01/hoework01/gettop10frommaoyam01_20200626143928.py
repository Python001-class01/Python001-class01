 # 使用requests，bs4库，爬取猫眼电影top10的电影名称、电影类型、上映时间，并以utf-8的字符集保存到csv文件中

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
    
maoyanUrl = "https://maoyan.com/board/4";
header = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Cookie' : '__mta=251934006.1593072991075.1593140975947.1593145816387.21; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; __mta=251934006.1593072991075.1593140975947.1593145813576.21; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593145819; _lxsdk_s=172ef3adc93-67a-f25-f7b%7C%7C1',
    # 'Host' : 'http://www.baidu.com',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

def get_urls(url, headers):
    main_url = 'https://maoyan.com'
    response = requests.get(url,headers=header)   
    bs_info = bs(response.text,"html.parser")

    films_url = []
    for tag in bs_info.find_all('div',):
       for tag_p in tag.find_all('a',href=re.compile('/films/')) :
           # 获取top10电影详情页链接
           films_url.append(main_url + tag_p.get('href'))

    urls = set(films_url)
    return urls

import pandas
# 获取详情页
def get_page_info(urls,header):
    films_content = []
    for url in urls:
        content = get_page_brief(url,header)
        #print(content)
        films_content.append(content)
    return films_content

# 获取单个电影的详情信息
def get_page_brief(url,header):
    response = requests.get(url, headers=header)
    bs_info = bs(response.text,'html.parser')
    atag =  bs_info.find('div',attrs={'class':'banner'})
    film_name = atag.find('h1').text +" "+ atag.find('div',attrs = {'class' : 'ename ellipsis'}).text
    film_type = ""
    for type in atag.find_all('a',attrs={'target':'_blank'}):
        film_type = film_type + type.text
    tags = atag.find_all('li')
    online_time = tags[-1].text
    brief = [film_name,film_type,online_time]
        
    return brief

# 保存movie信息
def save_movies(movies):
    print(movies)
    for movie in 
    movies_data = pd.DataFrame(data=movies)
    movies_data.to_csv('./top10.csv',encoding='utf-8',index=False,header=False)

def main():
    urls = get_urls(maoyanUrl,header)
    print(urls)
    movies = get_page_info(urls,header)
    save_movies(movies)


if __name__ == '__main__':
    main()