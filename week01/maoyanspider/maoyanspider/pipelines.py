# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        movie_list = []
        movie_list.append(item['movie_name'])
        movie_list.append(item['movie_type'])
        movie_list.append(item['movie_date'])

        movie = pd.DataFrame(data = movie_list)
        movie.to_csv('movie_info.csv', encoding='utf8', mode='a', index=False, header=False)
        return item
