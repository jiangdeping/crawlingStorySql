# -*- coding: utf-8 -*-
# Author:jiang
# 2020/10/27 15:16
import re
from fake_useragent import UserAgent
from util.get_url import get_url
from config import config
import requests

url = config.url
res = requests.get(url)
print(res.text)
print(hello)