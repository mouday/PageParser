# -*- coding: utf-8 -*-
"""
@File    : sina_parser.py
@Date    : 2024-02-18
"""
from parsel import Selector

from page_parser.utils import time_util


def parse_detail(content):
    sel = Selector(content)

    title = sel.css('meta[property="og:title"]::attr(content)').extract_first()
    description = sel.css('meta[property="og:description"]::attr(content)').extract_first()
    url = sel.css('meta[property="og:url"]::attr(content)').extract_first()
    image_url = sel.css('meta[property="og:image"]::attr(content)').extract_first()
    publish_time = sel.css("#top_bar_wrap .date::text").extract_first()
    author = sel.css("#top_bar_wrap .source::text").extract_first()
    content = sel.css("#artibody").get()

    if image_url.startswith('//'):
        image_url = 'https:' + image_url

    publish_time = time_util.format_datetime(publish_time)

    item = {
        "url": url,
        "image_url": image_url,
        "title": title,
        "content": content,
        "description": description,
        "author": author,
        "publish_time": publish_time,
    }

    return item
