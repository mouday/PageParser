# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu


from parsel import Selector


class QichachaParser(object):
    """
    企查查：https://www.qichacha.com/
    """

    def parse_financing(self, html):
        """
        解析融资事件页：https://www.qichacha.com/elib_financing
        """
        sel = Selector(html)

        trs = sel.css(".ntable tr")
        for tr in trs[1:]:
            product_image = tr.xpath("./td[1]/img/@src").extract_first("").strip()
            product_name = tr.xpath("./td[2]/a/text()").extract_first("").strip()
            product_link = tr.xpath("./td[2]/a/@href").extract_first("").strip()
            company = tr.xpath("./td[3]/text()").extract_first("").strip()
            investor = tr.xpath("./td[4]/text()").extract_first("").strip()
            financing_stage = tr.xpath("./td[5]/text()").extract_first("").strip()
            financing_money = tr.xpath("./td[6]/text()").extract_first("").strip()
            financing_time = tr.xpath("./td[7]/text()").extract_first("").strip()

            item = {
                "product_image": product_image,
                "product_name": product_name,
                "product_link": product_link,
                "company": company,
                "investor": investor,
                "financing_stage": financing_stage,
                "financing_money": financing_money,
                "financing_time": financing_time,

            }

            yield item


if __name__ == '__main__':
    import requests
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    }
    response = requests.get("https://www.qichacha.com/elib_financing", headers=headers)
    response.encoding = response.apparent_encoding
    items = QichachaParser().parse_financing(response.text)
    for item in items:
        print(item)
