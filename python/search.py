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
# ---
# Created with PyCharm.
# User: yanghua
# Date: 4/25/13
# Time: 11:53 AM

import sys
import re

GLOABL_APP_ARGS = dict(
    API_KEY='AIzaSyDSAxrt1UMK_uLRGGlBJXiR6xYUxzwR1_w',
    API_VERSION='v1',
    SERVICE_NAME='customsearch',
    SEARCH_ENGINE_ID='002302950730219782374:x2mqpz7mwog')

API_URL_PATTERN = 'https://www.googleapis.com/{service_name}/\
{api_version}?key={api_key}&cx={search_engine_id}&q={keywords}'

API_ARGS_REG_PATTERN = '\{[^\{\}]*\}'


def generateRequestUrl(keywordsList):
    """
        desc:   to generate request api url
        args:   none
        return: none
    """
    global API_URL_PATTERN
    if keywordsList is None:
        raise BaseException, "the keywords can not empty"

    [replaceArgValWithConfigedKey(keyItem) for keyItem in GLOABL_APP_ARGS.iterkeys()]

    return API_URL_PATTERN.replace('{keywords}', '+'.join(keywordsList))


def replaceArgValWithConfigedKey(key):
    '''
        desc:   replace arg value with configed key
        args:   none
        return: none
    '''
    global API_URL_PATTERN
    pattern = "{%s}" % key.lower()
    API_URL_PATTERN = API_URL_PATTERN.replace(pattern, GLOABL_APP_ARGS[key])


def getResponse():
    '''
        desc:   get http response
        args:   none
        return: none
    '''
    pass


#test:
print(generateRequestUrl(['yanghua', 'kobe', 'nba']))




