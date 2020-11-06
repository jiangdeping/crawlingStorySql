# -*- coding: utf-8 -*-
#Author:jiang
#2020/11/3 17:06
# -*- coding: utf-8 -*-
# Author:jiang
# 2020/10/27 14:35

from util.log import logger as logging
from util.getStoryContentUrl import getStoryContentUrl,get_story_urls
from util.downLoadStory import downLoadStory
from mysql.mySQL import MySQL
from config.sql_config import storyIndexCountSql,getStoryIndexSql
from util.getStoryIndex import get_index_url
from config import setting
from config.db_dbutils_init import MyConnectionPool
db=MySQL()
mysql=MyConnectionPool()
downloadnum=setting.DOWNLOADNUM  # 设置 downloadnum=False全量下载
storynum=setting.STORYNUM  #下载的故事个数 storynum=Fasle 全量下载
indexnum=setting.INDEXNUM   #小说索引页数
def downLoadStoryIndex():#获取小说的索引地址
    indexnum=mysql.getOne(storyIndexCountSql)[0] #当前已下载的索引页面总和
    indexurl=setting.url
    get_index_url(indexnum,indexurl)
def downLoadStoryNoUrl():#获取每部小说的下载地址
    indexnum=setting.INDEXNUM
    if indexnum==False:
        indexnum=mysql.getOne(storyIndexCountSql)[0]
    storyurls=mysql.getOne(getStoryIndexSql(indexnum))
    storynos=get_story_urls(storyurls)
    return storynos
def downLoadStoryCotentUrl(storyno):#获取每部小说内容的下载地址
    StoryCotentUrlList=db.getStoryDownUrl(storyno)
    storyno=StoryCotentUrlList[0]
    url=StoryCotentUrlList[1]
    print(storyno,url)
    getStoryContentUrl(storyno,url)
def getDownLoadStoryNo():#获取需要下载的小说ID
    storynos=db.getDownLoadSrotyNo(storynum)
def downLoadStoryTxt(storyno): #根据小说ID获取小说章节内容并下载
    newdownLoadUrl=[]
    storytitle=db.getStoryTitle(storyno)
    downloadUrl=db.getStoryDownLoadUrl(storyno)#获取需要下载小说的链接地址
    alreadyDownloadUrl=db.getAreadyStoryDownLoadUrl(storyno) #获取已下载小说的链接地址
    if len(downloadUrl)==0:#如果该小说没有存入链接地址，重新获取
            msg="没有- -<"+storytitle+">- -的下载地址,重新获取"
            logging.info(msg)
            data=db.getStoryDownUrl(storyno) #downloadnum需要下载的个数
            #data数据类型  #i[0] storyno,i[1]下载地址，i[2]标题
            urls=getStoryContentUrl(data[0],data[1])
            if len(urls)==0:
                msg="小说- - -<"+storytitle+">- - -暂未提供下载"
                logging.info(msg)
            else:
                newdownLoadUrl=urls
    elif len(downloadUrl)==len(alreadyDownloadUrl):
            msg="小说- - -"+storytitle+"- - -未更新"
            logging.info(msg)
    else:
        newdownLoadUrl=(set(downloadUrl).difference(set(alreadyDownloadUrl)))
    logging.info(newdownLoadUrl)
    downLoadStory(storyno,newdownLoadUrl)
downLoadStoryIndex()
srotynos=downLoadStoryNoUrl()
# for i in srotynos:
#     downLoadStoryCotentUrl(i)
# for i in srotynos:
#     downLoadStoryTxt(i)