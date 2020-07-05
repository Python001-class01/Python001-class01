# -*- coding: utf-8 -*-
import scrapy
import requests
import lxml.etree

from maoyanspider.items import MaoyanspiderItem
from fake_useragent import UserAgent

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    ua = UserAgent()
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'maoyan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':ua.random
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        for selector in response.xpath('//div[@class="movie-hover-info"]')[:10]:
            item = MaoyanspiderItem()
            item['movie_name'] = selector.xpath('./div[1]/span[1]/text()').extract_first()
            item['movie_date'] = selector.xpath('./div[4]/text()[2]').extract_first().strip()
            item['movie_type'] = selector.xpath('./div[2]/text()[2]').extract_first().strip()
            yield item
