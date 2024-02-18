# -*- coding: utf-8 -*-
"""
baidu_parser.py
@Date    : 2018-10-13
@Author  : Peng Shiyu
"""

import unittest

import requests

from page_parser.parsers import baidu_parser
from page_parser.utils import request_util


class BaiduParserTest(unittest.TestCase):
    def test_parse_index(self):
        content = request_util.request("https://www.baidu.com/")

        items = baidu_parser.parse_index(content)
        for item in items:
            print(item)

            # {'title': '百度一下，你就知道'}
