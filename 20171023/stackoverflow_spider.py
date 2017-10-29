# -*- coding: utf-8 -*-

# 先利用xpath_helper和chrome浏览器对，将要进行爬取的网站进行分析。
# 明确需求，需要哪些信息。
# 起始网址，北京出租：
# http://bj.58.com/chuzu/?PGTID=0d100000-0000-1d9c-5dc1-7d4e83b9779c&ClickID=1
# http://bj.58.com/chuzu/pn70/?PGTID=0d3090a7-0000-130b-372a-b388b1ae0f19&ClickID=2
# pn后面就是页数，总共70页，第一页和后面的网址有区别。

# 58房屋整体信息，单间房的信息，有标题，无价格
# /html/body/div[3]/div[1]/div[5]/div[2]/ul/li[1]/div[2]

# 标题部分：
# /html/body/div[3]/div[1]/div[5]/div[2]/ul/li[1]/div[2]/h2/a
# 房间情况：
# /html/body/div[3]/div[1]/div[5]/div[2]/ul/li[1]/div[2]/p[1]
# 位置：还可以细分
# /html/body/div[3]/div[1]/div[5]/div[2]/ul/li[1]/div[2]/p[2]
# 经纪人信息：也可以细分
# /html/body/div[3]/div[1]/div[5]/div[2]/ul/li[1]/div[2]/div
# 租金：这是直接定位到去除单位后的金额
# /html/body/div[3]/div[1]/div[5]/div[2]/ul/li[1]/div[3]/div[2]/b


import scrapy


class TC58(scrapy.Spider):
    name = 'tc58'
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d100000-0000-1d9c-5dc1-7d4e83b9779c&ClickID=1']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
        # for href in response.xpath('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }