# -*- coding: utf-8 -*-
import scrapy
import uuid
from scrapy.selector import Selector
import sys
sys.path.append("..")
import items
import time

class MaiSpider(scrapy.Spider):
    name = 'mai'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']
    #这里就不翻页了，下面评论里面有翻页功能，不过为了防止被反爬，手工限制了。
    # 每日任务的工作机理，根据 xxx 楼 ，也可以根据，字段里面包括，几个小时前，
    #  爬虫第一次，爬取多天的，或者全部的，以后，每次爬取，用“小时” 做过滤，
    # 不是当天的不写入数据库。
    #def start_requests(self):
     #   for i in range(1, 2):
      #      url = f'https://www.smzdm.com/fenlei/qipaoshui/p{i}'
       #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #//*[@id="feed-main-list"]
        #//*[@id="feed-main-list"]/li[1]/div/div[2]/h5/a
        #tags = Selector(response=response).xpath(
            #'//*[@id="feed-main-list"]')
        #print(tags)
        #i=0
        #for tag in tags:
           # i+=1
        #good= Selector(response=response).xpath('//*[@class="unvoted-wrap"]/span[1]')
        #gg=[]
        good= Selector(response=response).xpath(
               '//*[@class="unvoted-wrap"]')
        lala=[]
        for i in good:
            tw= i.xpath('./span[1]/text()').extract()
            lala+=tw
            #print(tw)
        #print(len(lala))    
        #print(lala,"------------999----------------------")

        for i in range(1,31):
            shoujiming= f'//*[@id="feed-main-list"]/li[{i}]/div/div[2]/h5/a/text()'
            #     <span _hover-ignore="1">5</span>                                   /li[2]/div/div[2]/div[4]/div[1]/a[2]/span
            
            #[@id="feed-main-list"]/li[1]/div/div[2]/h5/a
            #print("868===",temp)
            #span[contains(@_hover-ignore,"1")]
            #movie_title = tag.xpath('.//span[contains(@class,"name")]/text()').extract_first()
            shoujiming2 =Selector(response=response).xpath(shoujiming).extract()
            #//*[@id="feed-main-list"]/li[2]/div/div[2]/div[4]/div[1]/a[2]/span
            #//*[@id="feed-main-list"]/li[28]/div/div[2]/div[3]/div[1]/a[2]/span
            pinglunshu=shoujiming[:-11]+'div[4]/div[1]/a[2]/span/text()'
            pinglunshu2 =Selector(response=response).xpath(pinglunshu).extract()
            #//*[@id="feed-main-list"]/li[25]/div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span
            #//*[@id="feed-main-list"]/li[25]/div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span

            #good=shoujiming[:-23]+ \
             # '/div/div[2]/div[4]/div[1]/span/a[2]/span[1]'+\
             ## '/i[contains(@class,"icon-zhi-o-thin")]/span/'
            #good= Selector(response=response).xpath(good)  #.extract()
            #good= Selector(response=response).xpath('//*[@class="unvoted-wrap"]/span[1]/text()')
            
            #print(good,"----------------------------------")
            #<i class="icon-buzhi-o-thin"></i>
            '''bad= shoujiming[:-23]+ \
              '/div/div[2]/div[4]/div[1]/span/a[2]/span[1]'+\
              '/i[contains(@class,"icon-buzhi-o-thin")]/span/'
              '''
            #//*[@id="feed-main-list"]/li[24]/div/div[2]/div[3]/div[1]/span/a[1]/span[1]/i
            #/div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span <i class="icon-zhi-o-thin"></i>
            #/div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span
            #bad = Selector(response=response).xpath(bad)   #.extract()
            #print(bad)
            if pinglunshu2==[]:
                pinglunshu=shoujiming[:-11]+'div[3]/div[1]/a[2]/span/text()'
                pinglunshu2 =Selector(response=response).xpath(pinglunshu).extract()
                #good="9898"
                #bad="9797"

            phonelink=shoujiming[:-23]+'/div/div[2]/h5/a/@href'
            phonelink2 =Selector(response=response).xpath(phonelink).extract()
            
            #print(shoujiming2,pinglunshu2,phonelink2)
            #tt=tag.xpath('./text()').extract()
            #print("tttttttttt",tt[0])
        #print(12345888888888888888888889999989999999)
            item = items.GogogoItem()
            item['uid']=uuid.uuid1()
            item['shoujiming2'] = shoujiming2[0]
            item['pinglunshu2'] = pinglunshu2[0]
            uurl=phonelink2[0]
            item['phonelink2'] = uurl
           
            item['good']= lala[2*i-2]
            item['bad']=lala[2*i-1]
           # yield scrapy.Request(url=uurl , meta={'item':item},
                      #    callback=self.parse3 )
            #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            """"""
            shu =int(item['pinglunshu2'] )
            if shu>0:
                pages = shu//30+2
                #for i in range(1,pages):  fanpa
                for i in range(1,3):
                    url2=uurl+"p"+str(i)
                    print(url2)
                    time.sleep(0.125)
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    yield scrapy.Request(url=url2 , meta={'item':item},
                          callback=self.parse3 )
            else:
                yield item#""""""

#插入硬翻页功能，第一次爬取，把值取较大的数，以后每天爬取取10 页。
    def parse2(self, response):
        item =response.meta['item']
        uurl2= item['phonelink2'] 

        pinglunshu33=item['pinglunshu2'] 
        if pinglunshu33=="0":
            yield item
        else:
            pages =int(pinglunshu33)//30+2
            #for i in range(pages): 被发现
            for i in range(1,5):
                time.sleep(0.5)
                uurl3 = uurl2+'p'+str(i)
                yield scrapy.Request(url=uurl3 , meta={'item':item},
                      callback=self.parse3 )

    def parse3(self, response):
        item =response.meta['item']
        gg='//li[@class="comment_list"]'
        details = Selector(response=response).xpath(gg) 
        
        mlist=[]

        #cankao fengxiao daima

        if details:
            for detail in details:
                publisher = str(detail.xpath('./div[2]/div[1]/a/span/text()').extract_first().strip('\n').strip())
                datePublished = str(detail.xpath('./div[2]/div[1]/div[1]/meta/@content').extract_first().strip('\n').strip())
                timePublished = str(detail.xpath('./div[2]/div[1]/div[1]/text()').extract_first().strip('\n').strip())
                comment = str(detail.xpath('./div[2]/div[3]/div[1]/p/span/text() | ./div[2]/div[2]/div[1]/p/span/text()').extract_first().strip('\n').strip())
                print(f'评论内容：{publisher}-{datePublished}-{timePublished}-{comment}')
                dict2 = {'uid':item['uid'],'publisher':publisher,'datePublished': datePublished,'timePublished':timePublished, 'comment':comment}
                mlist.append(dict2)

        item['comments'] = mlist
        yield item

'''
import ast
import datetime
import re

import scrapy
from crawl_utils.scrapy.core import ErrorCallback

from ..items import ArticleItem, CommentItem


class GoodsSpider(scrapy.Spider, ErrorCallback):
    name = 'goods'
    allowed_domains = ['smzdm.com']

    def __init__(self, category, limit=30):
        # i.e. qipaoshui
        self.category = category
        self.count = 0
        self.limit = int(limit)
        self.position_dict = {
            "沙发": "1楼",
            "椅子": "2楼",
            "板凳": "3楼",
        }
        self._datetime = datetime.datetime
        self._timedelta = datetime.timedelta
        self.minutes_ago_pattern = re.compile(r"(\d+)分钟前")
        self.hours_ago_pattern = re.compile(r"(\d+)小时前")
        self.img_emotion_pattern = re.compile(r"""<img[^>]*alt="([^"]+)"[^>]*>""")
        self.img_mosaic_pattern = re.compile(r"""<img[^>]*mosaic[^>]*>""")
        self.MOSAIC = "[MOSAIC]"
        self.tag_pattern = re.compile(r"<[^>]*>")
        self.emotion_space_pattern = re.compile(r"(?<=])\ +(?=\[)")

    def start_requests(self):
        url = f"https://www.smzdm.com/fenlei/{self.category}/"
        yield scrapy.Request(url, meta={'count': 0}, errback=self.errback)

    def parse(self, response):
        count = response.meta['count']
        for div in response.css("#feed-main-list li > div"):
            count += 1
            if count > self.limit:
                break
            title_tag = div.css("h5 a")
            article_url = title_tag.xpath("@href").get()
            article_id = title_tag.xpath("@href").re_first(r"/p/(\d+)")
            article_data = title_tag.xpath("@onclick").re_first(r"push\((.*)\)")
            article_data = ast.literal_eval(article_data)
            position = article_data['position']
            article_title = article_data['pagetitle']
            mall = article_data['商城']
            img = div.css(".z-feed-img a img::attr(src)").get()
            img = response.urljoin(img)

            yield ArticleItem(**{
                'id': article_id,
                'title': article_title,
                'url': article_url,
                'position': position,
                'mall': mall,
                'img': img,
            })
            yield scrapy.Request(article_url, callback=self.parse_comments, meta={'article_id': article_id},
                                 errback=self.errback)

        next_url = response.css(".feed-pagenation .next-page a::attr(href)").get()
        if count <= self.limit and next_url:
            yield scrapy.Request(next_url, meta={'count': count}, errback=self.errback)

    def parse_comments(self, response):
        article_id = response.meta['article_id']
        goods_type = response.css("div.crumbs a > span::text").getall()[-1]
        for li in response.css("#commentTabBlockNew li.comment_list"):
            user_info = self._parse_user_info(li.css(".comment_avatar_time > a.user_name"))
            position = li.css(".comment_avatar span.grey::text").get()
            position = self.position_dict.get(position, position)
            pub_time = self._parse_time(li)
            come_from = li.css("span.come_from a::text").get()
            comment_tag = li.css(".comment_conBox > .comment_conWrap .comment_con")
            comment_id = comment_tag.css("input::attr(comment-id)").get()
            comment_info = self._parse_comments(comment_tag.css("p").get())
            # More comments quote, i.e: https://www.smzdm.com/p/8908644/
            # 回复别人的评论时, 有可能有多条, 超过3条页面上会隐藏,而获取所有的记录需要发请求
            # 因此这里不记录每条评论下所有引用的评论(如果有的话),而是记录最后一条引用的评论
            # 若需要还原为完整的回复链, 根据该字段递归查找
            comment_quote_id = li.css(
                ".comment_conBox > .blockquote_wrap > blockquote:last-child::attr(blockquote_cid)").get()
            yield CommentItem(**{
                'id': f"{article_id}_{comment_id}",
                'article_id': article_id,
                **user_info,
                'goods_type': goods_type,
                'position': position,
                'pub_time': pub_time,
                'come_from': come_from,
                'comment_id': comment_id,
                'comment_info': comment_info,
                'comment_quote_id': comment_quote_id,
            })

        # i.e. https://www.smzdm.com/p/23523045/
        next_url = response.css("#commentTabBlockNew .pagination .pagedown a::attr(href)").get()
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse_comments, meta={'article_id': article_id},
                                 errback=self.errback)

    def _parse_user_info(self, tag):
        return {
            'user_name': tag.css("span::text").get(),
            'user_id': tag.xpath("@usmzdmid").get(),
            'user_url': tag.xpath("@href").get(),
        }

    def _parse_comments(self, html):
        """保留表情顺序
        样例: https://regex101.com/r/CrHF9B/1  (v1/v2/v3)
        """
        if not html:
            return html
        if self.img_emotion_pattern.search(html):
            html = self.img_emotion_pattern.sub("\g<1>", html)
        if self.img_mosaic_pattern.search(html):
            # i.e. https://www.smzdm.com/p/23645559/
            html = self.img_mosaic_pattern.sub(self.MOSAIC, html)
        html = self.tag_pattern.sub("", html)
        html = self.emotion_space_pattern.sub("", html)
        if html:
            html = html.strip()
        return html

    def _parse_time(self, sel):
        def _outtime(ptime):
            return ptime.strftime("%Y-%m-%d %H:%M")

        pub_time1 = sel.css(".time meta::attr(content)").get()
        pub_time2 = sel.css(".time::text").get()
        pub_time = self._datetime.strptime(pub_time1, "%Y-%m-%d")

        try:
            # https://www.smzdm.com/p/23523045/p3/#comments
            tmp = self._datetime.strptime(pub_time2, "%m-%d %H:%M")
            pub_time = pub_time.replace(month=tmp.month, day=tmp.day, hour=tmp.hour, minute=tmp.minute)
            return _outtime(pub_time)
        except ValueError:
            if pub_time2 == pub_time1 or not pub_time2:
                # https://www.smzdm.com/p/8908644
                return _outtime(pub_time)
            elif self.hours_ago_pattern.search(pub_time2):
                hour = int(self.hours_ago_pattern.search(pub_time2).group(1))
                pub_time = self._datetime.now() - self._timedelta(seconds=hour * 3600)
                return _outtime(pub_time)
            elif self.minutes_ago_pattern.search(pub_time2):
                minutes = int(self.minutes_ago_pattern.search(pub_time2).group(1))
                pub_time = self._datetime.now() - self._timedelta(seconds=minutes * 60)
                return _outtime(pub_time)
        return _outtime(pub_time)
'''