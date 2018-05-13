# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from csrbox.items import CsrboxItem


class CsrboxSpider(Spider):
    name = 'Csrbox'
    # allowed_domains = ['csrbox.org']
    start_urls = ['file:///C:/Users/Amit/Downloads/Companies_List.html']

    def parse(self, response):
        companylist = Selector(response).xpath('//div[@class = "col-md-12 forheight"]')
        for company in companylist : 
            item = CsrboxItem()
            item ['company_name'] = company.xpath('div/div[@class = "col-md-8 textmnore"]/div[@class = "col-md-9"]/a/h2[@class = "listingContentHeading"]/text()').extract()[0].strip()
            item ['location'] = company.xpath('div/div[@class = "col-md-8 textmnore"]/div[@class = "listingContentSubheading"]/text()').extract()[0].strip()
            # item ['csr_foundation_status'] = companydata.xpath('').extract()[0].strip()
            item ['sector'] = company.xpath('div/div[@class = "col-md-4"]/span[not(contains(@style, "font"))]/text()').extract()[0].strip()
            yield item
