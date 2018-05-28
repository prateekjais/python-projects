# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IplscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    match_date = scrapy.Field()
    match_name = scrapy.Field()
    match_venue = scrapy.Field()
    match_time = scrapy.Field()
    match_result = scrapy.Field()
    
