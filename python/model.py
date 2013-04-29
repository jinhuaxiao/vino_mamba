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
# Date: 4/26/13
# Time: 4:46 PM

class CSEResult:
    """
        desc:   the model of the search result
    """

    def __init__(self):
        self.id = ''
        self.title = ''
        self.snippet = ''                   #snippet
        self.link = ''                      #formattedUrl
        self.cacheId = ''                   #joined with cache-base url can find the google cache
        self.keywords = ''                  #keywords splited by ','


pass
