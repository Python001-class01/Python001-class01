 # 使用requests，bs4库，爬取猫眼电影top10的电影名称、电影类型、上映时间，并以utf-8的字符集保存到csv文件中

import requests
    
maoyanUrl = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0'
header = {'user-agent' : user_agent}
response = requests.get(maoyanUrl,headers=header)   
response.encoding = 'utf-8' 
print(response.text)