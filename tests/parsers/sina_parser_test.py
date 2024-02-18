# -*- coding: utf-8 -*-
"""
@File    : sina_parser_test.py
@Date    : 2024-02-18
"""


import json
import unittest

from page_parser.parsers import sina_parser
from page_parser.utils import request_util


class SinaParserTest(unittest.TestCase):
    def test_parse_detail(self):
        url = "https://finance.sina.com.cn/roll/2024-02-17/doc-inaikkvc4492655.shtml"
        content = request_util.request(url)

        data = sina_parser.parse_detail(content)
        print(json.dumps(data, ensure_ascii=False, indent=2))

        # {'title': '百度一下，你就知道'}
