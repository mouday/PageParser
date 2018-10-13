# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu

from parsel import Selector


class LagouParser(object):
    """
    拉勾网：https://www.lagou.com
    """
    def parse_zhaopin(self, html):
        """
        解析招聘职位列表页: https://www.lagou.com/zhaopin/
        """
        sel = Selector(text=html)
        lis = sel.css("#s_position_list .item_con_list li")
        for li in lis:
            position_link = li.css(".position_link::attr(href)").extract_first("")
            position = li.css("h3::text").extract_first("")
            money = li.css(".money::text").extract_first("")
            company = li.css(".company_name a::text").extract_first("")
            logo = li.css(".com_logo img::attr(src)").extract_first("")
            position_tempt = li.css(".list_item_bot .li_b_r::text").extract_first("")
            key_words = "".join(li.css(".list_item_bot .li_b_l span::text").extract())
            position_require = "".join(li.css(".p_bot .li_b_l::text").extract()).strip()
            post_time = li.css(".format-time::text").extract_first("")
            industry = li.css(".industry::text").extract_first("").strip()

            item = {
                "position": position,
                "money": money,
                "company": company,
                "industry": industry,
                "logo": logo,
                "key_words": key_words,
                "position_link": position_link,
                "position_tempt": position_tempt,
                "position_require": position_require,
                "post_time": post_time
            }

            yield item


if __name__ == '__main__':
    # 直接获取不到网页，所以保存到本地
    html = open("source/lagou-zhaopin.html").read()
    items = LagouParser().parse_zhaopin(html)
    for item in items:
        print(item)
