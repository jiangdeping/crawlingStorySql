# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/28 13:21
import MySQLdb
from config import config
import configparser as cparser
def con_db():#1111
    filpath = config.dbpath
    cf = cparser.ConfigParser()
    cf.read(filpath)
    DB = MySQLdb.Connect(
        host=cf.get("mysqlconf", "host"),
        db=cf.get("mysqlconf", "db_name"),
        user=cf.get("mysqlconf", "user"),
        password=cf.get("mysqlconf", "password"),
        port=int(cf.get("mysqlconf", "port")),
        charset="utf8",
        use_unicode=True,
    )
    return DB