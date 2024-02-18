# -*- coding: utf-8 -*-
"""
@File    : request_util.py
@Date    : 2024-02-18
"""
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}


def request(url):
    response = requests.get(url=url, headers=HEADERS)
    response.encoding = response.apparent_encoding
    return response.text
