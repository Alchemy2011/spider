# -*- coding: utf-8 -*-
# 正则难构造、可读性差、适应变化能力差，该方法过于脆弱，容易在网页更新后出问题

import urllib2
import re


def scrape(html):
    area = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[0]
    return area


if __name__ == '__main__':
    html = urllib2.urlopen('http://127.0.0.1:8000/places/default/view/United-Kingdom-239').read()
    print scrape(html)
