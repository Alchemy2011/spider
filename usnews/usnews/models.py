# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    """连接数据库，需要设置当前工程的settings.py文件"""
    return create_engine(URL(**settings.DATABASE))


def create_news_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class University(DeclarativeBase):
    __tablename__ = "university"

    id = Column(Integer, primary_key=True)
    school = Column('school', String(200))
    undergrad = Column('undergrad', String(200))
    postgrad = Column('postgrad', String(200))
    teacher_student_ratio = Column('teacher_student_ratio', String(200))
    international_student_ratio = Column('international_student_ratio', String(200))
    school_address = Column('school_address', String(200))
    school_website = Column('school_website', String(255), nullable=True)
    # FIXME <精准语法还不会，需要加强>
