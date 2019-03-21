# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu

from page_parser import BaiduParser
import requests


def test_parser():
    response = requests.get("https://www.baidu.com/")
    response.encoding = response.apparent_encoding
    items = BaiduParser.parse_index(response.text)
    for item in items:
        print(item)

    print("test ok")


if __name__ == '__main__':
    test_parser()
