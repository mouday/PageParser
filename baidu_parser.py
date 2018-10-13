# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu

from parsel import Selector


class BaiduParser(object):
    """
    百度网：https://www.baidu.com/
    """
    def parse_index(self, html):
        """
        解析主页：https://www.baidu.com/
        :param html: {str} 网页文本
        :return: {iterator} 抽取的内容
        """
        sel = Selector(html)
        title = sel.css("title::text").extract_first()
        item = {
            "title": title
        }
        yield item


if __name__ == '__main__':
    import requests
    response = requests.get("https://www.baidu.com/")
    response.encoding = response.apparent_encoding
    items = BaiduParser().parse_index(response.text)
    for item in items:
        print(item)

    # {'title': '百度一下，你就知道'}