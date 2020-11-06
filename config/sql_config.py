# -*- coding: utf-8 -*-
#Author:jiang
#2020/11/3 14:33

from  datetime import datetime
storyIndexCountSql="SELECT count(*) FROM STORY_INDEX"
getStoryPageIndexCountSql="SELECT count(*) FROM STORY_INDEX"
def getStoryIndexSql(num):
    sql="SELECT storyindexurl FROM STORY_INDEX limit %s"%num
    return sql
def getinertStoryPageIndex(storyindexID, storyindexUrl):
    createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO story_index(storyindexID,storyindexUrl,createtime,updatetime) VALUES ('{}','{}','{}','{}')".format(
            storyindexID, storyindexUrl, createtime, updatetime)
    return sql