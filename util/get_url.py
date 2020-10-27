# -*- coding: utf-8 -*-
# Author:jiang
import re
import requests
from config.config import user_Agent
from util.log import logger as logging


def get_url(url):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    flag = True
    while flag:
        try:
            user_agent = user_Agent()
            res = requests.get(url, headers=user_agent)
            flag = False
            # res.request.headers  获取设置的user_agent
        except Exception as e:
            logging.error(e)
            continue
    url_reg = re.compile(r'<a href=(/book/22/69708/\d+).html><li>')
    allUrl = url_reg.findall(res.text)
    return allUrl


url = "http://m.xsqishu.com/newbook/"


def get_page_url(url):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    flag = True
    while flag:
        try:
            user_agent = user_Agent()
            res = requests.get(url, headers=user_agent)
            flag = False
            # res.request.headers  获取设置的user_agent
        except Exception as e:
            logging.error(e)
            continue
    max_index_reg = re.compile(r'<a id="pt_mulu">\d+/(\d+)</a>')
    max_index = max_index_reg.findall(res.text)[0]
    page_urls = []
    for i in range(1, int(max_index)):
        if i == 1:
            page_url = "http://m.xsqishu.com/newbook/index.html"
        else:
            page_url = "http://m.xsqishu.com/newbook/index_" + str(i + 1) + ".html"
        page_urls.append(page_url)
    return page_urls


complete_urls = []


def get_story_urls(url):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    flag = True
    while flag:
        try:
            user_agent = user_Agent()
            res = requests.get(url, headers=user_agent)
            flag = False
            # res.request.headers  获取设置的user_agent
        except Exception as e:
            logging.error(e)
            continue
    url_reg = re.compile(r'<a href="/txt/(\d+).html">')
    allUrl = url_reg.findall(res.text)
    complete_urls = []
    for i in allUrl:
        compile_url = "http://m.xsqishu.com/txt/" + i + ".html"
        complete_urls.append(compile_url)
    return complete_urls
