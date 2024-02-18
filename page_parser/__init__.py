import re

from .parsers import baidu_parser, kr36_parser
from .parsers.jandan_parser import JandanParser
from .parsers.qichacha_parser import QichachaParser
from .parsers.sogou_parser import SogouParser
from .parsers.xicidaili_parser import XicidailiParser
from .parsers.douban_parser import DoubanParser
from .parsers.lagou_parser import LagouParser
from .utils import request_util

parse_config = {
    '.*://www.baidu.com/?': baidu_parser.parse_index,
    '.*://movie.douban.com/?': baidu_parser.parse_index,
    '.*://36kr.com/p/.*': kr36_parser.parse_detail,
}


def get_parse_function(url):

    for parse_url, parse_function in parse_config.items():
        if re.match(parse_url, url):
            return parse_function


def parse(url, content=None):
    """
    解析函数
    :param url: 指定网页的url
    :param content: 网页内容 html格式
    :return: 解析后的数据
    """
    parse_function = get_parse_function(url)

    if not parse_function:
        raise Exception("not found parse function")

    if not content:
        content = request_util.request(url)

    return parse_function(content)
