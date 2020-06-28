# -*- coding: utf-8 -*-
import scrapy
from maoyanspiders.Items importMaoyanspidersItem
# import xlml.etree
from bs4 import BeautifulSoup as bs

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'https://maoyan.com/board/4'
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        soup = bs(response.text,'html.parser')
        print(soup.text)
        return soup
        item = MaoyanspidersItem()
        item['name'] = 'name'
        return  item


