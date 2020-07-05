import requests
from fake_useragent import UserAgent
from config import configs

ua = UserAgent(verify_ssl=False)

headers = {
    'Authority': 'shimo.im',
    'Path': '/lizard-api/auth/password/login',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'X-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
    'User-Agent':ua.random,
    'Referer':'https://shimo.im/login?from=home'
}

s = requests.Session()
url = "https://shimo.im/login?from=home"

pre_req = s.get(url, headers=headers)

login_url = "https://shimo.im/lizard-api/auth/password/login"

from_data = {
    'email':configs['username'],
    'mobile':'+86undefined',
    'password':configs['password']
}

response = requests.post(login_url, data=from_data, headers=headers, cookies=s.cookies)

print(response)