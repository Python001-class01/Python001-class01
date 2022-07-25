# 使用BeautifulSoup解析网页
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# bs4是第三方库需要使用pip命令安装
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
header = {'user-agent': user_agent,
          "cookie": '''__mta=245610043.1592894791939.1592894914700.1592908735626.7; uuid_n_v=v1; uuid=857B70C0B51D11EAB787AF911C0DA1B7F3C1C51002E94B59A3693439B0C6EB99; _lxsdk_cuid=172dfed9ffcc8-0869fbacef4019-581b3318-1fa400-172dfed9ffcc8; _lxsdk=857B70C0B51D11EAB787AF911C0DA1B7F3C1C51002E94B59A3693439B0C6EB99; mojo-uuid=cb08f78324b79bec583cc4cebe6b8613; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _csrf=d20e042478683f338bcc95f1e47ceb831249627bb3e9d840fcad685bb92dc8b2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592908632,1592909512,1592913676,1592913770; mojo-session-id={"id":"51d97df08107221c636d50edccbf46f6","time":1592956442893}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592956454; __mta=245610043.1592894791939.1592908735626.1592956454252.8; mojo-trace-id=3; _lxsdk_s=172e39a589a-928-a57-4a9%7C%7C5'''}
myurl = 'https://maoyan.com/films?showType=3&sortId=1'
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')
ans = []
# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'},limit=10):
    a = tags.find('span', ).text
    filmname = tags.find_all('div', attrs={'class': 'movie-hover-title'})
    for k in filmname:
        if "类型" in k.text:
            print(k.text[19:].strip())
            b = k.text[19:].strip()
        if "上映时间" in k.text:
            c = k.text[21:].strip()
    ans.append((a, b, c))

mv = pd.DataFrame(data=ans)
mv.to_csv("./mv.csv", encoding="utf8", index=False, header=False)
