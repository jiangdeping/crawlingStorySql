# -*- coding: utf-8 -*-
# Author:jiang
# 2020/10/27 14:35
downloadnum=4  # 设置 downloadnum=False全量下载
storynums=2  #下载的故事个数 storynum=Fasle 全量下载
from util.log import logger as logging
from mysql.storyMysql import getStoryNum, getDownLoadUrl, getStoryTitle,getAllStoryText,getStoryText
from util.getStoryContentUrl import getStoryContentUrl
from util.downLoadStory import downLoadStory
from util.storyWriteTxt import storyWriteTxt
from mysql.allStoryUrlMysql import getSrotyUrl
from mysql.mySQL import MySQL
db=MySQL()
def main():
    url=db.getSrotyUrl(storynums)
    for i in url:
        urls_dict=getStoryContentUrl(i[0],i[1])
        for storyno,urls in urls_dict.items():
            if downloadnum:
                url = urls[0:downloadnum]
            else:
                url = urls
            storytitle=getStoryTitle(storyno)
            count_num = getStoryNum(storyno)
            if count_num == len(url):
                msg="小说- - -"+storytitle+"- - -未更新"
                logging.info(msg)
            elif count_num < len(url):
                downLoadUrl = getDownLoadUrl(url)
                downLoadStory(storyno,downLoadUrl)
                storyWriteTxt(storyno)
                # dict = getAllStoryText()  # 获取全量小说
                # if dict:
                #     storyWriteTxt(dict,storyno,flag=0)
                # dict = getStoryText(downLoadUrl)  # 获取增量小说
                # if dict:
                #     storyWriteTxt(dict,storyno,flag=1)
if __name__ == '__main__':
    main()

    ###爬取过程中中断后写入txt出现问题
