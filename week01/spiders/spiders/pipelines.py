# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#from itemadapter import ItemAdapter
import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        movie_list = []
        movie_list.append((item['title'], item['info'], item['post_time']))
        movies = pd.DataFrame(data=movie_list)
        movies.to_csv('./movies2.csv', encoding='utf8', mode='a', index=False, header=False)
        return item
