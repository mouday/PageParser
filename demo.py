# -*- coding: utf-8 -*-

# @Date    : 2018-10-15
# @Author  : Peng Shiyu

from baidu_parser import BaiduParser
import requests

# 1、网页下载
url = "https://www.baidu.com/"
response = requests.get(url)

# 2、网页解析
parser = BaiduParser()
items = parser.parse_index(response.text)

# 3、数据输出
for item in items:
    print(item)