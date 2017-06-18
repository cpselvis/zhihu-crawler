#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
zhihu_crawler.scheduler
~~~~~~~~~~~~~~~~

Entrance file, assign task to crawler.

"""

from crawler import Crawler
import sys
reload(sys)
sys.setdefaultencoding('utf8')

c = Crawler()

SEED_URL = "https://www.zhihu.com/people/gaoming623"

if __name__ == '__main__':
    c.start(SEED_URL)
