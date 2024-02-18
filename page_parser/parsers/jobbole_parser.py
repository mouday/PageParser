# -*- coding: utf-8 -*-

# @Date    : 2019-03-20
# @Author  : Peng Shiyu


import requests
from parsel import Selector


def parse_python(html):
    """
    伯乐在线  http://www.jobbole.com/
    python栏目页面所有文章连接 2019-03-20
    http://python.jobbole.com/
    """
    sel = Selector(text=html)
    articles = sel.css(".meta-title")

    lst = []
    for article in articles:
        href = article.css("::attr(href)").extract_first("")
        text = article.css("::text").extract_first("")

        item = {
            "title": text,
            "url": href,
        }

        lst.append(item)


if __name__ == '__main__':
    url = "http://python.jobbole.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }
    response = requests.get(url, headers)
