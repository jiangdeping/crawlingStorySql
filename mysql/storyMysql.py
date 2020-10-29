# -*- coding: utf-8 -*-
# Author:jiang
# 2020/10/22 10:24
import os, re
from util.log import logger as logging
from mysql.connectMysql import con_db
# def selectId():
#     db = con_db()
#     real_sql = "select * from story "
#     cur_ids = db.cursor()
#     cur_ids.execute(real_sql)
#     ids = cur_ids.fetchall()
#     print(ids)
#     db.close()
#     return ids
# def inertUrl(chapters, urls):  # 写入下载的url
#     db = con_db()
#     cursor = db.cursor()
#     for i in range(7):
#         chapter_num = chapters[i]
#         url = urls[i]
#         chapter = "第" + str(chapter_num) + "章"
#         if judgeUrlExist(chapter_num):
#             sql = "INSERT INTO story_url(chapter,url,chapter_num) VALUES ('{}','{}',{})".format(chapter, url,chapter_num)
#             cursor.execute(sql)
#             db.commit()
#         logging.info("更新小说%s") % (chapter)
#     db.close()
# def judgeUrlExist(chapters):
#     db = con_db()
#     cursor = db.cursor()
#     sql = "SELECT * FROM STORY_URL WHERE chapter_num=%s" % (chapters)
#     print(sql)
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if len(result) > 0:
#         return False
#     else:
#         return True
# #     db.close()
# def getDownUrl():
#     db = con_db()
#     cursor = db.cursor()
#     sql = "SELECT URL FROM STORY_URL"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     urls = []
#     for i in range(len(result)):
#         urls.append(result[i][0])
#     return urls
#     db.close()
def insertStory(url,text,storyno):
    storytitle=getStoryTitle(storyno)
    db = con_db()
    cursor = db.cursor()
    logging.info(url)
    reg=re.compile(r'http://m.qishudu.com(.+).html')
    identical=reg.findall(url)  #同一小说相同的部分
    logging.info(identical)
    chapter_reg = re.compile(r'%s/(\d+).html'%identical)
    chapter_num =str(chapter_reg.findall(url)[0])
    new_chapter_num=storyno+chapter_num.zfill(5)
    logging.info(new_chapter_num)
    chapter = "第" + str(chapter_num) + "章"
    sql = "INSERT INTO story(chapter,url,text,chapter_num,story_no,state) VALUES ('{}','{}','{}','{}',{},{})".format(chapter, url, text,new_chapter_num,storyno,0)
    cursor.execute(sql)
    logging_text = "更新小说- -%s- -%s" %(storytitle,chapter)
    logging.info(logging_text)
    db.commit()
    db.close()
# def judgeStoryExist(chapters):
#     db=con_db()
#     cursor=db.cursor()
#     sql="SELECT * FROM STORY WHERE chapter_num=%s"%(chapters)
#     cursor.execute(sql)
#     result=cursor.fetchall()
#     if len(result)>0:
#         return False
#     else:
#         return True
#     db.close()
def getStoryNum(storyno):
    dict = {}
    db = con_db()
    cursor = db.cursor()
    count_sql = "SELECT count(*) FROM STORY where story_no=%s"%(storyno)
    cursor.execute(count_sql)
    count = cursor.fetchall()[0][0]  # 多少条数据
    max_sql = "select MAX(chapter_num) FROM STORY where story_no=%s"%(storyno)
    cursor.execute(max_sql)
    max = cursor.fetchall()[0][0]
    dict["max"] = max
    dict["count"] = count
    return dict
    db.close()
def getDownLoadUrl(urls):
    print(urls)
    downloadurl = []
    db = con_db()
    cursor = db.cursor()
    for url in urls:
        new_url="http://m.qishudu.com"+url+".html"
        sql = "SELECT * FROM STORY WHERE url='{}'".format(new_url)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            downloadurl.append(url)
    db.close()
    return downloadurl
def getAllStoryText():  # 全量下载
    logging.info("- - -全量下载- - -")
    dict = {}
    db = con_db()
    cursor = db.cursor()
    sql = "select chapter,text from story ORDER BY chapter_num"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        dict[i[0]] = i[1]
    return dict
def getStoryText(urls):  # 增量下载
    logging.info("- - -增量下载- - -")
    db = con_db()
    cursor = db.cursor()
    dict = {}
    for url in urls:
        new_url="http://m.qishudu.com"+url+".html"
        sql = "SELECT chapter,text FROM STORY WHERE url='{}'".format(new_url)
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            dict[i[0]] = i[1]
    db.close()
    return dict
def getStoryTitle(storyno):
    db = con_db()
    cursor = db.cursor()
    sql = "SELECT STORYTITLE FROM STORY_URL WHERE storyno=%s" % (storyno)
    cursor.execute(sql)
    stroytitle = cursor.fetchall()[0][0]
    return stroytitle
