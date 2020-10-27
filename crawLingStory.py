# -*- coding: utf-8 -*-
# Author:jiang
# 2020/10/27 14:35
downloadnum = 6  # 设置 downloadnum=False全量下载

from util.log import logger as logging
from util.mysql import getStoryNum, getDownLoadUrl, getStoryText, getAllStoryText
from util.get_url import get_url
from util.downLoadStory import downLoadStory
from config import config
from util import writetext


def main():
    allUrl = get_url(config.url)
    if downloadnum:
        url = allUrl[0:downloadnum]
    else:
        url = allUrl
    story_num = getStoryNum()
    max_num = story_num["max"]
    count_num = story_num["count"]
    if count_num == len(url):
        logging.info("小说未更新")
    elif count_num < len(url):
        if max_num == len(url):
            downLoadUrl = getDownLoadUrl(url)
            downLoadStory(downLoadUrl)
            dict = getAllStoryText()  # 获取全量小说
            if dict:
                writetext.writeText(dict, flag=0)
        else:
            downLoadUrl = url[count_num:len(url)]
            downLoadStory(downLoadUrl)
            dict = getStoryText(downLoadUrl)  # 获取增量小说
            if dict:
                writetext.writeText(dict, flag=1)


if __name__ == '__main__':
    main()

    ###爬取过程中中断后写入text出现问题
