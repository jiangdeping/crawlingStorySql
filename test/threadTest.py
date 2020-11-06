# # -*- coding: utf-8 -*-
# #Author:jiang
# #2020/11/2 11:14
# #提交任务的两种方式：
# #同步调用：执行完任务后，就原地等待，等到任务执行完毕，拿到返回值，才能继续下一行代码，导致程序串行执行。
# #异步调用+回调机制：执行完任务后，不再原地等待，任务一旦执行完毕就会触发回调函数，程序是并发执行的。
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread
# import requests,time
# def get(url):
#     print("%s GET %s"%(current_thread().getName(),url))
#     response = requests.get(url)
#     time.sleep(2)
#     if response.status_code==200:
#         return {"url":url,"content":response.text}
# def parse(res):
#     res = res.result()
#     print("parse:[%s] res:[%s]"%(res["url"],len(res["content"])))
#
# if __name__=="__main__":
#     starttime=time.time()
#     pool = ThreadPoolExecutor(5)     #线程池开两个线程，用于执行任务
#     urls = [
#         "https://www.baidu.com",
#         "http://www.sina.com.cn",
#         "http://www.163.com",
#         "https://www.cnblogs.com",
#         "https://www.cnblogs.com",
#         "https://www.cnblogs.com",
#         "https://www.cnblogs.com",
#         "https://www.cnblogs.com",
#         "https://www.cnblogs.com"
#     ]
#     for url in urls:
#         pool.submit(get,url).add_done_callback(parse)   #回调函数将前一个函数执行结果作为输入参数
#     pool.shutdown(wait=True)
#     endtime=time.time()
#     print('Cost {} seconds'.format(endtime-starttime))
import re, requests,time
from queue import Queue
from util.log import logger as logging
from config.setting import user_Agent
from startCrawLingStory import startCrawLingStory, downLoadStory
from threading import  Thread
from mysql.mySQL import MySQL
from mysql.connectMysql import insertStory,connect
from config.mysql import MySql
db=MySQL()
# stroy_queue = Queue()
# def downLoadStorys(no,url):
#     requests.adapters.DEFAULT_RETRIES = 5
#     s = requests.session()
#     s.keep_alive = False
#     stroy_text = {}
#     logging.info(url)
#     flag = True
#     while flag:
#         try:
#             user_agent = user_Agent()
#             res = s.get(url, headers=user_agent)
#             flag = False
#             # print(res.headers["User-Agent"])
#             # log.info(res.headers["User-Agent"])
#         except Exception as e:
#             logging.info("- - 连接失败,正在重连- ")
#             logging.error(e)
#             continue
#     text_reg = re.compile(r'<div class="articlecon font-large"><p>(.+)<br/><br/></p></div>')
#     result = text_reg.findall(res.text)
#     new_result = result[0].replace("<br/>", "")
#     new_result.lstrip("")
#     new_result = re.sub(' +', '\n  ', new_result)
#     insertStory(url,new_result,no)
#     return new_result
# urls = db.getStoryDownLoadUrl(82919)
# threads=[]
# starttime=time.time()
# for i in urls:
#     t=Thread(target=downLoadStorys,args=[82919,i])
#     t.start()
#     threads.append(t)
# for i in threads:
#     t.join()
# endtime=time.time()
# print('Cost {} seconds'.format(endtime-starttime))
for id in range(1626, 1700):
    sql="SELECT * FROM STORY where id=%s"%id
    MySql.selectone(sql,id)
