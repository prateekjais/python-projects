# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsrboxItem(scrapy.Item):
    # define the fields for your item here like:
      company_name = scrapy.Field()
      location = scrapy.Field()
      csr_foundation_status = scrapy.Field()
      sector = scrapy.Field()
    
