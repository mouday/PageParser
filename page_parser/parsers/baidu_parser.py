# -*- coding: utf-8 -*-
"""
baidu_parser.py
@Date    : 2018-10-13
@Author  : Peng Shiyu
"""

from parsel import Selector


def parse_index(html):
    """
    解析百度网主页：https://www.baidu.com/
    :param html: {str} 网页文本
    :return: {iterator} 抽取的内容
    eg:
    {
        'title': '百度一下，你就知道'
    }
    """
    sel = Selector(html)
    title = sel.css("title::text").extract_first()
    item = {
        "title": title
    }

    return item
