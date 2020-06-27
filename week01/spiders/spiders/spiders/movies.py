# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import sys
sys.path.append("..")
import items


# from maoyan_scrapy.items import MaoyanMovieItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']

    # def parse(self, response):
    # pass
    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    '''
    def start_requests(self):
        # for i in range(0, 10):
        url = f'https://maoyan.com/films?showType=3&sortId=1'
        print(4444)
        return scrapy.Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
        '''

    # 解析函数,不会xpath 参考同学的代码
    def parse(self, response):
        tags = Selector(response=response).xpath(
            '//div[@class="movie-item film-channel"]')
        count = -1
        for tag in tags:
            # 只取前10个电影
            count += 1
            if count >= 10: break

            # 电影名称的class和别的hover信息不同，可以直接通过class定位
            movie_title = tag.xpath('.//span[contains(@class,"name")]/text()').extract_first()

            # 获取其它hover信息
            hover_texts = tag.xpath('.//span[@class="hover-tag"]/../text()').extract()
            # 通过xpath定位时多出了很多\n，数据索引有变化
            movie_type = hover_texts[1].strip('\n').strip()
            movie_time = hover_texts[5].strip('\n').strip()
            print(movie_title, movie_type, movie_time)
            item = items.SpidersItem()
            item['title'] = movie_title
            item['info'] = movie_type
            item['post_time'] = movie_time

            yield item
