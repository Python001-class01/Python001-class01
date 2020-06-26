 # 使用requests，bs4库，爬取猫眼电影top10的电影名称、电影类型、上映时间，并以utf-8的字符集保存到csv文件中

import requests
from bs4 import BeautifulSoup as bs
    
maoyanUrl = "https://maoyan.com/board/4";
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
header = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Cookie' : '__mta=251934006.1593072991075.1593100662316.1593100664951.15; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; __mta=251934006.1593072991075.1593075275703.1593078726963.7; mojo-session-id={"id":"435818e6a726415f46defffa27f7abc6","time":1593100221937}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593100665; mojo-trace-id=17; _lxsdk_s=172ec2bff67-0c2-e9f-c64%7C%7C24__mta=251934006.1593072991075.1593100690175.1593100868002.17; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; __mta=251934006.1593072991075.1593075275703.1593078726963.7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593100868; _lxsdk_s=172ee2f4a3e-1c2-3a1-5a4%7C%7C1__mta=251934006.1593072991075.1593133988033.1593140260525.19; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; __mta=251934006.1593072991075.1593134712257.1593134712989.9; mojo-session-id={"id":"b78cc9fcb57a627220ec165f84d9d5a9","time":1593140260318}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593140260; _lxsdk_s=172ee8f28d1-560-08-4aa%7C%7C3',
    # 'Host' : 'http://www.baidu.com',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

def get_urls(url, headers):
    response = requests.get(url,headers=header)   
    bs_info = bs(response.text,"html.parser")

    import re

    films_url = []
    for tag in bs_info.find_all('div',):
       for tag_p in tag.find_all('a',href=re.compile('/films/')) :
           # 获取top10电影详情页链接
           films_url.append(url + tag_p.get('href'))

    urls = set(films_url)
    return urls

import pandas
# 获取详情页
def get_page_info(self,urls,header):
    films_content = []
    for url in urls:
        content = get_page_content(self,url,header)
        films_content.append(content)
    return films_content

# 获取单个电影的详情信息
def get_page_brief(url,header):
    import re
    response = requests.get(url, headers=header)
    bs_info = bs(response.text,'html.parser')
    # print(response.text)
    atag =  bs_info.find('div',attrs={'class':'banner'})
    film_name = atag.find('h1').text +" "+ atag.find('div',attrs = {'class' : 'ename ellipsis'}).text
    film_type = ""
    for type in atag.find_all('a',attrs={'target':'_blank'}):
        film_type = film_type + type.text
    tags = atag.find_all('li')
    online_time = tags[-1].text
    brief = [film_name,film_type,online_time]
        
    return brief

def save_movies(movies):
    movies_data = pd.DataFrame

def main():
    #urls = get_urls(maoyanUrl,header)
    #contents = get_page_info(self,urls,header)
    #print(urls)
    page_1 = 'https://maoyan.com/films/1375'
    brief = get_page_brief(page_1,header)
    save_movies(movies)
    print(brief)


if __name__ == '__main__':
    main()