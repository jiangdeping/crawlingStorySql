# -*- coding: utf-8 -*-
# Author:jiang
sotryContentNum=5  #配置下载故事的章节
import re
import requests
from config.config import user_Agent
from util.log import logger as logging
from mysql.mySQL import MySQL
db=MySQL()
def getStoryContentUrl(storyno,url):
    story={}
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
    for i in storyUrls[0:sotryContentNum]:
        reg=re.compile(r'%s/(\d+)'%(identical))
        chapter_num=reg.findall(i)[0]
        url="http://m.xsqishu.com"+i+".html"
        new_chapter_num=storyno+str(chapter_num.zfill(5))
        newstoryUrls.append(url)
        db.insetStoryContentUrl(storyno,new_chapter_num,url)
    return newstoryUrls

