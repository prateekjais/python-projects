# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from GiveIndia.items import GiveindiaItem

class ScrapengoSpider(Spider):
    name = 'ScrapeNGO'
    allowed_domains = ['www.giveindia.org']
    start_urls = ['http://www.giveindia.org/certified-indian-ngos.aspx']

    def parse(self, response):
        ngolist = Selector(response).xpath('//table[@class="panel panel-default"]/tbody/tr')
        for ngo in ngolist : 
            item = GiveindiaItem()
            item['ngo_name'] = ngo.xpath('td/a/text()').extract()[0].strip()
            item['ngo_url'] = 'http://www.giveindia.org' + ngo.xpath('td/a/@href').extract()[0].strip()
            item['ngo_cause'] = 'Children'
            item['ngo_state'] = ngo.xpath('td[2]/text()').extract()[0].strip()
            item['ngo_city'] = ngo.xpath('td[3]/text()').extract()[0].strip()
            yield item
