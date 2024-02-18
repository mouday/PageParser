# -*- coding: utf-8 -*-
"""
@File    : time_util.py
@Date    : 2024-02-18
"""
import dateparser

# 日期时间标准格式化
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# 日期标准格式化
DATE_FORMAT = "%Y-%m-%d"

# 时间标准格式化
TIME_FORMAT = "%H:%M:%S"


def format_datetime(datetime_str):
    date_time = dateparser.parse(datetime_str)
    if date_time:
        return date_time.strftime(DATE_TIME_FORMAT)
