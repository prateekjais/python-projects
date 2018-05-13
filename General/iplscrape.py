# -*- coding: utf-8 -*-
import scrapy


class IplscrapeSpider(scrapy.Spider):
    name = 'iplscrape'
    allowed_domains = ['iplt20.com']
    start_urls = ['http://iplt20.com/']

    def parse(self, response):
        pass
