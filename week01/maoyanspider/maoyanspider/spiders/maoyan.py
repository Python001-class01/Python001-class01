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
        'Cookie': '__mta=175526813.1592845237500.1592969032485.1592969232874.10; uuid_n_v=v1; uuid=E386DAC0B4A911EAACB6BBD781D89938787DFDB6AB144B8BB7BCDA252EE20E80; mojo-uuid=07d9ac28c4af0e46a8f98a3353933dc0; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592845237; _lxsdk_cuid=172dcf97ca5c8-0fd5444e050b77-143f6257-13c680-172dcf97ca5c8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172e454ce7aa02-0685a4a43d46a-2076244f-327200-172e454ce7b741%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172e454ce7aa02-0685a4a43d46a-2076244f-327200-172e454ce7b741%22%7D; _lxsdk=E386DAC0B4A911EAACB6BBD781D89938787DFDB6AB144B8BB7BCDA252EE20E80; __mta=175526813.1592845237500.1592969021189.1592969032485.9',
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
