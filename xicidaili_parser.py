# -*- coding: utf-8 -*-

# @Date    : 2018-10-15
# @Author  : Peng Shiyu


from parsel import Selector


class XicidailiParser(object):
    """
    西刺代理：http://www.xicidaili.com/
    """
    def parse_index(self, html):
        """
        解析主页：http://www.xicidaili.com/
        """
        sel = Selector(html)
        trs = sel.css("#ip_list tr")
        for tr in trs:
            country = tr.xpath("./td[1]/img/@alt").extract_first("")
            ip = tr.xpath("./td[2]/text()").extract_first("")
            port = tr.xpath("./td[3]/text()").extract_first("")
            server_address = tr.xpath("./td[4]/text()").extract_first("")
            hide_type = tr.xpath("./td[5]/text()").extract_first("")
            scheme_type = tr.xpath("./td[6]/text()").extract_first("")
            live_time = tr.xpath("./td[7]/text()").extract_first("")
            verify_time = tr.xpath("./td[8]/text()").extract_first("")

            item = {
                "country": country,
                "ip": ip,
                "port": port,
                "server_address": server_address,
                "hide_type": hide_type,
                "scheme_type": scheme_type,
                "live_time": live_time,
                "verify_time": verify_time,
            }
            if country != "":
                yield item
            else:
                continue

    def parse_list(self, html):
        """
        解析代理列表页：
        1. 国内高匿代理: http://www.xicidaili.com/nn/
        2. 国内普通代理: http://www.xicidaili.com/nt/
        3. 国内HTTPS代理: http://www.xicidaili.com/wn/
        4. 国内HTTP代理: http://www.xicidaili.com/wt/
        """
        sel = Selector(html)
        trs = sel.css("#ip_list tr")
        for tr in trs:
            country = tr.xpath("./td[1]/img/@alt").extract_first("")
            ip = tr.xpath("./td[2]/text()").extract_first("")
            port = tr.xpath("./td[3]/text()").extract_first("")
            server_address = tr.xpath("./td[4]/a/text()").extract_first("")
            hide_type = tr.xpath("./td[5]/text()").extract_first("")
            scheme_type = tr.xpath("./td[6]/text()").extract_first("")
            speed = tr.xpath("./td[7]/div/@title").extract_first("")
            connect_time = tr.xpath("./td[8]/div/@title").extract_first("")
            live_time = tr.xpath("./td[9]/text()").extract_first("")
            verify_time = tr.xpath("./td[10]/text()").extract_first("")

            item = {
                "country": country,
                "ip": ip,
                "port": port,
                "server_address": server_address,
                "hide_type": hide_type,
                "speed": speed,
                "connect_time": connect_time,
                "scheme_type": scheme_type,
                "live_time": live_time,
                "verify_time": verify_time,
            }
            if country != "":
                yield item
            else:
                continue


if __name__ == '__main__':
    import requests

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    }

    # url="http://www.xicidaili.com/"  # 首页
    # url = "http://www.xicidaili.com/nn/"  # 国内高匿代理
    # url = "http://www.xicidaili.com/nt/" # 国内普通代理
    # url= "http://www.xicidaili.com/wn/"# 国内HTTPS代理
    url= "http://www.xicidaili.com/wt/" # 国内HTTP代理

    response = requests.get(url, headers=headers)

    items = XicidailiParser().parse_list(response.text)

    for item in items:
        print(item)
