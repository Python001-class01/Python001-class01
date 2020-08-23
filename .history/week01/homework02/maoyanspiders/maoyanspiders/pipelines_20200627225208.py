# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanspidersPipeline(object):
    def process_item(self, item, spider):
        films_name = item['films_name']
        films_type = item['films_type']
        release_time = item['release_time']
        output = f'|{films_name}|\t|'
