# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 13:17
from mysql.connectMysql import con_db
from util.log import logger as logging
def inertStoryUrl(storyNo,storyTitle,storyUrl):
    db = con_db()
    cursor = db.cursor()
    sql= "INSERT INTO story_url(storyno,storytitle,storyurl) VALUES ('{}','{}','{}')".format(storyNo, storyTitle,storyUrl)
    cursor.execute(sql)
    db.commit()
    msg="小说"+storyTitle+"新增入库"
    logging.info(msg)
    db.close
def getSrotyUrl(num):
    db=con_db()
    cursor=db.cursor()
    sql="SELECT storyno,storyurl,storytitle FROM story_url LIMIT %s"%num
    cursor.execute(sql)
    result=cursor.fetchall()
    return result


