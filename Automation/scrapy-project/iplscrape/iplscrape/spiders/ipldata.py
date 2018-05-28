# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from iplscrape.items import IplscrapeItem

class IpldataSpider(Spider):
    name = 'ipldata'
    allowed_domains = ['cricbuzz.com']
    start_urls = ['http://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/matches']

    def parse(self, response):
        matchlist2 = Selector(response).xpath('//div[@class="cb-col-100 cb-col "]')
        for match in matchlist2 : 
            item = IplscrapeItem()
            item['match_date'] = match.xpath('div[@class="cb-col-25 cb-col pad10"]/span/text()').extract()[0].strip()
            item['match_name'] = match.xpath('div[@class="cb-col-75 cb-col"]/div[@class="cb-col-60 cb-col cb-srs-mtchs-tm"]/a[@class="text-hvr-underline"]/span/text()').extract()[0].strip()
            item['match_venue'] = match.xpath('div[@class="cb-col-75 cb-col"]/div[@class="cb-col-60 cb-col cb-srs-mtchs-tm"]/div[@class="text-gray"]/text()').extract()[0].strip()
            item['match_time'] = match.xpath('div[@class="cb-col-75 cb-col"]/div[@class="cb-col-40 cb-col cb-srs-mtchs-tm"]/div[@class="cb-font-12 text-gray"]/text()').extract()[0][14:]
            item['match_result'] = match.xpath('div[@class="cb-col-75 cb-col"]/div[@class="cb-col-60 cb-col cb-srs-mtchs-tm"]/a[@class="cb-text-link"]/text()').extract()[0].strip()
            yield item

