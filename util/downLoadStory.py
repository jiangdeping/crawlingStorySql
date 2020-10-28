# -*- coding: utf-8 -*-
# Author:jiang
import re
import requests, re
from mysql.storyMysql import insertStory
from util.log import logger as logging
from config.config import user_Agent
from mysql.allStoryUrlMysql import getSrotyUrl
def downLoadStory(storyno,urls):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    stroy_text = {}
    for i in urls:
        url="http://m.qishudu.com" + i + ".html"
        flag = True
        while flag:
            try:
                user_agent = user_Agent()
                res = s.get(url, headers=user_agent)
                flag = False
                # print(res.headers["User-Agent"])
                # logging.info(res.headers["User-Agent"])
            except Exception as e:
                logging.error(e)
                continue
        text_reg = re.compile(r'<div class="articlecon font-large"><p>(.+)<br/><br/></p></div>')
        result = text_reg.findall(res.text)
        new_result = result[0].replace("<br/>", "")
        new_result.lstrip("")
        new_result = re.sub(' +', '\n  ', new_result)
        insertStory(url,new_result,storyno)
    return stroy_text
