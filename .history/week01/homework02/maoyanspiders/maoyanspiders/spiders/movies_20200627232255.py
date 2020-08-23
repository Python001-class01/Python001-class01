# -*- coding: utf-8 -*-
import scrapy
from maoyanspiders.items import MaoyanspidersItem
# import xlml.etree
from bs4 import BeautifulSoup as bs

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4']

    # def parse(self, response):
    #     pass
    def start_requests(self):

        header = {
            'Content-Type': 'text/plain; charset=UTF-8',
            'Cookie' : '__mta=251934006.1593072991075.1593267136578.1593267143630.29; uuid_n_v=v1; uuid=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; _csrf=8557626db9b655cf9050ae7e5b2aab69278c8061c21eca95e1c3cf2130b0b64c; _lxsdk_cuid=172ea8cb247c8-0a73066b1c0a8b-4353760-100200-172ea8cb248c8; _lxsdk=2395D3F0B6BC11EA9F28E30FF5FFF73C9A16AE2FA53A448DA75AEAA9D715CB59; mojo-uuid=c457eacb7c1eb59d3d2f6c1f8d75b9c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593072989,1593073002; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; __mta=251934006.1593072991075.1593140975947.1593145813576.21; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593267144; _lxsdk_s=172f6570f57-262-d57-29%7C%7C1',
            # 'Host' : 'http://www.baidu.com',
            'Origin': 'https://maoyan.com',
            'Referer': 'https://maoyan.com/board/4',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        }
        url = f'https://maoyan.com/board/4'
        yield scrapy.Request(url=url,headers=header,callback=self.parse)

    def parse(self, response):
        soup = bs(response.text,'html.parser')
        for i in soup.find_all('div',attrs={'class' : 'movie-item-info'}):
            item = MaoyanspidersItem()
            title = i.find('p',attrs={'class':'name'}).find('a')
            name = title.get('title')
            link = 'https://maoyan.com/'+ title.get('href')           
            time = i.find('p',attrs={'class' : 'releasetime'}).text
            item['films_name'] = name
            item['release_time'] = time
            yield scrapy.Request(url=link, meta={'item':item},callback=self.parse1)



    def parse1(self, response):
        item = response.meta['item')
        soup = bs(response.text,'html.parser')
        type =  soup.find('div',attrs={'class' :'movie-brief-container'}).find_all('li')[0]
        item['films_type'] = type
        yield item



