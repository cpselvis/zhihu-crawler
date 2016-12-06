#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import time


class MySQL:

    error_code = ''
    _instance = None
    _conn = None
    _cursor = None
    _TIMEOUT = 30
    _timecount = 0

    def __init__(self, cfg):
        try:
            self._conn = MySQLdb.connect(
                host = cfg["host"],
                port = cfg["port"],
                user = cfg["user"],
                passwd = cfg["passwd"],
                db = cfg["db"],
                charset = cfg["charset"]
            )
        except MySQLdb.Error as e:
            self.error_code = e.args[0]
            print "MySQL error %d: %s" % (e.args[0], e.args[1])

            # Try to reconnect if not timeout
            if self._timeout < self._TIMEOUT:
                interval = 5
                self._timecout += interval
                time.sleep(interval)
                return self.__init__(cfg)
            else:
                raise Exception(error_msg)

        self._cursor = self._conn.cursor()
        self._instance = MySQLdb

    def query(self, sql):
        try:
            self._cursor.execute("SET NAMES utf8")
            result = self._cursor.execute(sql)
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "MySQL error %d: %s" % (e.args[0], e.args[1])
            result = False

        return result

    def update(self, sql):
        try:
            self._cursor.execute("SET NAMES utf8")
            result = self._cursor.execute(sql)
            self._conn.commit()
        except MySQLdb.Error as e:
            self.error_code = e.args[0]
            print "MySQL error %d: %s" % (e.args[0], e.args[1])
            result = False

        return result

    def insert(self, sql):
        try:
            self._cursor.execute("SET NAMES utf8")
            self._cursor.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except MySQLdb.Error as e:
            self.error_code = e.args[0]
            print "MySQL error %d: %s" % (e.args[0], e.args[1])
            return False

    def getRowCount(self):
        return self._cursor.rowcount


    def __del__(self):
        try:
            self._cursor.close()
            self._conn.close()
        except:
            pass
    
    def close(self):
        self.__del__()
