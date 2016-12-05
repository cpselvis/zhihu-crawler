# -*- coding: utf-8 -*-

"""
zhihu_crawler.crawler
~~~~~~~~~~~~~~~~

A zhihu user information crawler, which will collect some useful message including username, education,
profession, follower and folling count.  

"""

import requests
from lxml import html
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


SEED_URL = "https://www.zhihu.com/people/gaoming623/answers"

## Global variable
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.3"
ZHIHU_REFERER = "https://www.zhihu.com/"
HTTP_STATUS_CODE_200 = 200

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

        self.send_request(seed_url)

    def send_request(self, url):
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
        username = self.get_username(tree)
        brief_info = self.get_brief_info(tree)
        industry = self.get_industry(tree)
        profession = self.get_profession(tree)
        education = self.get_education(tree)
        major = self.get_major(tree)
        answer_count = self.get_answer_count(tree)
        article_count = self.get_article_count(tree)
        ask_question_count = self.get_question_count(tree)
        collection_count = self.get_collection_count(tree)
        follower_count = self.get_follower_count(tree)
        followed_count = self.get_followed_count(tree)
        return

    def get_avatar(self, tree):
        return
        
    def get_username(self, tree):
        username_xpath = "//span[@class='ProfileHeader-name']/text()"
        return tree.xpath(username_xpath)[0]

    def get_brief_info(self, tree):
        brief_info_xpath = "//span[@class='RichText ProfileHeader-headline']/text()"
        return tree.xpath(brief_info_xpath)[0]

    def get_industry(self, tree):
        industry_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
        return tree.xpath(industry_xpath)[0]
    
    def get_profession(self, tree):
        profession_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
        return tree.xpath(profession_xpath)[1]


    def get_education(self, tree):
        education_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
        return tree.xpath(education_xpath)[0]

    def get_major(self, tree):
        major_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
        return tree.xpath(major_xpath)[1]

    def get_answer_count(self, tree):
        answer_count_xpath = "//li[@class='Tabs-item' and @aria-controls='Profile-answers']/a/span[@class='Tabs-meta']/text()"
        return tree.xpath(answer_count_xpath)[0]

    def get_article_count(self, tree):
        article_count_xpath = "//li[@class='Tabs-item' and @aria-controls='Profile-asks']/a/span[@class='Tabs-meta']/text()"
        return tree.xpath(article_count_xpath)[0]

    def get_ask_question_count(self, tree):
        ask_question_count_xpath = "//li[@class='Tabs-item' and @aria-controls='Profile-asks']/a/span[@class='Tabs-meta']/text()"
        return tree.xpath(ask_question_count_xpath)[0]

    def get_collection_count(self, tree):
        collection_count_xpath = "//a[@class='Profile-followStatus'][1]/div/div[@class='Profile-followStatusValue']/text()"
        return tree.xpath(collection_count_xpath)[0]

    def get_follower_count(self, tree):
        follower_count_xpath = "//a[@class='Profile-followStatus'][2]/div/div[@class='Profile-followStatusValue']/text()"
        return tree.xpath(follower_count_xpath)[0]

    def get_followed_count(self, tree):
        followed_count_xpath = "//a[@class='Profile-followStatus'][1]/div/div[@class='Profile-followStatusValue']/text()"
        return tree.xpath(followed_count_xpath)[0]
        
# Cases here

if __name__ == "__main__":
    crawler = Crawler(SEED_URL)
