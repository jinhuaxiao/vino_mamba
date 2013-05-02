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
# Date: 4/27/13
# Time: 9:28 AM

import ConfigParser

SECTION_API_REQUEST = 'api_request'


class configManager:
    """
        desc: the manager of the config file
    """

    def __init__(self):
        pass

    def getConfigVal(self, section, key):
        """
            desc:   get config value by sectionName and key
            args:   section - the name of the section
                    key - the key of the value
            return: value(string)
        """
        if section is None or len(section) is 0:
            raise BaseException, 'the section can not be none or empty'

        if key is None or len(key) is 0:
            raise BaseException, 'the key can not be none or empty'

        result = ''

        config = ConfigParser.ConfigParser()
        with open('../config.conf', mode='rw') as configFile:
            config.readfp(configFile)
            result = config.get(section, key)

        return result

    def setConfigVal(self, section, key, value):
        """
            desc:   set config value by sectionName and key
            args:   section - the name of the section
                    key - the setting option's key
                    value - the setting option's value
            return: None
        """
        if not section or len(section) is 0:
            raise BaseException, 'the section can not be none or empty'

        if not key or len(key) is 0:
            raise BaseException, 'the key can not be none or empty'

        if not value or len(value) is 0:
            raise BaseException, 'the value can not be none or empty'

        config = ConfigParser.ConfigParser()
        with open('../config.conf', mode='rw') as configFile:
            config.readfp(configFile)
            config.set(section, key, value)
        config.write(open("../config.conf", "w"))



