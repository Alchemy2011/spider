# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import scrapy

from ..items import UsnewsItem


class QianmuRedisSpider(scrapy.Spider):
    name = 'qianmu'
    allowed_domains = ['qianmu.org']
    start_urls = [r'http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D']

    def parse(self, response):
        for href in response.xpath('//div[@id="content"]//td[2]/a/@href').extract():
            try:
                yield scrapy.Request(href, callback=self.parse_info)
            except:
                href = 'http://www.qianmu.org/' + href
                yield scrapy.Request(href, callback=self.parse_info)

    def parse_info(self, response):
        item = UsnewsItem()
        detail = response.xpath('//*[@id="wikiContent"]')
        table_dict = {}
        info_table = detail.xpath('div[1]/table/tbody/tr')
        if info_table:
            item['school'] = detail.xpath('h1/text()').extract_first()
        for row in info_table:
            tr_key = row.xpath('td[1]/p//text()').extract_first()
            if tr_key is None:
                tr_key = row.xpath('td[1]//text()').extract_first()
            tr_value = row.xpath('td[2]/p//text()').extract_first()
            if tr_value is None:
                tr_value = row.xpath('td[2]//text()').extract_first()
            table_dict[tr_key] = tr_value
        item['undergrad'] = table_dict.get(u'本科生人数', '')
        item['postgrad'] = table_dict.get(u'研究生人数', '')
        item['teacher_student_ratio'] = table_dict.get(u'师生比', '')
        item['international_student_ratio'] = table_dict.get(u'国际学生比例', '')
        item['school_website'] = table_dict.get(u'网址', '')
        item['school_address'] = (table_dict.get(u'国家', '')
                                  + table_dict.get(u'州省', '')
                                  + table_dict.get(u'城市', ''))
        yield item
        # FIXME <逻辑有改善空间>
