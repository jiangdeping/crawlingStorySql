# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 13:04
import re
import requests,time
from config.config import user_Agent
from util.log import logger as logging
from mysql.mySQL import MySQL
from threading import Thread
db=MySQL()
from threading import Thread,Lock
import time
def get_page_url():
    url = "http://m.xsqishu.com/newbook/"
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
    logging.info(max_index)
    already_index_count=db.getStoryPageIndexCount()
    if already_index_count<int(max_index):
        for i in range(already_index_count+1, int(max_index)+1):
            if i == 1:
                page_url = "http://m.xsqishu.com/newbook/index.html"
            else:
                page_url = "http://m.xsqishu.com/newbook/index_" + str(i) + ".html"
            db.inertStoryPageIndex(i,page_url)
            msg="新增第"+str(i)+"页"
            logging.info(msg)
    else:
        logging.info("当前总页数未更新")
def get_story_urls(urls):
    stroy_urls = {}
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
            stroy_urls[i]=story_url
    for num,compileurl in stroy_urls.items():
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
        download_urls.setdefault(num,{title:download_url})
        # logging.info(num)
        if db.isExistStory(num):
            msg="小说"+title+"已入库"
            logging.info(msg)
        else:
            db.inertStoryUrl(num,title,download_url)
        # logging.info(download_url)
    return download_urls
# storynums=3
def get_story_urlsnew(url):
    stroy_urls = {}
    download_urls = {}
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
        stroy_urls[i]=story_url
    for num,compileurl in stroy_urls.items():
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
        download_urls.setdefault(num,{title:download_url})
        # logging.info(num)
        if db.isExistStory(num):
            msg="小说"+title+"已入库"
            logging.info(msg)
        else:
            db.inertStoryUrl(num,title,download_url)
        # logging.info(download_url)
    return download_urls
urls=db.getStoryIndex(10)

# starttime=time.time()
# for url in urls:
#     get_story_urlsnew(url)
# endtime=time.time()
# print('Cost {} seconds'.format(endtime-starttime))

threads=[]
starttime=time.time()
for i in urls:
    t=Thread(target=get_story_urlsnew,args=[i])
    t.start()
    threads.append(t)
for i in threads:
    t.join()
endtime=time.time()
print('Cost {} seconds'.format(endtime-starttime))