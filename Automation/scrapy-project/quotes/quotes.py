# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['espncricinfo.com']
    start_urls = ['http://www.espncricinfo.com/ci/content/series/1131611.html?template=fixtures']

    def parse(self, response):
        self.log('I just visited' + response.url)
        for qte in response.css('div.large-11.medium-11.small-20.columns'):
            item = {
                'match': qte.css('a::text').extract_first().strip(),
                'venue': qte.css('span.play_stadium::text').extract_first().strip(),
                'status': qte.css('span.live_match::text').extract_first().strip(),
            }
            yield item
        