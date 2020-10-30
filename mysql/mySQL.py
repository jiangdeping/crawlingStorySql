# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/29 17:03
from  datetime import datetime
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
        self.conn.commit()#提交事务
        self.cur.close()  #关闭游标
        self.conn.close() #关闭连接

    def inertStoryPageIndex(self,storyindexID,storyindexUrl):
        createtime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updatetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql= "INSERT INTO story_index(storyindexID,storyindexUrl,createtime,updatetime) VALUES ('{}','{}','{}','{}')".format(storyindexID,storyindexUrl, createtime,updatetime)
        self.cur.execute(sql)
        self.conn.commit()
    def getStoryPageIndexCount(self):
        sql="SELECT count(*) FROM STORY_INDEX"
        self.cur.execute(sql)
        count = self.cur.fetchall()[0][0]  # 多少条数据
        return count
    def getStoryIndex(self,num):#获取页面地址
        index=[]
        sql="SELECT storyindexurl FROM STORY_INDEX limit %s"%num
        self.cur.execute(sql)
        count = self.cur.fetchall() # 多少条数据
        # logging.info(count)
        for i in count:
            index.append(i[0])
        return index
    def isExistStory(self,STORYNO):
        sql="SELECT count(*) FROM story_url where STORYNO=%s"%STORYNO
        self.cur.execute(sql)
        count = self.cur.fetchall()[0][0]  # 多少条数据
        # logging.info(count)
        if count:
            return True
        else:
            return False
    def inertStoryUrl(self,storyNo,storyTitle,storyUrl):#插入小说的链接地址
        sql= "INSERT INTO story_url(storyno,storytitle,storyurl) VALUES ('{}','{}','{}')".format(storyNo, storyTitle,storyUrl)
        self.cur.execute(sql)
        self.conn.commit()
        msg="新增小说："+storyTitle+"下载地址"
        logging.info(msg)
    def insetStoryContentUrl(self,storyno,storychapter,chapter_num_url):
        sql= "INSERT INTO story_content_url(storyno,chapter_num,chapter_num_url) VALUES ('{}','{}','{}')".format(storyno, storychapter,chapter_num_url)
        self.cur.execute(sql)
        self.conn.commit()
    def getStoryContentCount(self,storyno):#获取该小说所有链接地址之和
        count_sql = "SELECT count(*) FROM story_content_url where storyno=%s"%(storyno)
        # logging.info(count_sql)
        self.cur.execute(count_sql)
        count = self.cur.fetchall()[0][0]  # 多少条数据
        return count
    def getStoryDownLoadUrl(self,storyno): #获取需要下载的小说章节
        urls=[]
        count_sql = "SELECT chapter_num_url FROM story_content_url where storyno=%s"%(storyno)
        # logging.info(count_sql)
        self.cur.execute(count_sql)
        result=self.cur.fetchall()
        for i in result:
            urls.append(i[0])
        # dict[storyno]=urls # 多少条数据
        return urls
    def getAreadyStoryDownLoadUrl(self,storyno):#获取已下载小说的章节
        chapternum=[]
        sql = "SELECT CHAPTER_NUM FROM STORY  WHERE STORY_NO=%s ORDER BY CHAPTER_NUM"%storyno
        self.cur.execute(sql)
        result = self.cur.fetchall()
        for i in result:
            chapternum.append(i[0])
        return chapternum
    def getDownLoadSrotyNo(self,num):#获取需要下载小说的No,num为下载故事的个数
        storyno=[]
        sql="SELECT storyno FROM story_url LIMIT %s"%num
        self.cur.execute(sql)
        result=self.cur.fetchall()
        for i in result:
            storyno.append(i[0])
        return storyno
    def getSrotyUrl(self,num):#获取需要下载小说的链接地址,num为下载故事的个数
        sql="SELECT storyno,storyurl,storytitle FROM story_url LIMIT %s"%num
        self.cur.execute(sql)
        result=self.cur.fetchall()
        return result
    def getSrotyDownUrl(self,storyno):#获取需要下载小说的链接地址,num为下载故事的个数
        sql="SELECT storyurl FROM story_url LIMIT %s"%storyno
        self.cur.execute(sql)
        result=self.cur.fetchall()[0][0]
        return storyno,result

    def getStorySumChapter_Num(self,storyno):#获取该小说所有章节之和
        count_sql = "SELECT count(*) FROM STORY where story_no=%s"%(storyno)
        # logging.info(count_sql)
        self.cur.execute(count_sql)
        count = self.cur.fetchall()[0][0]  # 多少条数据
        return count
    def getWithOutDownLoadChapternum(self,storyno):#获取该小说未下载的故事章节
        chapternum=[]
        sql ="select chapter_num from story where story_no=%s and state=0 ORDER BY chapter_num"%(storyno)
        self.cur.execute(sql)
        result=self.cur.fetchall()
        for i in result:
            chapternum.append(i[0])
        return chapternum
    def getStoryTitle(self,storyno): #根据小说ID获取小说标题
        sql = "SELECT STORYTITLE FROM STORY_URL WHERE storyno=%s"%(storyno)
        self.cur.execute(sql)
        stroytitle=self.cur.fetchall()[0][0]
        return stroytitle
    def getStoryText(self,chapternums):#根据章节ID获虎丘需要再找的内容
        dict={}
        for chapternum in chapternums:
            sql = "SELECT  chapter,text FROM STORY  WHERE CHAPTER_NUM=%s"%chapternum
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for i in result:
                dict[i[0]]=i[1]
        return dict
    def insertStory(self,url,text,storyno):
        logging.info(storyno)
        storytitle=self.getStoryTitle(storyno)
        logging.info(url)
        reg=re.compile(r'http://m.xsqishu.com(.+).html')
        identical=reg.findall(url)  #同一小说相同的部分
        # logging.info(identical)
        chapter_reg = re.compile(r'%s/(\d+).html'%identical)
        chapter_num =str(chapter_reg.findall(url)[0])
        new_chapter_num=storyno+chapter_num.zfill(5)
        chapter = "第" + str(chapter_num) + "章"
        sql = "INSERT INTO story(chapter,url,text,chapter_num,story_no,state) VALUES ('{}','{}','{}','{}',{},{})".format(chapter, url, text,new_chapter_num,storyno,0)
        self.cur.execute(sql)
        logging_text = "更新小说- -%s- -%s" %(storytitle,chapter)
        logging.info(logging_text)
        self.conn.commit()
    def getDownLoadUrl(self,urls): #判断该URL是否下载，未下载加入需要下载的url地址
        downloadurl = []
        for url in urls:
            sql = "SELECT * FROM STORY WHERE url='{}'".format(url)
            self.cur.execute(sql)
            result = self.cur.fetchall()
            if len(result) == 0:
                downloadurl.append(url)
        return downloadurl
    def getDownLoadChapternum(self,storyno):#获取需要下载的章节
        allnums=self.getAllChapterNum(storyno)
        downloadchapternum=self.getWithOutDownLoadChapternum(storyno)
        count=len(allnums)
        maxchapternum=allnums[len(allnums)-1]
        withOutdownloadsql ="select count(*) from story where story_no=%s and state=0"%storyno
        self.cur.execute(withOutdownloadsql)
        withOutdownloadCount = self.cur.fetchall()[0][0] #统计未下载个数
        maxchapternum_sql ="select state from story where chapter_num=%s"%maxchapternum
        self.cur.execute(maxchapternum_sql)
        maxchapternum_state=self.cur.fetchall()[0][0]
        downnums=[]
        if withOutdownloadCount==0:
            return downnums
        elif withOutdownloadCount<count and maxchapternum_state==1: #全部下载
            downnums=allnums
            return downnums
        elif withOutdownloadCount==count: #全部下载
            downnums=allnums
            return downnums
        else:
            return handleChaprerNum(downloadchapternum)
    def changeState(self,nums):#更改状态
        for i in nums:
            sql="update story set state=1 where chapter_num =(%s)"%i
            self.cur.execute(sql)
            self.conn.commit()
# db=MySQL()
# print(db.getSrotyDownUrl(82869))
# #  print(db.getDownLoadSrotyNo(5))