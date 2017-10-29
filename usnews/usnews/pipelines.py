# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from .models import db_connect, create_news_table, University


class UsnewsPipeline(object):
    """利用管道保存数据到数据库"""
    def __init__(self):
        engine = db_connect()
        create_news_table(engine)
        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        pass

    def process_item(self, item, spider):
        a = University(school=item['school'].encode("utf-8"),
                       undergrad=item['undergrad'].encode('utf-8'),
                       postgrad=item['postgrad'].encode('utf-8'),
                       teacher_student_ratio=item['teacher_student_ratio'].encode('utf-8'),
                       international_student_ratio=item['international_student_ratio'].encode('utf-8'),
                       school_website=item['school_website'],
                       school_address=item['school_address'].encode('utf-8'),)
        session = self.Session()
        session.merge(a)
        # session.add(a)  # FIXME <数据重复写入数据库的问题并没有处理>
        session.flush()
        session.commit()
        return item

    def close_spider(self, spider):
        pass
