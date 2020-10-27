# -*- coding: utf-8 -*-
# Author:jiang
import os
from fake_useragent import UserAgent

url = "http://m.qishudu.com/book/22/69708.html"
stroypath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "story\story.txt")
urlpath = os.path.join(os.path.dirname(os.getcwd()), "story\\url.txt")
dbpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config\\db_config.ini")
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_PATH, 'logging')


def user_Agent():
    ua = UserAgent()
    useragent = ua.chrome
    headers = {"User-Agent": useragent}
    return headers
