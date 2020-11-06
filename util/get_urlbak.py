# -*- coding: utf-8 -*-
# Author:jiang
import re
import requests
from config.setting import user_Agent
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
def get_index_url(url):
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
            page_url = "http://m.xsqishu.com/newbook/index_" + str(i) + ".html"
        page_urls.append(page_url)
    return page_urls
def get_story_url(urls):
    stroy_urls = []
    download_urls = {}
    for url in urls:
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
        for i in allUrl:
            story_url = "http://m.xsqishu.com/txt/" + i + ".html"
            stroy_urls.append(story_url)
    for compileurl in stroy_urls:
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        flag = True
        while flag:
            try:
                user_agent = user_Agent()
                res = requests.get(compileurl, headers=user_agent)
                res.encoding = "gbk"
                flag = False
                # res.request.headers  获取设置的user_agent
            except Exception as e:
                logging.error(e)
                continue
        reg = re.compile(r'<a href="/book/(.+).html" class="bdbtn greenBtn">')
        url = reg.findall(res.text)
        story_title_reg = re.compile(r'<h1 class="title">(.+)</h1>')
        title = story_title_reg.findall(res.text)[0]
        download_url = "http://m.xsqishu.com/book/" + url[0] + ".html"
        download_urls[title] = download_url
        msg = title + ":" + download_url
        logging.info(msg)
    return download_urls

