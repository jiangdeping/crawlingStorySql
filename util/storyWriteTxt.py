# -*- coding: utf-8 -*-
# Author:jiang
# #
# from Function.crawlingStorySql.util.mysql import getStoryText,getStoryText
from mysql.storyWriteTxtSql import getStoryText
from util.log import logger as loggering
from mysql.storyMysql import getStoryTitle
import os
#
def storyWriteTxt(storydict,storyno, flag):
    storyTitle=getStoryTitle(storyno)
    path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename=os.path.join(path,"story\\"+storyTitle+".txt")
    if flag == 0:
        os.remove(filename)
    for k, v in storydict.items():
        value = k + "\n" + v + "\n"
        with open(filename, "a", encoding="utf-8")as f:
            try:
                f.write(value)
            except Exception as e:
                loggering.warn(e)
# storyno=["82785","82784"]
def storyWriteTxt1(storynos,flag=0):
    for storyno in storynos:
        storyTitle=getStoryTitle(storyno)
        storydict=getStoryText(storyno)
        for i in storydict:
            print(i[2].encode("gbk"))
        path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename=os.path.join(path,"story\\"+storyTitle+".txt")
        if flag == 0:
            os.remove(filename)
        for k, v in storydict.items():
            value = k + "\n" + v + "\n"
            with open(filename, "a", encoding="utf-8")as f:
                try:
                    f.write(value)
                except Exception as e:
                    loggering.warn(e)
