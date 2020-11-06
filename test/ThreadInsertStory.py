# # -*- coding: utf-8 -*-
# #Author:jiang
# #2020/11/2 11:14

import re, requests,time
from queue import Queue
from util.log import logger as logging
from config.setting import user_Agent
from startCrawLingStory import startCrawLingStory, downLoadStory
from threading import  Thread
from mysql.mySQL import MySQL
from mysql.connectMysql import insertStory,connect,select

db=MySQL()
def downLoadStorys(no,url):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    logging.info(url)
    flag = True
    while flag:
        try:
            user_agent = user_Agent()
            res = s.get(url, headers=user_agent)
            flag = False
            # print(res.headers["User-Agent"])
            # log.info(res.headers["User-Agent"])
        except Exception as e:
            logging.info("- - 连接失败,正在重连- ")
            logging.error(e)
            continue
    text_reg = re.compile(r'<div class="articlecon font-large"><p>(.+)<br/><br/></p></div>')
    result = text_reg.findall(res.text)
    new_result = result[0].replace("<br/>", "")
    new_result.lstrip("")
    new_result = re.sub(' +', '\n  ', new_result)
    insertStory(url,new_result,no)
    return new_result
urls = db.getStoryDownLoadUrl(82919)
threads=[]
# starttime=time.time()
# for i in urls:
#     t=Thread(target=downLoadStorys,args=[82919,i])
#     t.start()
#     threads.append(t)
# for i in threads:
#     t.join()
# endtime=time.time()
# print('Cost {} seconds'.format(endtime-starttime))
starttime=time.time()
for i in range(1626,2927):
    t=Thread(target=select,args=[i])
    t.start()
    threads.append(t)
for i in threads:
    t.join()
endtime=time.time()
print('Cost {} seconds'.format(endtime-starttime))