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


def insert(searchResultList):
    '''
        desc:   insert search result list into db
        args:   list of cse
        return: none
    '''
    pass

def getCSEResult(count=10):
    '''
        desc:   get custom search result from db(mysql) [default count item is 10]
                Attetion: the results records will be deleting and flow into history records
        args:   number:item count
        return: list
    '''
    pass

def deleteCSEFlowintoHistory(searchResultList):
    '''
        desc:   delete (cse) result. Ah, it's not truth!
                the analysised result will be flowed into history records table
        args:   list of deleting cse result
        return: none
    '''
    pass

def clearHistory():
    '''
        desc:   clear all history records
        args:   none
        return: none
    '''
    pass
