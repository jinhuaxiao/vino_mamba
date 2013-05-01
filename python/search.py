#! /Users/yanghua/Documents/Python/Virtualenvs/v2.7.2/vino_mamba/bin/python
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
# -------------------------------------------------------------------
# Created with PyCharm.
# User: yanghua
# Date: 4/25/13
# Time: 11:53 AM

import re
import configUtility
import json
import urllib2
import model
from random import randint

API_ARGS_REG_PATTERN = "\{[^\{\}]*\}"


class searchManager:
    def __init__(self):
        self.CSEResultList = []
        self.requestUrl = ''
        self.configManager = configUtility.configManager()
        pass

    def __generateRequestUrl(self):
        """
            desc:   to generate request api url
            args:   none
            return: none
        """
        self.requestUrl = self.configManager.getConfigVal('api_request', 'api_url_pattern')
        matchedList = re.findall(API_ARGS_REG_PATTERN, self.requestUrl)
        if not matchedList:
            raise BaseException, 'the matchObj can not be none'
        [self.__replaceArgValWithConfigedKey(item) for item in matchedList]

    def __replaceArgValWithConfigedKey(self, matchedItem):
        """
            desc:   replace arg value with configed key
            args:   matchedItem - matchedItem like {XXX}
            return: none
        """
        if not matchedItem or len(matchedItem) == 0:
            raise BaseException, 'matchedItem can not be none'
        config_key = matchedItem[1:-1]
        if config_key != 'keywords':
            self.requestUrl = self.requestUrl.replace(matchedItem,
                                                      self.configManager.getConfigVal('api_request', config_key))
        else:
            #format keywords from a,b,c to a+b+c requied by google cse api
            keywordsStr=self.configManager.getConfigVal('api_request', config_key)
            if self.configManager.getConfigVal('api_request', 'keep_keywords_sequence').lower() != 'false':

                keywordsFormattedToReqParam = keywordsStr.split(',').join('+')
                self.requestUrl = self.requestUrl.replace(matchedItem, keywordsFormattedToReqParam)
            else:                       #random sequence
                keywordList = keywordsStr.split(',')
                formattedKeywords = ''
                keywordsFormatter = '%s+'
                while (len(keywordList) != 0):
                    #random index from 0 to len-1
                    tmp_index = randint(0, len(keywordList) - 1)
                    formattedKeywords = formattedKeywords+''+ keywordsFormatter % keywordList[tmp_index]
                    #remove the used element from list
                    keywordList.remove(keywordList[tmp_index])

                formattedKeywords = formattedKeywords[0:-1]
                self.requestUrl = self.requestUrl.replace(matchedItem, formattedKeywords)


    def __getResponseData(self):
        """
            desc:   get http response parser
            args:   none
            return: the response data
        """
        self.__generateRequestUrl()
        header = {'User-Agent': 'mozilla/5.0 (windows; U; windows NT 5.1; zh-cn)'}
        responseData = None
        try:
            req = urllib2.Request(self.requestUrl, headers=header)
            responseData = urllib2.urlopen(req).read()
        except urllib2.HTTPError, e:
            print(e.code)
            print(e.message)
            print(e.headers)
            print(e.fp.read())

        return responseData


    def getParsedJSON(self):
        """
            desc:   get parsed json object
            args:   None
            return: json object
        """
        responseData = self.__getResponseData()
        if not responseData:
            raise BaseException, 'the http response data can not be none'

        resultDic = json.loads(responseData)
        if not resultDic:
            raise BaseException, 'the json prase error!'
        return resultDic

    def loadModel(self, jsonObj):
        """
            desc:   load model from json obj
            args:   jsonObj - the json dic
            return: List of models
        """
        if not jsonObj and not jsonObj['items']:
            raise BaseException, 'the jsonObj can not be none'

        keyworlds = self.configManager.getConfigVal('api_request', 'keywords')

        result = []
        for item in jsonObj['items']:
            if not item:
                continue
            entity = model.CSEResult()
            entity.title = item['title']
            entity.snippet = item['snippet']
            entity.cachedId = item['cacheId']
            entity.link = item['link']
            entity.keywords = keyworlds
            result.append(entity)

        return result

    def doSearch(self):
        """
            desc:   the public-main method available to the outter
            args:   None
            return: boxed model list
        """
        resultDic = self.getParsedJSON()
        return self.loadModel(resultDic)








