# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']

    #def parse(self, response):
        #pass
    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        #for i in range(0, 10):
        url = f'https://maoyan.com/films?showType=3&sortId=1'
        return scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')


        ans = []
        '''
        # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
        for tags in soup.find_all('div', attrs={'class': 'movie-item film-channel'},limit=10):

        title_list = soup.find_all('div', attrs={'class': 'hd'})
        #for i in range(len(title_list)):
        # 在Python中应该这样写
        for i in title_list: '''
