#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
zhihu_crawler.crawler
~~~~~~~~~~~~~~~~

A zhihu user information crawler, which will collect some useful message including username, education,
profession, follower and folling count.

"""

import requests
import sys
import datetime
from Queue import Queue
from lxml import html
from mysql import MySQL
from html_parser import HtmlParser
from bloom_filter import BloomFilter
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# Use bloom filter to check if a url has beed visited.
bf = BloomFilter()


## Global variable
SEED_URL = "https://www.zhihu.com/people/gaoming623"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.3"
ZHIHU_REFERER = "https://www.zhihu.com/"
HTTP_STATUS_CODE_200 = 200

DATABASE_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "",
    "db": "zhihu_user",
    "charset": "utf8"
}


class Crawler():

    def __init__(self, seed_url):
        self.headers = {
            "User-Agent": USER_AGENT,
            "Referer": ZHIHU_REFERER
        }
        self.cookies = {
            "d_c0": "AECA7v-aPwqPTiIbemmIQ8abhJy7bdD2VgE=|1468847182",
            "login": "NzM5ZDc2M2JkYzYwNDZlOGJlYWQ1YmI4OTg5NDhmMTY=|1480901173|9c296f424b32f241d1471203244eaf30729420f0",
            "n_c": "1",
            "q_c1": "395b12e529e541cbb400e9718395e346|1479808003000|1468847182000",
            "l_cap_id": "NzI0MTQwZGY2NjQyNDQ1NThmYTY0MjJhYmU2NmExMGY=|1480901160|2e7a7faee3b3e8d0afb550e8e7b38d86c15a31bc",
            "d_c0": "AECA7v-aPwqPTiIbemmIQ8abhJy7bdD2VgE=|1468847182",
            "cap_id": "N2U1NmQwODQ1NjFiNGI2Yzg2YTE2NzJkOTU5N2E0NjI=|1480901160|fd59e2ed79faacc2be1010687d27dd559ec1552a"
        }
        # Url queue to store crawler task.
        self.url_queue = Queue()

    def start(self, seed_url):
        # Add seed url to a url queue
        self.url_queue.put(seed_url)
        # Add seed url to bloomfilter bit vector.
        bf.add(seed_url)

        # Begin task
        self.task_master()

    def task_master(self):
        # Never stop crawler task when there exist url in url task queue.
        while(True):
            if (self.url_queue.qsize() > 0):
                curr_url = self.url_queue.get()
                self.send_request(curr_url)
            else:
                break

    def send_request(self, url):
        url = url + "/following"
        # Send a request through requests library and get HTML source
        # file content
        try:
            r = requests.get(url, cookies = self.cookies, headers = self.headers)
        except:
            return
        html_source = r.text

        # If HTTP request return successfully, parse HTML source
        if r.status_code == HTTP_STATUS_CODE_200:
            self.html_parser(html_source)

    def html_parser(self, html_source):
        tree = html.fromstring(html_source)
        parser = HtmlParser()

        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print "*"*60
        print "用户名：%s\n" % parser.get_username(tree)
        print "个人简介：%s\n" % parser.get_brief_info(tree)
        print "所处行业：%s\n" % parser.get_industry(tree)
        print "毕业学校：%s\n" % parser.get_education(tree)
        print "主修专业：%s\n" % parser.get_major(tree)
        print "回答数：%s\n" % parser.get_answer_count(tree)
        print "文章数：%s\n" % parser.get_article_count(tree)
        print "提问数：%s\n" % parser.get_ask_question_count(tree)
        print "收藏数：%s\n" % parser.get_collection_count(tree)
        print "被关注数：%s\n" % parser.get_follower_count(tree)
        print "关注数：%s\n" % parser.get_followed_count(tree)
        print "关注直播数：%s\n" % parser.get_follow_live_count(tree)
        print "关注话题数：%s\n" % parser.get_follow_topic_count(tree)
        print "关注专栏数：%s\n" % parser.get_follow_column_count(tree)
        print "关注问题数：%s\n" % parser.get_follow_question_count(tree)
        print "关注收藏夹数：%s\n" % parser.get_follow_collection_count(tree)
        print "当前时间：%s\n" % current_time
        print "*"*60

        # Save data to mysql.
        db = MySQL(DATABASE_CONFIG)
        sql = "INSERT INTO t_user(username, brief_info, industry, education, major, answer_count, article_count, ask_question_count, collection_count, follower_count, followed_count, follow_live_count, follow_topic_count, follow_column_count, follow_question_count, follow_collection_count, gmt_create) values('" + username + "','" + brief_info + "','" + industry + "','" + education + "', '" + major + "', '" + answer_count+ "', '" + article_count + "', '" + ask_question_count + "', '" + collection_count + "', '" + follower_count + "', '" + followed_count + "', '" + follow_live_count + "', '" + follow_topic_count + "', '" + follow_column_count + "', '" + follow_question_count+ "', '" + follow_collection_count + "', '" + current_time + "')"
        db.insert(sql)

        # Extract urls
        self.extract_urls(tree)
        return

    def extract_urls(self, tree):
        followed_xpath = "//span[@class='UserLink UserItem-name']/div/div/a/@href"
        followed_user_list = tree.xpath(followed_xpath)

        # Iterate followed list and put new url to url task queue.
        for followed_user_item in followed_user_list:
            new_url = "https://www.zhihu.com" + followed_user_item
            # If url not visited before (check bloom filter)
            if not bf.contains(new_url):
                self.url_queue.put(new_url)
                bf.add(new_url)
            else:
                print "Bloom filter judge " + new_url + " visited, this record will be ignored."

# Cases here

if __name__ == "__main__":
    crawler = Crawler(SEED_URL)
    crawler.start(SEED_URL)
