# -*- coding: utf-8 -*-
import scrapy
from scrapy import spider
from scrapy.selector import Selector
from ngobox.items import NgoboxItem

class NgoscrapeSpider(scrapy.Spider):
    name = 'ngoscrape'
    allowed_domains = ['csrbox.org']
    start_urls = ['https://csrbox.org/list-companies-india']

    def parse(self, response):
        companydata = Selector(response).xpath('//div[@class = "col-md-12 forheight"]')
        for data in companydata : 
            item = NgoboxItem()
            item ['company_name'] = companydata.xpath('div/div[@class = "col-md-8 textmnore"]/div[@class = "col-md-9"]/a/h2[@class = "listingContentHeading"]/text()').extract()[0].strip()
            item ['location'] = companydata.xpath('div/div[@class = "col-md-8 textmnore"]/div[@class = "listingContentSubheading"]/text()').extract()[0].strip()
            # item ['csr_foundation_status'] = companydata.xpath('').extract()[0].strip()
            item ['sector'] = companydata.xpath('div/div[@class = "col-md-4"]/span[not(contains(@style, "font"))]/text()').extract()[0].strip()
            yield item
