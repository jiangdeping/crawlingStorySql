# -*- coding: utf-8 -*-
#Author:jiang
#2020/11/3 10:51
from dbutils.pooled_db import PooledDB
from config import db_configs
from util.log import logger as logging
import  MySQLdb
#
class BasePymysqlPool(object):
    def __init__(self):
        self.host=db_configs.HOST,
        self.port=int(db_configs.PORT),
        self.user=db_configs.USER,
        self.passwd=db_configs.PASSWORD,
        self.db=db_configs.DB_NAME,
        self.use_unicode=True,
        self.charset="utf8"
class MyConnectionPool(BasePymysqlPool):
    __pool=None
    def __init__(self):
        super(MyConnectionPool, self).__init__()
        self._conn=self.__getConn()
        self._cursor=self._conn.cursor()
    def __getConn(self):
        if MyConnectionPool.__pool is None:
            __pool=PooledDB(
            creator=db_configs.DB_CREATOR,
            mincached=db_configs.DB_MIN_CACHED,
            maxcached=db_configs.DB_MAX_CACHED,
            maxshared=db_configs.DB_MAX_SHARED,
            maxconnections=db_configs.DB_MAX_CONNECYIONS,
            blocking=db_configs.DB_BLOCKING,
            maxusage=db_configs.DB_MAX_USAGE,
            setsession=db_configs.DB_SET_SESSION,
            host=db_configs.HOST,
            port=int(db_configs.PORT),
            user=db_configs.USER,
            passwd=db_configs.PASSWORD,
            db=db_configs.DB_NAME,
            charset="utf8",
            use_unicode=True,
        )
        return __pool.connection()

    # 释放连接池资源
    def getOne(self, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result
    def execute(self,sql,param=None):
        """
        基础更新、插入、删除操作
        :param sql:
        :param param:
        :return: 受影响的行数
        """
        ret=None
        try:
            if param==None:
                print(sql)
                ret=self._cursor.execute(sql)
            else:
                ret=self._cursor.execute(sql,param)
            self._conn.commit()
        except TypeError as te:
            logging.debug("类型错误")
            logging.exception(te)
        return ret
    def insert(self,sql,param=None):
        """
        数据库插入
        :param sql: SQL语句
        :param param: 参数
        :return: 受影响的行数
        """
        return self.execute(sql,param)
    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()
