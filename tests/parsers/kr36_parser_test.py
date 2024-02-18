# -*- coding: utf-8 -*-
"""
baidu_parser.py
@Date    : 2018-10-13
@Author  : Peng Shiyu
"""
import json
import unittest

import requests

from page_parser.parsers import baidu_parser, kr36_parser
from page_parser.utils import request_util


class kr36ParserTest(unittest.TestCase):
    def test_parse_detail(self):
        url = "https://36kr.com/p/2652091684060295"
        content = request_util.request(url)

        data = kr36_parser.parse_detail(content)
        print(json.dumps(data, ensure_ascii=False, indent=2))

        # {'title': '百度一下，你就知道'}
