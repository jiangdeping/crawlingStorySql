# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/29 17:03
from config import config
import configparser as cparser
import MySQLdb
import re
from util.log import logger as logging
from mysql.getMysqlConfig import ConfigParse
from util.handleChapterNum import handleChaprerNum
class MySQL(object):
    # def __init__(self):
    #     filpath = config.dbpath
    #     cf = cparser.ConfigParser()
    #     cf.read(filpath)
    #     self.host=cf.get("mysqlconf", "host")
    #     self.port=int(cf.get("mysqlconf", "port"))
    #     self.user=cf.get("mysqlconf", "user")
    #     self.password=cf.get("mysqlconf", "password")
    #     self.db=cf.get("mysqlconf", "db_name")
    #     self.charset="utf8"
    #     self.use_unicode=True
    #     self.conn=MySQLdb.connect(host=self.host,port=self.port,user=self.user,
    #                               passwd=self.password,db=self.db
    #                              ,charset=self.charset,use_unicode=self.use_unicode)
    def __init__(self):
        self.db_conf = ConfigParse.get_db_config()
        self.conn = MySQLdb.connect(
            host = self.db_conf["host"],
            port = int(self.db_conf["port"]),
            user = self.db_conf["user"],
            password = self.db_conf["password"],
            database = self.db_conf["db"],
            charset = "utf8",
            use_unicode=True
        )
        self.cur = self.conn.cursor()
    def close(self):
        self.conn.close()
        # self.cur.close()
    def getCursor(self):
        self.cursor=self.conn.cursor()
        return self.cursor
    def inertStoryUrl(self,storyNo,storyTitle,storyUrl):#插入下载小说的链接地址
        cursor = self.getCursor()
        sql= "INSERT INTO story_url(storyno,storytitle,storyurl) VALUES ('{}','{}','{}')".format(storyNo, storyTitle,storyUrl)
        cursor.execute(sql)
        self.conn.commit()
        msg="小说"+storyTitle+"新增入库"
        logging.info(msg)
        self.close
    def getSrotyUrl(self,num): #需要多少个故事
        # cursor=self.getCursor()
        sql="SELECT storyno,storyurl,storytitle FROM story_url LIMIT %s"%num
        self.cur.execute(sql)
        result=self.cur.fetchall()
        self.close()
        return result
    # def getSrotyUrl(self,num):#获取需要下载小说的链接地址,num为下载故事的个数
    #     cursor=self.getCursor()
    #     sql="SELECT storyno,storyurl,storytitle FROM story_url LIMIT %s"%(num)
    #     cursor.execute(sql)
    #     result=cursor.fetchall()
    #     return result
    def getAllChapterNum(self,storyno):#获取所有章节
        cursor=self.getCursor()
        chapternum=[]
        sql = "SELECT CHAPTER_NUM FROM STORY  WHERE STORY_NO=%s ORDER BY CHAPTER_NUM"%storyno
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            chapternum.append(i[0])
        return chapternum
    def getStorySumChapter_Num(self,storyno):#获取该小说所有章节之和
        cursor =self.getCursor()
        count_sql = "SELECT count(*) FROM STORY where story_no=%s"%(storyno)
        logging.info(count_sql)
        cursor.execute(count_sql)
        count = cursor.fetchall()[0][0]  # 多少条数据
        return count
        self.close()
    def getWithOutDownLoadChapternum(self,storyno):#获取该小说未下载的故事章节
        chapternum=[]
        cursor = self.getCursor()
        sql ="select chapter_num from story where story_no=%s and state=0 ORDER BY chapter_num"%(storyno)
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            chapternum.append(i[0])
        return chapternum
    def getStoryTitle(self,storyno): #根据小说ID获取小说标题
        cursor = self.getCursor()
        sql = "SELECT STORYTITLE FROM STORY_URL WHERE storyno=%s" % (storyno)
        cursor.execute(sql)
        stroytitle=cursor.fetchall()[0][0]
        return stroytitle
    def getStoryText(self,chapternums):#根据章节ID获虎丘需要再找的内容
        dict={}
        cursor = self.getCursor()
        for chapternum in chapternums:
            sql = "SELECT  chapter,text FROM STORY  WHERE CHAPTER_NUM=%s"%chapternum
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                dict[i[0]]=i[1]
        return dict
    def insertStory(self,url,text,storyno):
        storytitle=self.getStoryTitle(self,storyno)
        cursor =self.getCursor()
        logging.info(url)
        reg=re.compile(r'http://m.qishudu.com(.+).html')
        identical=reg.findall(url)  #同一小说相同的部分
        # logging.info(identical)
        chapter_reg = re.compile(r'%s/(\d+).html'%identical)
        chapter_num =str(chapter_reg.findall(url)[0])
        new_chapter_num=storyno+chapter_num.zfill(5)
        chapter = "第" + str(chapter_num) + "章"
        sql = "INSERT INTO story(chapter,url,text,chapter_num,story_no,state) VALUES ('{}','{}','{}','{}',{},{})".format(chapter, url, text,new_chapter_num,storyno,0)
        cursor.execute(sql)
        logging_text = "更新小说- -%s- -%s" %(storytitle,chapter)
        logging.info(logging_text)
        self.cursor.commit()
        self.close()
    def getDownLoadUrl(self,urls): #判断该URL是否下载，未下载加入需要下载的url地址
        downloadurl = []
        cursor = self.getCursorr()
        for url in urls:
            new_url="http://m.qishudu.com"+url+".html"
            sql = "SELECT * FROM STORY WHERE url='{}'".format(new_url)
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) == 0:
                downloadurl.append(url)
        self.close()
        return downloadurl

    def inertStoryUrl(self,storyNo,storyTitle,storyUrl): #插入小说的ID、名称、下载地址
        cursor = self.getCursor()
        sql= "INSERT INTO story_url(storyno,storytitle,storyurl) VALUES ('{}','{}','{}')".format(storyNo, storyTitle,storyUrl)
        cursor.execute(sql)
        self.conn.commit()
        msg="小说"+storyTitle+"新增入库"
        logging.info(msg)
        self.close()
    def getDownLoadChapternum(self,storyno):#获取需要下载的章节
        cursor = self.getCursor()
        allnums=self.getAllChapterNum(storyno)
        logging.info("allnums")
        logging.info(allnums)
        downloadchapternum=self.getWithOutDownLoadChapternum(storyno)
        count=len(allnums)
        maxchapternum=allnums[len(allnums)-1]
        withOutdownloadsql ="select count(*) from story where story_no=%s and state=0"%storyno
        cursor.execute(withOutdownloadsql)
        withOutdownloadCount = cursor.fetchall()[0][0] #统计未下载个数
        alreadydownloadCount=count-withOutdownloadCount#统计已下载个数
        logging.info("withOutdownloadCount")
        logging.info(withOutdownloadCount)
        maxchapternum_sql ="select state from story where chapter_num=%s"%maxchapternum
        logging.info("maxchapternum_sql")
        logging.info(maxchapternum_sql)
        cursor.execute(maxchapternum_sql)
        maxchapternum_state=cursor.fetchall()[0][0]
        logging.info("maxchapternum_state")
        logging.info(maxchapternum_state)
        downnums=[]
        if withOutdownloadCount==0:
            print(1111111)
            return downnums
        elif withOutdownloadCount<count and maxchapternum_state==1: #全部下载
            downnums=allnums
            print(222222)
            return downnums
        elif withOutdownloadCount==count: #全部下载
            print(33333333)
            downnums=allnums
            return downnums
        else:
            print(444444)
            return handleChaprerNum(downloadchapternum)
    def changeState(self,nums):
        cursor = self.getCursor()
        for i in nums:
            sql="update story set state=1 where chapter_num =(%s)"%i
            cursor.execute(sql)
        self.conn.commit()
        self.close()
sql=MySQL()
# print(sql.getStoryTitle("82785"))
print(sql.getDownLoadChapternum(82785))