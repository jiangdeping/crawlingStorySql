# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/29 17:03
from config import config
import configparser as cparser
import MySQLdb
filpath = config.dbpath
cf = cparser.ConfigParser()
cf.read(filpath)
host=cf.get("mysqlconf", "host"),
db=cf.get("mysqlconf", "db_name"),
user=cf.get("mysqlconf", "user"),
password=cf.get("mysqlconf", "password"),
port=int(cf.get("mysqlconf", "port")),
class MySQL(object):
    def __init__(self,host,port,user,password,db):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        # self.charset="utf8"
        # self.use_unicode=True
    def conn_db(self):
        self.conn=MySQLdb.connect(host=self.host,post=self.port,user=self.user,
                                  passwd=self.password,db=self.db)
                                  # charset=self.charset,use_unicode=self.use_unicode)
    # def get_cursor(self):
    #     self.cursor=self.conn.cursor()
    #     return self.cursor
    def close(self):
        self.conn.close()
    def getSrotyUrl(self,num):
        self.conn_db()
        cursor=self.get_cursor()
        sql="SELECT storyno,storyurl,storytitle FROM story_url LIMIT %s"%num
        result=cursor.execute(sql)
        result=cursor.feachall()
        return result
sql=MySQL(host,port,user,password,db)
sql.getSrotyUrl("82785")
