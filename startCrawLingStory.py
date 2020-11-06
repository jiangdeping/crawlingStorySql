# -*- coding: utf-8 -*-
# Author:jiang
# 2020/11/2 10:01
from mysql.mySQL import MySQL
from util.log import logger as logging
from util.getStoryContentUrl import getStoryContentUrl
from util.downLoadStory import downLoadStory
import time
from config.setting import user_Agent
from threading import Thread
import re,requests
from concurrent.futures import ThreadPoolExecutor
db = MySQL()

def startCrawLingStory(storyno):
    storytitle = db.getStoryTitle(storyno)
    allDownloadUrl = db.getStoryDownLoadUrl(storyno)  # 获取所有小说的链接地址
    logging.info(allDownloadUrl)
    alreadyDownloadUrl = db.getAreadyStoryDownLoadUrl(storyno)  # 获取已下载小说的链接地址
    downLoadUrl=[]
    if len(allDownloadUrl) == 0:  # 如果该小说没有存入链接地址，重新获取
        msg = "没有- -<" + storytitle + ">- -的下载地址,重新获取"
        logging.info(msg)
        data = db.getSrotyDownUrl(storyno)  # downloadnum需要下载的个数
        # data数据类型  #i[0] storyno,i[1]下载地址，i[2]标题
        urls = getStoryContentUrl(data[0], data[1])
        if len(urls) == 0:
            msg = "小说- - -<" + storytitle + ">- - -暂未提供下载"
            logging.info(msg)
        else:
            downLoadUrl = urls
    elif len(allDownloadUrl) == len(alreadyDownloadUrl):
        msg = "小说- - -" + storytitle + "- - -未更新"
        logging.info(msg)
    else:
        downLoadUrl = (set(allDownloadUrl).difference(set(alreadyDownloadUrl)))

    # downLoadUrl[storyno]=newdownLoadUrl
    # print(downLoadUrl)
    return {"storyno":storyno,"downLoadUrl":downLoadUrl}
    # downLoadStory(storyno, newdownLoadUrl)

def downLoadStory(storyno,urls):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    stroy_text = {}
    for url in urls:
        # logging.info(url)
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
        logging.info(new_result)
        # db.insertStory(url,new_result,storyno)
    return stroy_text




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