PageParser
==========

|Build Status|

安装模块
--------

::

    pip install page-parser

使用示例
--------

.. code:: python

    # -*- coding: utf-8 -*-

    import requests
    from page_parser.baidu_parser import BaiduParser

    # 1、下载网页
    url = "https://www.baidu.com/"
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    # 2、解析网页
    parser = BaiduParser()
    items = parser.parse_index(response.text)

    # 3、输出数据
    for item in items:
        print(item)

    # {'title': '百度一下，你就知道'}

网络爬虫工作流程：
------------------

::

    页面下载器 -> 页面解析器 -> 数据存储

``页面下载器``: 主要涉及防爬攻破，方法各异，爬虫的难点也在此

``页面解析器``:
一般页面在一段时间内是固定的，每个人下载页面后都需要解析出页面内容，属于重复工作

``数据存储``: 不管是存储到什么文件或数据库，主要看业务需求

此项目就是将这项工作抽离出来，让网络爬虫程序重点关注于：网页下载，而不是重复的网页解析

项目说明
--------

此项目可以和python 的requests 和scrapy 配合使用

当然如果要和其他编程语言使用，可以使用flask等网络框架再次对此项目进行封装，提供网络接口即可

发起人：mouday

发起时间：2018-10-13

需要更多的人一起来维护

代码示例
--------

贡献代码，如没有更好的理由，应该按照下面的格式，便于使用者调用

baidu\_parser.py

.. code:: python


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
            2018-10-13 pengshiyuyx@gmai.com
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

说明：
------

原则：
~~~~~~

1. 按照网站分类建立解析类

2. 解析方法包含在解析类中

3. 因为网页解析有时效性，所以必须\ ``注明日期``

命名规则：
~~~~~~~~~~

例如:

::

    文件名：baidu_parser
    类名：BaiduParser
    方法名：parse_index

其他
~~~~

1. 必要的代码注释

2. 必要的测试代码

3. 其他必要的代码

加入我们
--------

PageParser QQ群号: 932301512

.. figure:: source/page-parser-min.jpeg
   :alt: 

.. |Build Status| image:: https://travis-ci.org/mouday/PageParser.svg?branch=master
   :target: https://travis-ci.org/mouday/PageParser
