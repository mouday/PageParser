import requests
from page_parser.baidu_parser import BaiduParser

# 1、下载网页
response = requests.get("https://www.baidu.com/")
html = response.content.decode("utf-8")

# 2、解析网页
items = BaiduParser().parse_index(html)

# 3、输出数据
for item in items: print(item)
# {'title': '百度一下，你就知道'}
