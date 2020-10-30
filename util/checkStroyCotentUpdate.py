# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/30 14:56
from mysql.mySQL import MySQL
db=MySQL()
def checkStoryCotentUpdate(storyno,downloadurls):
    count=db.getStoryContentCount(storyno)