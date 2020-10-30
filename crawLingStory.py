# -*- coding: utf-8 -*-
# Author:jiang
# 2020/10/27 14:35
downloadnum=9 # 设置 downloadnum=False全量下载
storynums=30 #下载的故事个数 storynum=Fasle 全量下载
from util.log import logger as logging
# from mysql.storyMysql import getStoryNum, getDownLoadUrl, getStoryTitle,getAllStoryText,getStoryText
from util.getStoryContentUrl import getStoryContentUrl
from util.downLoadStory import downLoadStory
from util.storyWriteTxt import storyWriteTxt
# from mysql.allStoryUrlMysql import getSrotyUrl
from mysql.mySQL import MySQL
db=MySQL()
def main():
    storynos=db.getDownLoadSrotyNo(storynums)
    for storyno in storynos:
        newdownLoadUrl=[]
        storytitle=db.getStoryTitle(storyno)
        downloadUrl=db.getStoryDownLoadUrl(storyno)#获取需要下载小说的链接地址
        alreadyDownloadUrl=db.getAreadyStoryDownLoadUrl(storyno) #获取已下载小说的链接地址
        #i:http://m.xsqishu.com/book/54/82868.html
        if len(downloadUrl)==0:#如果该小说没有存入链接地址，重新获取
            msg="没有- -<"+storytitle+">- -的下载地址,重新获取"
            logging.info(msg)
            data=db.getSrotyDownUrl(storyno) #downloadnum需要下载的个数
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
        # for storyno,urls in urls_dict.items():
        # #     if downloadnum:
        # #         url = urls[0:downloadnum]
        # #     else:
        # #         url = urls
        # #     logging.info(url)
        #     #url=['http://m.xsqishu.com/book/100/82862/1.html', 'http://m.xsqishu.com/book/100/82862/2.html']
        #     storytitle=db.getStoryTitle(storyno)
        #     count_num = db.getStorySumChapter_Num(storyno) #获取该小说所有章节之和
        #     logging.info("len(url)")
        #     logging.info(len(url))
        #     logging.info("count_num")
        #     logging.info(count_num)
        #     if len(url)==0:
        #         msg="小说- - -"+storytitle+"- - -暂未提供下载"
        #         logging.info(msg)
        #     else:
        #         if count_num == len(url):
        #             msg="小说- - -"+storytitle+"- - -未更新"
        #             logging.info(msg)
        #         if count_num < len(url):
        #             logging.info("------------")
        #             logging.info(url)
        #             downLoadUrl = db.getDownLoadUrl(url)
        #             downLoadStory(storyno,downLoadUrl)
        #             storyWriteTxt(storyno)
        #         # dict = getAllStoryText()  # 获取全量小说
        #         # if dict:
        #         #     storyWriteTxt(dict,storyno,flag=0)
        #         # dict = getStoryText(downLoadUrl)  # 获取增量小说
        #         # if dict:
        #         #     storyWriteTxt(dict,storyno,flag=1)
if __name__ == '__main__':
    main()

    ###爬取过程中中断后写入txt出现问题
