# # -*- coding: utf-8 -*-
# #Author:jiang
# #2020/10/28 13:21
import MySQLdb, re
from util.log import logger as logging
from config import setting
import configparser as cparser

def connect():#1111
    filpath = setting.dbpath
    cf = cparser.ConfigParser()
    cf.read(filpath)
    conn= MySQLdb.Connect(
        host=cf.get("mysqlconf", "host"),
        db=cf.get("mysqlconf", "db_name"),
        user=cf.get("mysqlconf", "user"),
        password=cf.get("mysqlconf", "password"),
        port=int(cf.get("mysqlconf", "port")),
        charset="utf8",
        use_unicode=True,
    )
    return conn


def insertStory(url, text, storyno="82919"):
    db=connect()
    storytitle = "123"
    reg = re.compile(r'http://m.xsqishu.com(.+).html')
    identical = reg.findall(url)  # 同一小说相同的部分
    # log.info(identical)
    chapter_reg = re.compile(r'%s/(\d+).html' % identical)
    chapter_num = str(chapter_reg.findall(url)[0])
    new_chapter_num = str(storyno) + chapter_num.zfill(5)
    chapter = "第" + str(chapter_num) + "章"
    sql = "INSERT INTO story(chapter,url,text,chapter_num,story_no,state) VALUES ('{}','{}','{}','{}',{},{})".format(
        chapter, url, text, new_chapter_num, storyno, 0)
    cur=db.cursor()
    cur.execute(sql)
    logging_text = "更新小说- -%s- -%s" % (storytitle, chapter)
    logging.info(logging_text)
    db.commit()
def select(no):
    db=connect()
    sql="SELECT * FROM STORY where id=%s"%no
    print(sql)
    cur=db.cursor()
    cur.execute(sql)