# -*- coding: utf-8 -*-
# 这个模块不能用

from link_crawler import link_crawler
from mongo_cache import MongoCache
from alexa_cb import AlexaCallback
import time


def main():
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    cache.clear()
    link_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, user_agent='GoodCrawler', ignore_robots=True)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print '串行爬取耗费 ', (end - start)
