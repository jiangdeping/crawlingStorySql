# -*- coding: utf-8 -*-
# Author:jiang
 #配置下载故事的章节
import re
import requests
from config.setting import user_Agent
from config import  setting
from util.log import logger as logging
from mysql.mySQL import MySQL
db=MySQL()

def get_story_urls(urls):
    downloadnum=setting.DOWNLOADNUM
    db=MySQL()
    stroy_urls = {}
    downloadstoryno=[]
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
        if downloadnum==False:
            downloadnum=len(allUrl)
        for i in allUrl[0:downloadnum]:
            story_url = "http://m.xsqishu.com/txt/" + i + ".html"
            stroy_urls[i]=story_url
            downloadstoryno.append(i)
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
        if db.isExistStory(num):
            msg="小说---"+title+"---已入库"
            logging.info(msg)
        else:
            db.inertStoryUrl(num,title,download_url)
    return downloadstoryno
# storynums=3
def getStoryContentUrl(storyno,url):
    storyContentNum=setting.STORYNUM
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    flag = True
    # logging.info(url)
    while flag:
        try:
            user_agent = user_Agent()
            res = requests.get(url, headers=user_agent)
            flag = False
            # res.request.headers  获取设置的user_agent
        except Exception as e:
            logging.error(e)
            continue
    reg=re.compile(r'http://m.xsqishu.com(.+).html')
    identical=reg.findall(url)[0]  #同一小说相同的部分
    storyurlreg = re.compile(r'<a href=(%s/\d+).html><li>'%(identical)) #获取小说url
    storyUrls = storyurlreg.findall(res.text)
    newstoryUrls=[]
    if storyContentNum==False:
        storyContentNum=len(storyUrls)
    for i in storyUrls[0:storyContentNum-1]:
        reg=re.compile(r'%s/(\d+)'%(identical))
        chapter_num=reg.findall(i)[0]
        url="http://m.xsqishu.com"+i+".html"
        new_chapter_num=storyno+str(chapter_num.zfill(5))
        newstoryUrls.append(url)
        print(storyno,new_chapter_num,url)
        db.insetStoryContentUrl(storyno,new_chapter_num,url)
    return newstoryUrls
def getStoryContentUrl(storyno,url):
    story={}
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    # log.info(url)
    while flag:
        try:
            user_agent = user_Agent()
            res = requests.get(url, headers=user_agent)
            flag = False
            # res.request.headers  获取设置的user_agent
        except Exception as e:
            logging.error(e)
            continue
    reg=re.compile(r'http://m.xsqishu.com(.+).html')
    identical=reg.findall(url)[0]  #同一小说相同的部分
    storyurlreg = re.compile(r'<a href=(%s/\d+).html><li>'%(identical)) #获取小说url
    storyUrls = storyurlreg.findall(res.text)
    newstoryUrls=[]
    for i in storyUrls[0:sotryContentNum]:
        reg=re.compile(r'%s/(\d+)'%(identical))
        chapter_num=reg.findall(i)[0]
        url="http://m.xsqishu.com"+i+".html"
        new_chapter_num=storyno+str(chapter_num.zfill(5))
        newstoryUrls.append(url)
        db.insetStoryContentUrl(storyno,new_chapter_num,url)
    return newstoryUrls

