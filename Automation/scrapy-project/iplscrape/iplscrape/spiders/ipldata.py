# -*- coding: utf-8 -*-
import scrapy


class IpldataSpider(scrapy.Spider):
    name = 'ipldata'
    allowed_domains = ['cricbuzz.com']
    start_urls = ['http://cricbuzz.com/']

    def parse(self, response):
        pass
