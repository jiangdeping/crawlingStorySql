# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 17:01
from mysql.connectMysql import con_db
from util.handleChapterNum import handleChaprerNum
def getStoryNo(): #已废弃
    storyno=[]
    db = con_db()
    cursor = db.cursor()
    sql = "SELECT STORYNO FROM STORY_URL"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        storyno.append(i[0])
    return storyno

def getStoryText(chapternums):#111111111111111
    dict={}
    db = con_db()
    cursor = db.cursor()
    for chapternum in chapternums:
        sql = "SELECT  chapter,text FROM STORY  WHERE CHAPTER_NUM=%s"%chapternum
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            dict[i[0]]=i[1]
    return dict

def getAllChapterNum(storyno):#获取所有章节111111111
    chapternum=[]
    db = con_db()
    cursor = db.cursor()
    sql = "SELECT CHAPTER_NUM FROM STORY  WHERE STORY_NO=%s ORDER BY CHAPTER_NUM"%storyno
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        chapternum.append(i[0])
    return chapternum
def getNoDownLoadChapternum(storyno):#获取未下载的故事章节1111111111
    chapternum=[]
    db = con_db()
    cursor = db.cursor()
    sql ="select chapter_num from story where story_no=%s and state=0 ORDER BY chapter_num"%(storyno)
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
        chapternum.append(i[0])
    return chapternum
def getDownLoadChapternum(storyno):#获取需要下载的章节1111111111
    db = con_db()
    cursor = db.cursor()
    allnums=getAllChapterNum(storyno)
    downloadchapternum=getNoDownLoadChapternum(storyno)
    count=len(allnums)
    maxchapternum=allnums[len(allnums)-1]
    notdownloadsql ="select count(*) from story where story_no=%s and state=0"%storyno
    cursor.execute(notdownloadsql)
    notdownloadsql = cursor.fetchall()[0][0] #统计未下载的个数
    maxchapternum_sql ="select state from story where chapter_num=%s"%maxchapternum
    cursor.execute(maxchapternum_sql)
    maxchapternum_state=cursor.fetchall()[0][0]
    if notdownloadsql<count and maxchapternum_state==1: #全部下载
        return allnums
    elif notdownloadsql==count: #全部下载
        return allnums
    else:
        return handleChaprerNum(downloadchapternum)
def changeState(nums):#11111111111
    db = con_db()
    cursor = db.cursor()
    for i in nums:
        sql="update story set state=1 where chapter_num =(%s)"%i
        cursor.execute(sql)
    db.commit()
    db.close()

print(getDownLoadChapternum(82785))