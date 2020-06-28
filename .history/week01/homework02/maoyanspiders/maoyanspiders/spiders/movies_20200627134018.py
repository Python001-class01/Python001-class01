# -*- coding: utf-8 -*-
import scrapy
from movies.Item import MaoyanspidersItem
import xlml.etree

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com\']
    start_urls = ['http://maoyan.com\/']

    # def parse(self, response):
    #     pass
    def start_request(self):
        url = f'https://maoyan.com/board/4'
        yield scrapy.request(url=url,callback=self.parse)

    def parse(self, response):


