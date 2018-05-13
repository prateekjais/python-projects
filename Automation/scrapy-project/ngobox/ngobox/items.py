# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NgoboxItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    location = scrapy.Field()
    sector = scrapy.Field()
    
