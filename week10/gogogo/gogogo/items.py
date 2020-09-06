# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class GogogoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uid=scrapy.Field()
    shoujiming2 = scrapy.Field()
    pinglunshu2 = scrapy.Field()
    phonelink2 = scrapy.Field()
    good =scrapy.Field()
    bad =scrapy.Field()
    comments = scrapy.Field()

         

    


