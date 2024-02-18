# PageParser

[![Build Status](https://travis-ci.org/mouday/PageParser.svg?branch=master)](https://travis-ci.org/mouday/PageParser)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/page-parser.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/page-parser.svg)
![PyPI](https://img.shields.io/pypi/v/page-parser.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/mouday/PageParser.svg)
![PyPI - Format](https://img.shields.io/pypi/format/page-parser.svg)

## 项目简介

项目名称：六行代码写爬虫

英文名称：PageParser

项目简介：一个爬虫使用的网页解析包，实现最大限度的代码复用

项目目标：不懂网页解析也能写爬虫


## 安装模块
```
pip install page-parser
```

最小项目示例：

```python
import requests
from page_parser import BaiduParser

# 1、下载网页
response = requests.get("https://www.baidu.com/")
html = response.content.decode("utf-8")

# 2、解析网页
items = BaiduParser.parse_index(html)

# 3、输出数据
for item in items: print(item)
# {'title': '百度一下，你就知道'}
```

## 支持网页

| 序号 |网站 | 网页名称 |网页地址 |
| - |- | - | - |
| 1 |百度 | 主页  | https://www.baidu.com/ |
| 2 |豆瓣 | 电影 正在热映 | https://movie.douban.com/ |
| 3 |拉勾 | 招聘职位列表页  | https://www.lagou.com/zhaopin/ |
| 4 |企查查 | 融资事件页  | https://www.qichacha.com/elib_financing |
| 5 |西刺代理 | 主页  |http://www.xicidaili.com/ |
| 6 |西刺代理 | 国内高匿代理 | http://www.xicidaili.com/nn/ |
| 7 |西刺代理 | 国内普通代理 |http://www.xicidaili.com/nt/ |
| 8 |西刺代理 | 国内HTTPS代理 |http://www.xicidaili.com/wn/ |
| 9 |西刺代理 | 国内HTTP代理 | http://www.xicidaili.com/wt/ |
| 10 |搜狗搜索 | 微信公众号搜索页  | https://weixin.sogou.com/weixin?type=1&query=百度 |
| 11 | 煎蛋网 | 主页列表 | http://jandan.net/|
|12| 伯乐在线 | python栏目 | http://python.jobbole.com/|

## 使用示例
```python
# -*- coding: utf-8 -*-

import requests
from page_parser import BaiduParser

# 1、下载网页
url = "https://www.baidu.com/"
response = requests.get(url)
response.encoding = response.apparent_encoding

# 2、解析网页
items = BaiduParser.parse_index(response.text)

# 3、输出数据
for item in items:
    print(item)

# {'title': '百度一下，你就知道'}

```

## 网络爬虫工作流程：

```
页面下载器 -> 页面解析器 -> 数据存储

```

`页面下载器`: 主要涉及防爬攻破，方法各异，爬虫的难点也在此

`页面解析器`: 一般页面在一段时间内是固定的，每个人下载页面后都需要解析出页面内容，属于重复工作

`数据存储`: 不管是存储到什么文件或数据库，主要看业务需求

此项目就是将这项工作抽离出来，让网络爬虫程序重点关注于：网页下载，而不是重复的网页解析

## 项目说明

此项目可以和python 的requests 和scrapy 配合使用

当然如果要和其他编程语言使用，可以使用flask等网络框架再次对此项目进行封装，提供网络接口即可

发起人：mouday

发起时间：2018-10-13

需要更多的人一起来维护

## 贡献代码

贡献的代码统一放入文件夹：page_parser

代码示例，如没有更好的理由，应该按照下面的格式，便于使用者调用

baidu_parser.py

```python

# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu

from parsel import Selector


class BaiduParser(object):
    """
    百度网：https://www.baidu.com/
    """

    @staticmethod
    def parse_index(html):
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
    items = BaiduParser.parse_index(response.text)
    for item in items:
        print(item)

    # {'title': '百度一下，你就知道'}

```
## 说明：

### 原则：

1. 按照网站分类建立解析类

2. 解析方法包含在解析类中 为方便调用需要静态方法

3. 因为网页解析有时效性，所以必须`注明日期`


### 命名规则：
例如:
```
文件名：baidu_parser
类名：BaiduParser
方法名：parse_index
```

### 其他

1. 必要的代码注释

2. 必要的测试代码

3. 其他必要的代码


## 加入我们
### 基本要求
1. python的基本语法 + 面向对象 + 迭代器（yield）
2. 掌握的库：requests、parsel、scrapy（了解即可）
3. 解析库统一使用parsel（基于xpath），简单高效，与scrapy无缝衔接
4. 不太懂也没关系，自己看参考文章，只要愿意学就会，瞬间提升自己

参考文章：

1. [Python编程：class类面向对象](https://blog.csdn.net/mouday/article/details/79002712)

2. [Python编程：生成器yield与yield from区别简单理解](https://blog.csdn.net/mouday/article/details/80760973)

3. [Python爬虫：requests库基本使用](https://blog.csdn.net/mouday/article/details/80087627)

4. [Python网络爬虫之scrapy框架](https://blog.csdn.net/mouday/article/details/79736108)

5. [Python爬虫：xpath常用方法示例](https://blog.csdn.net/mouday/article/details/80364436)

6. [python爬虫：scrapy框架xpath和css选择器语法](https://blog.csdn.net/mouday/article/details/80455560)

### 联系方式

PageParser QQ群号: 932301512

![](images/page-parser-min.jpeg)
