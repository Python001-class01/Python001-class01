# -*- coding: utf-8 -*-
# 第二周 作业一：
# 为 Scrapy 增加代理 IP 功能。
# 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
# 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。
import scrapy
from scrapy.selector import Selector
import sys
sys.path.append("..")
import items

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']
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