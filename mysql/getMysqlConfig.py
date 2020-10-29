# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 13:17
from configparser import ConfigParser
from config import config
class ConfigParse(object):
    def __init__(self):
        pass
    @classmethod
    def get_db_config(cls):
        #cls使用的类方法,cls就是指定本身
        cls.cfp = ConfigParser()
        cls.cfp.read(config.dbpath)
        host = cls.cfp.get("mysqlconf", "host")
        port = cls.cfp.get("mysqlconf", "port")
        user = cls.cfp.get("mysqlconf", "user")
        password = cls.cfp.get("mysqlconf", "password")
        db = cls.cfp.get("mysqlconf", "db_name")
        return {"host":host, "port":port, "user":user, "password":password,"db":db}
