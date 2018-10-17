# -*- coding: utf-8 -*-

# @Date    : 2018-10-15
# @Author  : Peng Shiyu

# page_parser 包使用示例

import requests
from page_parser.baidu_parser import BaiduParser

# 1、下载网页
url = "https://www.baidu.com/"
response = requests.get(url)
response.encoding = response.apparent_encoding

# 2、解析网页
parser = BaiduParser()
items = parser.parse_index(response.text)

# 3、输出数据
for item in items:
    print(item)

    # {'title': '百度一下，你就知道'}
