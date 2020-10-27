# -*- coding: utf-8 -*-
# Author:jiang
# #
# from Function.crawlingStorySql.util.mysql import getStoryText,getStoryText
from config import config
from util.log import logger as loggering

filename = config.stroypath
import os


def writeText(storydict, flag):
    if flag == 0:
        os.remove(filename)
    for k, v in storydict.items():
        value = k + "\n" + v + "\n"
        with open(filename, "a", encoding="utf-8")as f:
            try:
                f.write(value)
            except Exception as e:
                loggering.warn(e)
