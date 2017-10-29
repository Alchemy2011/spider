# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UsnewsItem(scrapy.Item):
    school = scrapy.Field()
    undergrad = scrapy.Field()
    postgrad = scrapy.Field()
    teacher_student_ratio = scrapy.Field()
    international_student_ratio = scrapy.Field()
    school_website = scrapy.Field()
    school_address = scrapy.Field()
