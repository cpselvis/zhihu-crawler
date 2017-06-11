#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
zhihu_crawler.html_parser
~~~~~~~~~~~~~~~~

Parse html content with xpath.
"""

class HtmlParser:

    def parse_xpath_source(self, source, index, is_int):
        if source and index < len(source):
            return source[index]
        else:
            if is_int:
                return "0"
            else:
                return ""

    def get_avatar(self, tree):
        return

    def get_username(self, tree):
        username_xpath = "//span[@class='ProfileHeader-name']/text()"
        return self.parse_xpath_source(tree.xpath(username_xpath), 0, False)

    def get_brief_info(self, tree):
        brief_info_xpath = "//span[@class='RichText ProfileHeader-headline']/text()"
        return self.parse_xpath_source(tree.xpath(brief_info_xpath), 0, False)

    def get_industry(self, tree):
        industry_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
        return self.parse_xpath_source(tree.xpath(industry_xpath), 0, False)

    def get_profession(self, tree):
        profession_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
        return self.parse_xpath_source(tree.xpath(profession_xpath), 1, False)

    def get_education(self, tree):
        education_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
        return self.parse_xpath_source(tree.xpath(education_xpath), 0, False)

    def get_major(self, tree):
        major_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
        return self.parse_xpath_source(tree.xpath(major_xpath), 1, False)

    def get_answer_count(self, tree):
        answer_count_xpath = "//li[@class='Tabs-item' and @aria-controls='Profile-answers']/a/span[@class='Tabs-meta']/text()"
        return self.parse_xpath_source(tree.xpath(answer_count_xpath), 0, True)

    def get_article_count(self, tree):
        article_count_xpath = "//li[@class='Tabs-item' and @aria-controls='Profile-asks']/a/span[@class='Tabs-meta']/text()"
        return self.parse_xpath_source(tree.xpath(article_count_xpath), 0, True)

    def get_ask_question_count(self, tree):
        ask_question_count_xpath = "//li[@class='Tabs-item' and @aria-controls='Profile-asks']/a/span[@class='Tabs-meta']/text()"
        return self.parse_xpath_source(tree.xpath(ask_question_count_xpath), 0, True)

    def get_collection_count(self, tree):
        collection_count_xpath = "//a[@class='Profile-followStatus'][1]/div/div[@class='Profile-followStatusValue']/text()"
        return self.parse_xpath_source(tree.xpath(collection_count_xpath), 0, True)

    def get_follower_count(self, tree):
        follower_count_xpath = "//a[@class='Profile-followStatus'][2]/div/div[@class='Profile-followStatusValue']/text()"
        return self.parse_xpath_source(tree.xpath(follower_count_xpath), 0, True)

    def get_followed_count(self, tree):
        followed_count_xpath = "//a[@class='Profile-followStatus'][1]/div/div[@class='Profile-followStatusValue']/text()"
        return self.parse_xpath_source(tree.xpath(followed_count_xpath), 0, True)

    def get_follow_live_count(self, tree):
        follow_live_count_xpath = "//a[@class='Profile-lightItem'][1]/span[@class='Profile-lightItemValue']/text()"
        return self.parse_xpath_source(tree.xpath(follow_live_count_xpath), 0, True)

    def get_follow_topic_count(self, tree):
        follow_topic_count_xpath = "//a[@class='Profile-lightItem'][2]/span[@class='Profile-lightItemValue']/text()"
        return self.parse_xpath_source(tree.xpath(follow_topic_count_xpath), 0, True)

    def get_follow_column_count(self, tree):
        follow_column_count_xpath =  "//a[@class='Profile-lightItem'][3]/span[@class='Profile-lightItemValue']/text()"
        return self.parse_xpath_source(tree.xpath(follow_column_count_xpath), 0, True)

    def get_follow_question_count(self, tree):
        follow_question_count_xpath = "//a[@class='Profile-lightItem'][4]/span[@class='Profile-lightItemValue']/text()"
        return self.parse_xpath_source(tree.xpath(follow_question_count_xpath), 0, True)

    def get_follow_collection_count(self, tree):
        follow_collection_count_xpath = "//a[@class='Profile-lightItem'][5]/span[@class='Profile-lightItemValue']/text()"
        return self.parse_xpath_source(tree.xpath(follow_collection_count_xpath), 0, True)
