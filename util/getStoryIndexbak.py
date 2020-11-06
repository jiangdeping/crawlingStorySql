# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 13:04
import re
import requests,time
from config.setting import user_Agent
from util.log import logger as logging
from mysql.mySQL import MySQL
from config import setting
def get_index_url(indexnum,indexurl):
    db=MySQL()
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    flag = True
    while flag:
        try:
            user_agent = user_Agent()
            res = requests.get(indexurl,headers=user_agent)
            flag = False
            # res.request.headers  获取设置的user_agent
        except Exception as e:
            logging.error(e)
            continue
    max_index_reg = re.compile(r'<a id="pt_mulu">\d+/(\d+)</a>')
    max_index = max_index_reg.findall(res.text)[0]
    if indexnum==0:
        logging.info("---索引下载中，请等待---")
        for i in range(1, int(max_index)+1):
            if i == 1:
                page_url = "http://m.xsqishu.com/newbook/index.html"
            else:
                page_url = "http://m.xsqishu.com/newbook/index_" + str(i) + ".html"
            db.inertStoryPageIndex(i,page_url)
            msg="下载第"+str(i)+"页"
            logging.info(msg)
    elif indexnum==int(max_index):
        logging.info("----当前已是最新索引,无需更新----")
    else:
        logging.info("----索引更新中,请等待----")
        for i in range(indexnum+1, int(max_index)+1):
            page_url = "http://m.xsqishu.com/newbook/index_" + str(i) + ".html"
            db.inertStoryPageIndex(i,page_url)
            msg="更新第"+str(i)+"页"
            logging.info(msg)
def get_page_url():
    url=setting.url
    db=MySQL()
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
def get_story_urlsnew(url):
    db=MySQL()
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
    logging.info(stroy_urls)
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
        logging.info("-----------")
        logging.info(url)
        story_title_reg = re.compile(r'<h1 class="title">(.+)</h1>')
        title = story_title_reg.findall(res.text)[0]
        download_url = "http://m.xsqishu.com/book/" + url[0] + ".html"
        download_urls[num]=download_url
        if db.isExistStory(num):
            msg="小说"+title+"已入库"
            logging.info(msg)
        else:
            db.inertStoryUrl(num,title,download_url)
        # logging.info(download_url)
    return download_urls
# urls=db.getStoryIndex(10)

# starttime=time.time()
# for url in urls:
#     get_story_urlsnew(url)
# endtime=time.time()
# print('Cost {} seconds'.format(endtime-starttime))

# threads=[]
# starttime=time.time()
# for i in urls:
#     t=Thread(target=get_story_urlsnew,args=[i])
#     t.start()
#     threads.append(t)
# for i in threads:
#     t.join()
# endtime=time.time()
# print('Cost {} seconds'.format(endtime-starttime))