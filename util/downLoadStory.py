# -*- coding: utf-8 -*-
# Author:jiang
import re
import requests, re,time
# from mysql.storyMysql import insertStory
from util.log import logger as logging
from config.config import user_Agent
from mysql.mySQL import MySQL
from threading import Thread
db=MySQL()
# from mysql.allStoryUrlMysql import getSrotyUrl
def downLoadStory(storyno,urls):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    stroy_text = {}
    for url in urls:
        logging.info(url)
        flag = True
        while flag:
            try:
                user_agent = user_Agent()
                res = s.get(url, headers=user_agent)
                flag = False
                # print(res.headers["User-Agent"])
                # logging.info(res.headers["User-Agent"])
            except Exception as e:
                logging.info("- - 连接失败,正在重连- ")
                logging.error(e)
                continue

        text_reg = re.compile(r'<div class="articlecon font-large"><p>(.+)<br/><br/></p></div>')
        result = text_reg.findall(res.text)
        new_result = result[0].replace("<br/>", "")
        new_result.lstrip("")
        new_result = re.sub(' +', '\n  ', new_result)
        db.insertStory(url,new_result,storyno)
    return stroy_text
# data=db.getAllStoryDownLoadUrl(82862)
# downLoadStory(82862,data)
# print(data)
# def downLoadStoryContent(storyno):
#     data=db.getAllStoryDownLoadUrl(storyno)
#     urls=data[1]
#     threads=[]
#     starttime=time.time()
#     for i in data:
#         t=Thread(target=downLoadStory,args=[i])
#         t.start()
#         threads.append(t)
#     for i in threads:
#         t.join()
#     endtime=time.time()
#     print('Cost {} seconds'.format(endtime-starttime))


