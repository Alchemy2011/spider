# -*- coding: utf-8 -*-
# windows下不能用，linux上没试

import sys
from process_crawler import process_crawler
from mongo_cache import MongoCache
from alexa_cb import AlexaCallback
import time


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    cache.clear()
    process_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)


if __name__ == '__main__':
    # max_threads = int(sys.argv[1]
    start = time.time()
    max_threads = 4
    main(max_threads)
    end = time.time()
    print '多进程耗时',(end - start)
