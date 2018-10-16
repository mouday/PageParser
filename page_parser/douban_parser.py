# -*- coding: utf-8 -*-

# @Date    : 2018-10-16
# @Author  : Peng Shiyu

from parsel import Selector


class DoubanParser(object):
    """
    豆瓣网：https://www.douban.com/
    """

    def parse_movie(self, html):
        """
        豆瓣电影 正在热映：https://movie.douban.com/

        以下两个板块是接口不做解析
        最近热门电影：
            https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=50&page_start=0
        最近热门电视剧：
            https://movie.douban.com/j/search_subjects?type=tv&tag=热门&page_limit=50&page_start=0
        """

        sel = Selector(html)
        rows = sel.css("#screening li.ui-slide-item")
        for row in rows:
            title = row.xpath("./@data-title").extract_first("")
            release = row.xpath("./@data-release").extract_first("")
            rate = row.xpath("./@data-rate").extract_first("")
            star = row.xpath("./@data-star").extract_first("")
            duration = row.xpath("./@data-duration").extract_first("")
            region = row.xpath("./@data-region").extract_first("")
            director = row.xpath("./@data-director").extract_first("")
            actors = row.xpath("./@data-actors").extract_first("")
            image = row.css(".poster img::attr(src)").extract_first("")
            href = row.css(".poster a::attr(href)").extract_first("")

            item = {
                "title": title,
                "release": release,
                "rate": rate,
                "star": star,
                "duration": duration,
                "region": region,
                "director": director,
                "actors": actors,
                "image": image,
                "href": href,
            }
            yield item


if __name__ == '__main__':
    import requests

    response = requests.get("https://movie.douban.com/")
    items = DoubanParser().parse_movie(response.text)
    for item in items:
        print(item)
