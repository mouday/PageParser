# -*- coding: utf-8 -*-

# @Date    : 2018-10-17
# @Author  : Peng Shiyu

from parsel import Selector


class JandanParser(object):
    """
    煎蛋网：http://jandan.net/
    """

    def parse_index(self, html):
        """
        解析主页：http://jandan.net/
        :param html: {str} 网页文本
        :return: {iterator} 抽取的内容
        """
        sel = Selector(html)
        posts = sel.css("#content .list-post")
        for post in posts:
            image = post.css(".thumbs_b img::attr(src)").extract_first("")
            if image == "":
                image = post.css(".thumbs_b img::attr(data-original)").extract_first("")

            title = post.css("h2 a::text").extract_first("")
            url = post.css("h2 a::attr(href)").extract_first("")
            author = post.css(".time_s a::text").extract_first("")
            tag = post.css(".time_s strong a::text").extract_first("")
            summary = "".join(post.css(".indexs::text").extract()).strip()

            if image.startswith("//"):
                image = "http:" + image

            item = {
                "title": title,
                "author": author,
                "tag": tag,
                "summary": summary,
                "image": image,
                "url": url
            }
            yield item


if __name__ == '__main__':
    import requests

    response = requests.get("http://jandan.net/")
    items = JandanParser().parse_index(response.text)
    for item in items:
        print(item)
