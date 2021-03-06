# -*- coding: utf-8 -*-
# 问题：写入csv有空行

import json
import csv
import downloader


def main():
    writer = csv.writer(open('countries1.csv', 'wb'))
    D = downloader.Downloader()
    html = D('http://127.0.0.1:8000/places/ajax/search.json?page=0&page_size=1000&search_term=.')
    ajax = json.loads(html)
    for record in ajax['records']:
        writer.writerow([record['country']])


if __name__ == '__main__':
    main()
