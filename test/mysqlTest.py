# -*- coding: utf-8 -*-
# Author:jiang
# 2020/11/3 10:06
import MySQLdb, re
from util.log import logger as logging
from config import setting
import configparser as cparser
import  time,queue
from threading import  Thread
def connect():  # 1111
    filpath = setting.dbpath
    cf = cparser.ConfigParser()
    cf.read(filpath)
    conn = MySQLdb.Connect(
        host=cf.get("mysqlconf", "host"),
        db=cf.get("mysqlconf", "db_name"),
        user=cf.get("mysqlconf", "user"),
        password=cf.get("mysqlconf", "password"),
        port=int(cf.get("mysqlconf", "port")),
        charset="utf8",
        use_unicode=True,
    )
    return conn

def getStorySumChapter_Num(id):  # 获取该小说所有章节之和
    db=connect()
    cur=db.cursor()
    sql = "SELECT * FROM STORY where id=%s" % (id)
    cur.execute(sql)
    count = cur.fetchall()
    print(id)
    db.close()
    return count
# start=time.time()
# for id in range(1626,1700):
#     getStorySumChapter_Num(id)
# print(time.time()-start)

start=time.time()
q=queue.Queue(maxsize=20)
for id in range(1626, 1700):
    t = Thread(target=getStorySumChapter_Num, args=[id])
    q.put(t)
    if q.qsize() == 15:
        # 用于记录线程，便于终止线程
        join_thread = []
        # 从对列取出线程并开始线程，直到队列为空
        while q.empty() != True:
            t = q.get()
            join_thread.append(t)
            t.start()
        # 终止上一次队满时里面的所有1线程
        for t in join_thread:
            t.join
print(time.time()-start)