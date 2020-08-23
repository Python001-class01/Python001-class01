 # 使用requests，bs4库，爬取猫眼电影top10的电影名称、电影类型、上映时间，并以utf-8的字符集保存到csv文件中

import requests
from bs4 import BeautifulSoup as bs
    
maoyanUrl = "https://maoyan.com/board/4";
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
header = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Cookie' : '__mta=251934006.1593072991075.1593075273346.1593075275703.6; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; mojo-session-id={"id":"dd5ec1780230b10b3b01a18882424620","time":1593078373432}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593078727; __mta=251934006.1593072991075.1593075275703.1593078726963.7; mojo-trace-id=3; _lxsdk_s=172eade6a22-b72-c5-308%7C%7C6',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
response = requests.get(maoyanUrl,headers=header)   
response.encoding = 'utf-8' 
bs_info = bs(response.text,"html.parser")


# print(response.text)
app_link = bs_info.find('div')
for tags in bs_info.find_all('div',id = 'app'):
    print(tags)
    for tag in tags.find_all('a',):
        print(tag.get('href'))
        print(tag.get('title'))
       