# -*- coding: utf-8 -*-
# Author:jiang
import re
import requests
from config.config import user_Agent
from util.log import logger as logging
def getStoryContentUrl(storyno,url):
    story={}
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    flag = True
    logging.info(url)
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
    storyurlreg = re.compile(r'<a href=(%s/\d+).html><li>'%(identical)) #获取小说章节
    storyUrls = storyurlreg.findall(res.text)
    story[storyno]=storyUrls
    return story

# getStoryContentUrl(url)
