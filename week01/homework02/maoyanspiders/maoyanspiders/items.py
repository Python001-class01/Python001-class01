# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanspidersItem(scrapy.Item):
    # define the fields for your item here like:
    films_name = scrapy.Field()
    release_time = scrapy.Field()
    films_type = scrapy.Field()
    # pass

