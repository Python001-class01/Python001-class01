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

        
        url = f'https://maoyan.com/board/4'
        yield scrapy.Request(url=url,headers=header,callback=self.parse)

    from scrapy.shell import inspect_response
    def parse(self, response):
        soup = bs(response.text,'html.parser')
        for i in soup.find_all('div',attrs={'class' : 'movie-item-info'}):
            item = MaoyanspidersItem()
            title = i.find('p',attrs={'class':'name'}).find('a')
            name = title.get('title')
            link = 'https://maoyan.com'+ title.get('href')           
            time = i.find('p',attrs={'class' : 'releasetime'}).text
            item['films_name'] = name
            item['release_time'] = time
            print(link)
            yield scrapy.Request(url=link, meta={'item':item},callback=self.parse1)


    def parse1(self, response):
        item = response.meta['item']
        soup = bs(response.text,'html.parser')
        print(soup)
        item['films_type'] = 'type'
        print(item)
        yield item



