# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GiveindiaItem(scrapy.Item):
    # define the fields for your item here like:
    ngo_name = scrapy.Field()
    ngo_url = scrapy.Field()
    ngo_cause = scrapy.Field()
    ngo_city = scrapy.Field()
    ngo_state = scrapy.Field()
    
