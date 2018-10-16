# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu

from parsel import Selector


class SogouParser(object):
    """
    搜狗搜索：https://www.sogou.com/
    """

    def parse_weixin_name(self, html):
        """
        解析搜狗微信公众号搜索，搜到的微信信息结果
        https://weixin.sogou.com/weixin?type=1&query=百度
        """
        sel = Selector(text=html)
        lst = sel.css(".news-list2 li")
        for li in lst:
            img = li.css(".img-box img::attr(src)").extract_first("")
            if img.startswith("//"):
                img = "http:" + img
            title = li.css(".tit").xpath("string(.)").extract_first("").strip()
            name = li.css(".info label::text").extract_first("")
            name = name.replace("微信号：", "")
            introduce_title = li.xpath("./dl[1]/dt/text()").extract_first("")
            if "功能介绍" in introduce_title:
                introduce = li.xpath("./dl[1]/dd").xpath("string(.)").extract_first("")
            else:
                introduce = ""
            authentication_title = li.xpath("./dl[2]/dt").xpath("string(.)").extract_first("")
            if "认证" in authentication_title:
                authname = li.xpath("./dl[2]/dd/text()").extract_first("")
            else:
                authname = ""
            qrcode = "http://open.weixin.qq.com/qr/code?username=" + name

            item = dict()
            item["title"] = title
            item["name"] = name
            item["introduce"] = introduce
            item["authname"] = authname
            item["img"] = img
            item["qrcode"] = qrcode

            yield item


if __name__ == '__main__':
    import requests

    url = "https://weixin.sogou.com/weixin?type=1&query=百度"
    response = requests.get(url)
    items = SogouParser().parse_weixin_name(response.text)
    for item in items:
        print(item)
