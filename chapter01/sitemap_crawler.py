# -*- coding: utf-8 -*-

import re
from common import download


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...


if __name__ == '__main__':
    crawl_sitemap('http://127.0.0.1:8000/places/static/sitemap.xml')
