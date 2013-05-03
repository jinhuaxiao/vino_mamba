#! /usr/local/bin/python
# -*- coding:utf-8 -*-
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ---
# Created with PyCharm.
# User: yanghua
# Date: 4/25/13
# Time: 11:53 AM

import model
import pymysql
import configUtility
import string


class dataAccessManager:
    """
        desc:   data access manager
    """

    def __init__(self):
        configManager = configUtility.configManager()
        self.encoder = 'utf8'
        self.host = configManager.getConfigVal('data_access', 'host')
        portStr = configManager.getConfigVal('data_access', 'port')
        self.user = configManager.getConfigVal('data_access', 'user')
        if portStr:
            self.port = string.atoi(portStr)
        else:
            self.port = 3306
        self.passwd = configManager.getConfigVal('data_access', 'passwd')
        if not self.passwd or len(self.passwd) is 0:
            self.passwd = '123456'
        self.db = configManager.getConfigVal('data_access', 'db')

    def insert(self, searchResultList):
        """
            desc:   insert search result list into db
            args:   list of cse
            return: none
        """
        if not searchResultList:
            raise BaseException, 'the searchResultList can not be none'

        insert_sql = 'INSERT INTO tb_cse_result (title,link,cacheId,snippet,generateTime,keywords) \
                        VALUES (%(title)s,%(link)s,%(cacheId)s,%(snippet)s,now(),%(keywords)s)'

        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, \
                               passwd=self.passwd, db=self.db, charset=self.encoder)
        cur = conn.cursor()

        for item in searchResultList:
            tmp_dic = dict()
            tmp_dic['title'] = item.title
            tmp_dic['link'] = item.link
            tmp_dic['cacheId'] = item.cacheId
            tmp_dic['snippet'] = item.snippet
            tmp_dic['keywords'] = item.keywords

            cur.execute(insert_sql, tmp_dic)
            pass

        conn.commit()
        cur.close()
        conn.close()
        pass

    def getCSEResult(self, count=10):
        '''
            desc:   get custom search result from db(mysql) [default count item is 10]
                    Attetion: the results records will be deleting and flow into history records
            args:   number:item count
            return: list
        '''

        select_sql="SELECT TOP %d * FROM tb_cse_result ORDER BY cse_id" % count

        conn=pymysql.connect(host=self.host, port=self.port, user=self.user, \
                               passwd=self.passwd, db=self.db, charset=self.encoder)
        cur = conn.cursor()

        cur.execute(select_sql)
        cur.fetchall()


        cur.close()
        conn.close()

        pass

    def deleteCSEFlowintoHistory(self, searchResultList):
        """
            desc:   delete (cse) result. Ah, it's not truth!
                    the analysised result will be flowed into history records table
            args:   list of deleting cse result
            return: none
        """
        if not searchResultList:
            raise BaseException,'searchResultList can not be none'

        #TODO: mysql 批量删除

        #TODO:插入历史表


        pass

    def insert_history(self,deletedCSEResult):
        """
            desc:   insert deleted cse result into cse_history
        """
        if not deletedCSEResult:
            raise BaseException,'deletedCSEResult can not be none'

        insert_sql='INSERT INTO tb_cse_result_history (hy)'

        pass

    def clearHistory(self):
        """
            desc:   clear all history records
            args:   none
            return: none
        """
        deleteAll_sql='DELETE FROM tb_cse_result_history'

        conn=pymysql.connect(host=self.host, port=self.port, user=self.user, \
                               passwd=self.passwd, db=self.db, charset=self.encoder)
        cur = conn.cursor()

        cur.execute(deleteAll_sql)

        conn.commit()
        cur.close()
        conn.close()

        pass
