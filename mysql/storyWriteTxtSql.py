# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 17:01
from mysql.connectMysql import con_db
def getStoryNo():
    storyno=[]
    db = con_db()
    cursor = db.cursor()
    sql = "SELECT STORYNO FROM STORY_URL"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        storyno.append(i[0])
    return storyno
def getStoryChapterNum(storyno):
    chapternum=[]
    db = con_db()
    cursor = db.cursor()
    sql = "SELECT CHAPTER_NUM FROM STORY  WHERE STORY_NO=%s ORDER BY CHAPTER_NUM"%storyno
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        chapternum.append(i[0])
    return chapternum
def getStoryText(chapternums):
    dict={}
    db = con_db()
    cursor = db.cursor()
    for chapternum in chapternums:
        sql = "SELECT  chapter,text FROM STORY  WHERE CHAPTER_NUM=%s"%chapternum
        cursor.execute(sql)
        result = cursor.fetchall()
s=getStoryChapterNum(82785)
getStoryText(s)