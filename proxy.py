#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
zhihu_crawler.proxy
~~~~~~~~~~~~~~~~

Set proxy ip due to crawler against reptiles.
Free proxy api interface: http://api.xicidaili.com/free2016.txt, it will change per 15minutes.
"""

import requests
import random

class Proxy:

    def __init__(self):
        self.cache_ip_list = []

    # Get random ip from free proxy api url.
    def get_random_ip(self):
        if not len(self.cache_ip_list):
            api_url = 'http://api.xicidaili.com/free2016.txt'
            try:
                r = requests.get(api_url)
                ip_list = r.text.split('\r\n')
                self.cache_ip_list = ip_list
            except Exception as e:
                # Return null list when caught exception.
                # In this case, crawler will not use proxy ip.
                print e
                return {}

        proxy_ip = random.choice(self.cache_ip_list)
        proxies = {'http': 'http://' + proxy_ip}
        return proxies
