# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#from itemadapter import ItemAdapter

import os
import sys
import re
import datetime
sys.path.append("..")
from DBOperator import DBOperation as db

print("当前的工作目录：" + os.getcwd())
print("python搜索模块的路径集合：", sys.path)

class GogogoPipeline:

    def process_item(self, item, spider):
        uid=item['uid']
        shoujiming2 = item['shoujiming2']
        pinglunshu2 = item['pinglunshu2']
        phonelink2 = item['phonelink2']
        good = item['good']
        bad = item['bad']
        cclist = item['comments']
        sql = f"""INSERT INTO phone_info(uid,shoujiming2, pinglunshu2, phonelink2,good,bad) \
         VALUES ("{uid}","{shoujiming2}", "{pinglunshu2}", "{phonelink2}","{good}","{bad}");"""
        
        db.run(sql)
        comment_values=[]
        #评论很多，写在另一个表中，
        for onedict in cclist:
            if '小时' in onedict['timePublished'] :
                shijian = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
            else:
                shijian = f"{onedict['datePublished']} 01:02:03"
            
            print(shijian,"---time-------")
            #(onedict['uid'], onedict['publisher'], shijian, onedict['comment'])
            sql2 = f"""INSERT INTO pinglun(uid,publisher, shijian, comment) \
                    VALUES ("{onedict['uid']}","{onedict['publisher']}", 
                    "{shijian}", "{ onedict['comment']}");"""
        
            db.run(sql2)
        print(88888888888888888888877777777888888888888)
        return item


''' 参考别人的代码

 dict2 = {'uid':item['uid'],'publisher':publisher,
 'datePublished': datePublished,
 'timePublished':timePublished, 'comment':comment}

                mlist.append(dict2)
   def process_item(self, item, spider):
        if type(item) == ArticleItem:
            table = 'article'
        elif type(item) == CommentItem:
            table = 'comment'
        keys = ', '.join(item.keys())
        values = ', '.join([f'%({i})s' for i in item])
        add_item = ("INSERT INTO %s (%s) VALUES (%s)" % (table, keys, values))
        try:
            self.cursor.execute(add_item, dict(item))



            shoujiming= f'//*[@id="feed-main-list"]/li[{i}]/div/div[2]/h5/a/text()'
            shoujiming2 =Selector(response=response).xpath(shoujiming).extract()
          
            pinglunshu=shoujiming[:-11]+'div[4]/div[1]/a[2]/span/text()'
            pinglunshu2 =Selector(response=response).xpath(pinglunshu).extract()
          
            good=shoujiming[:-23]+ \
              '/div/div[2]/div[4]/div[1]/span/a[2]/span[1]'+\
              '/i[contains(@class,"icon-zhi-o-thin")]/span/'
            good= Selector(response=response).xpath(good)  #.extract()
            print(good)
           
            bad= shoujiming[:-23]+ \
              '/div/div[2]/div[4]/div[1]/span/a[2]/span[1]'+\
              '/i[contains(@class,"icon-buzhi-o-thin")]/span/'
           
            bad = Selector(response=response).xpath(bad)   #.extract()
            print(bad)
'''





