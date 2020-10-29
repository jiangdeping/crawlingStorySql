# -*- coding: utf-8 -*-
# Author:jiang
# #
# from Function.crawlingStorySql.util.mysql import getStoryText,getStoryText
from mysql.storyWriteTxtSql import getStoryText,getDownLoadChapternum,changeState
from util.log import logger as loggering
from mysql.storyMysql import getStoryTitle
import os
# def storyWriteTxt(storydict,storyno, flag):
#     storyTitle=getStoryTitle(storyno)
#     path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     filename=os.path.join(path,"story\\"+storyTitle+".txt")
#     if flag == 0:
#         os.remove(filename)
#     for k, v in storydict.items():
#         value = k + "\n" + v + "\n"
#         with open(filename, "a", encoding="utf-8")as f:
#             try:
#                 f.write(value)
#             except Exception as e:
#                 loggering.warn(e)
def storyWriteTxt(storynos):
    for storyno in storynos:
        #获取写入的文件名称
        storyTitle=getStoryTitle(storyno)
        print(storyTitle)
        path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename=os.path.join(path,"story\\"+storyTitle+".txt")
        #获取写入txt的章节
        nums=getDownLoadChapternum(storyno)
        print("---")
        storydict=getStoryText(nums)
        # if state:
        #     os.remove(filename)
        for k, v in storydict.items():
            value = k + "\n" + v + "\n"
            with open(filename, "a", encoding="utf-8")as f:
                try:
                    f.write(value)
                except Exception as e:
                    loggering.warn(e)
        changeState(nums)
no=["82783"]
storyWriteTxt(no)
# # nums=getStoryChapterNum(no)
# # dict=getStoryText(nums)
# # storyWriteTxt(dict,no,1)