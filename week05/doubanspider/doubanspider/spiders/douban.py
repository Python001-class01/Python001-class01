# -*- coding: utf-8 -*-
import scrapy
import json
from fake_useragent import UserAgent
from scrapy.utils.python import to_unicode
from bs4 import BeautifulSoup
import lxml.etree
from doubanspider.items import DoubanspiderItem

douban_rate = {'力荐': 5, '推荐': 4, '还行': 3, '较差': 2, '很差': 1}


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]

    handle_httpstatus_list = [301, 302]

    # ua = UserAgent()
    # headers = {
    #     'Accept': 'application/json',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'bid=4JrQ8aU7wfo; ll="118318"; douban-fav-remind=1; __utmc=30149280; _vwo_uuid_v2=DF6060A6081460A4E255F3ED6F2E3DA00|cc4c8d8f4437bb875dca441e28adc4ca; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1596036266; _ga=GA1.2.1677349363.1579332922; _gid=GA1.2.2087354240.1596036266; talionnav_show_app="0"; __utmz=30149280.1596113729.12.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1596115642; ap_v=0,6.0; __utma=30149280.1677349363.1579332922.1596113729.1596115744.13; __utmt=1; __utmb=30149280.2.10.1596115744',
    #     'Host': 'douban.com',
    #     'User-Agent': ua.random,
    #     'Referer': 'https://movie.douban.com/subject/1292064/'
    # }

    def start_requests(self):
        url = "https://movie.douban.com/subject/1292064/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info("got response %d for %r" %
                         (response.status, response.url))
        # 获取“更多短评”链接
        selector = lxml.etree.HTML(response.text)
        # self.logger.info(selector.xpath('//*[@id="comments-section"]/div[1]/h2/span/a'))
        # 如果一直不行就用beautifulsoup
        more_comment = selector.xpath(
            '//*[@id="comments-section"]/div[1]/h2/span/a/@href')

        # self.logger.info(more_comment)
        yield scrapy.Request(url=more_comment[0], callback=self.parse_comment)

    def parse_comment(self, response):
        # self.logger.info("parse_comment got response %d for %r" %
        #                  (response.status, response.url))
        # test1
        # with open('text.html', 'w') as f:
        #     f.write(response.text)
        for i in range(1, 21):
            items = DoubanspiderItem()
            cid = response.xpath(f'//*[@id="comments"]/div[{i}]/@data-cid')[0].get()
            comment = response.xpath(
                f'//*[@id="comments"]/div[{i}]/div[2]/p/span/text()')[0].get()
            rate_text = response.xpath(
                f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]/@title')[0].get()
            self.logger.info(cid)
            try:
                items['cid'] = cid
                items['comment'] = comment
                # self.logger.info(comment)
                # self.logger.info(rate_text)
                items['rate'] = douban_rate[rate_text]
                # self.logger.info(items['comment'])
                # self.logger.info(items['rate'])
            except Exception as e:
                self.logger.error(e)
                return
            yield items
