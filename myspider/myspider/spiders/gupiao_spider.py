# -*- coding: utf-8 -*-
# __author__ = 'liqirong'

import scrapy
import time

class GupiaoSpider(scrapy.Spider):
    name = "gupiao"

    start_urls = {
        'http://stock.10jqka.com.cn',
    }
    gp_name = ""


    def parse(self, response):
        # print(response.text)
        a_list = response.xpath(r'//*[@id="rzrq"]//tr/td[2]/a')
        for a in a_list:
            link = a.xpath("./@href").extract()[0]
            self.gp_name = a.xpath("./text()").extract()[0]
            print(link)
            print(self.gp_name)

            yield scrapy.Request(link, callback=self.download_data,
                                 meta={'gp_name': self.gp_name,
                                       'index': 2})
            # meta传参是个知识点。

    def download_data(self, response):
        table = []
        row = []
        # index = 2  不能在这里定义，没吃都是一个自循环

        print(response.url)
        time.sleep(1)
        tr_list = response.xpath('//*[@id="J-ajax-main"]//tr/')
        for tr in tr_list:
            td_list = tr.xpath('./td/text()').extract()
            for td in td_list:
                # print(td)
                row.append(td.strip())
            table.append(row)
            row = []  # 置空行是关键
        # print(table)
        print(response.meta['gp_name'])

        # 结束方式
        if response.meta['index'] > 5:
            return
        # 自循环
        url_str = r'http://data.10jqka.com.cn/market/rzrqgg/code/518880/order/desc/page/' \
                  + str(response.meta['index']) + '/ajax/1/'
        print(url_str)
        time.sleep(3)
        yield scrapy.Request(url_str, callback=self.download_data,
                             meta={'index': response.meta['index']+1,
                                   'gp_name': self.gp_name})
