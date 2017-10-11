# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from example.items import ExampleItem


class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow='/places/default/index/', deny='/places/default/user/'), follow=True),
        Rule(LinkExtractor(allow='/places/default/view/', deny='/places/default/user/'), callback='parse_item')
    )

    def parse_item(self, response):
        item = ExampleItem()
        item['name'] = response.css('tr#places_country__row td.w2p_fw::text').extract()
        item['population'] = response.css('tr#places_population__row td.w2p_fw::text').extract()
        return item
