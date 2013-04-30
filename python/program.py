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
# -------------------------------------------------------
# Created with PyCharm.
# User: yanghua
# Date: 4/29/13
# Time: 12:21 PM

from search import searchManager
from dao import dataAccessManager
from report import pdfReporter


class program:
    """
        desc:   it's the main login of the project
    """

    def __init__(self):
        self.searchManager = searchManager()
        self.dataAccessManager = dataAccessManager()
        self.reporter = pdfReporter()
        pass

    def do(self):
        """
            desc:   it's the program's entry method
            args:   None
            return: None
        """
        cseResultList = self.searchManager.doSearch()
        self.dataAccessManager.insert(cseResultList)
        handledResultList = self.dataAccessManager.getCSEResult()
        self.reporter.generatePDF(handledResultList)