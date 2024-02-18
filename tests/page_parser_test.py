# -*- coding: utf-8 -*-
"""
@File    : page_parser_test.py
@Date    : 2024-02-18
"""
import json
import unittest

import page_parser


class PageParserTest(unittest.TestCase):
    def test_parse(self):
        urls = [
            'https://www.baidu.com/',
            'https://36kr.com/p/2652091684060295'
        ]

        for url in urls:
            print('url:', url)
            data = page_parser.parse(url)
            print(json.dumps(data, ensure_ascii=False, indent=2))
