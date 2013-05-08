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
# Date: 4/30/13
# Time: 1:20 PM

import reportlabLibs
import time, re
from configUtility import configManager

PDF_FileName_REG_PATTERN = "\{[^\{\}]*\}"
Cache_Url_Reg_PATTERN = "\{[^\{\}]*\}"


class pdfReporter:
    """
        desc:   pdf reporter
    """

    #privite fields
    __pdfOperator = None

    def __init__(self):
        pass

    def __generateFileName(self):
        """
            desc:   generate pdf's file name by config-file pdf_fileNamePattern
        """
        timePartSet = time.localtime(time.time())
        timeDict = dict()
        timeDict['month'] = timePartSet[1]
        timeDict['day'] = timePartSet[2]
        timeDict['hour'] = timePartSet[3]
        timeDict['minute'] = timePartSet[4]
        timeDict['second'] = timePartSet[5]

        fileName = 'cseResult.pdf'

        fileName_pattern = configManager().getConfigVal('report', 'pdf_fileNamePattern')
        matchedList = re.findall(PDF_FileName_REG_PATTERN, fileName_pattern)
        if matchedList:
            fileName = fileName_pattern
            for matchedItem in matchedList:
                tmp_key = matchedItem[1:-1]
                fileName = fileName.replace(matchedItem, str(timeDict[tmp_key]))

        return fileName


    def getPDFOperater(self):
        """
            desc:   get the operator of the pdf
            args:   None
            return: None
        """
        if self.__pdfOperator:
            return self.__pdfOperator
        filePath = configManager().getConfigVal('report', 'pdf_filePath')

        if not filePath or len(filePath) == 0:
            raise BaseException, 'the config-key:pdf_filePath can not be empty'

        fileName = self.__generateFileName()

        if filePath[-1] != '/' and fileName[0] != '/':
            filePath = '%s/' % filePath

        fileFullPath = filePath + '' + fileName
        print(fileFullPath)
        self.__pdfOperator = reportlabLibs.canvas.Canvas(fileFullPath, pagesize=reportlabLibs.A4)
        return self.__pdfOperator

    def __drawTable(self, itemindex, cseResultItem):
        """
            desc:   draw table
            args:   cseResultItem - cse result item
            return: None
        """
        tbData = self.__generateCSEResultTBData(cseResultItem)
        table = reportlabLibs.Table(tbData, colWidths=[3.05 * reportlabLibs.cm, 15 * reportlabLibs.cm])

        table.setStyle(reportlabLibs.TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, reportlabLibs.colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, reportlabLibs.colors.black),
        ]))

        table.wrapOn(self.getPDFOperater(), reportlabLibs.width, reportlabLibs.height)

        tb_x = 1.8
        tb_y = 0
        if itemindex % reportlabLibs.tb_numPerPage == 0:                 #page start
            tb_y = reportlabLibs.tb_firstItem_top
        else:
            tb_y = reportlabLibs.tb_firstItem_top + (
                                                        itemindex % reportlabLibs.tb_numPerPage) * reportlabLibs.tb_height + (
                       itemindex % reportlabLibs.tb_numPerPage ) * reportlabLibs.tb_margin_v

        if itemindex != 0 and itemindex % reportlabLibs.tb_numPerPage == 0:
            self.getPDFOperater().showPage()        #new a page

        table.drawOn(self.getPDFOperater(), *reportlabLibs.coord(tb_x, tb_y, reportlabLibs.cm))


    def __generateCachedLink(self, cacheId, originalLink):
        """
            desc:   generate cached url by config-file's cache_url_pattern
            args:   cacheId - string
                    originalLink - string
            return: generated cached url
        """
        if not cacheId or len(cacheId) is 0:
            raise BaseException, 'cachedId can not be none or empty'

        if not originalLink or len(originalLink) is 0:
            raise BaseException, 'original can not be none or empty'

        cachedLink = cacheId

        matchingDict = dict()
        matchingDict['cacheId'] = cacheId
        matchingDict['originalUrl'] = originalLink

        url_pattern = configManager().getConfigVal('api_request', 'cache_url_pattern')
        matchedList = re.findall(Cache_Url_Reg_PATTERN, url_pattern)
        if url_pattern and matchedList and len(matchedList) != 0:
            cachedLink = url_pattern
            for matchedItem in matchedList:
                tmp_key = matchedItem[1:-1]
                cachedLink = cachedLink.replace(matchedItem, str(matchingDict[tmp_key]))

        return cachedLink


    def __generateCSEResultTBData(self, cseResultItem):
        """
            desc:   generate table data for generating table in pdf
            args:   the model of cse result
            return: the data List
        """
        if not cseResultItem:
            raise BaseException, 'the cseResultItem can not be None'
            # Keys
        htitle = reportlabLibs.Paragraph('''<b>title</b>''', reportlabLibs.styleBH)
        hlink = reportlabLibs.Paragraph('''<b>link</b>''', reportlabLibs.styleBH)
        hcachelink = reportlabLibs.Paragraph('''<b>cache link</b>''', reportlabLibs.styleBH)
        hsnippet = reportlabLibs.Paragraph('''<b>snippet</b>''', reportlabLibs.styleBH)
        hkeywords = reportlabLibs.Paragraph('''<b>key words</b>''', reportlabLibs.styleBH)
        hmatchdegree = reportlabLibs.Paragraph('''<b>match degree</b>''', reportlabLibs.styleBH)

        # Values
        warppedUrl = '<link href=\'%s\' color=\'blue\'><u>%s</u></link>' % (cseResultItem.link, cseResultItem.link)

        cachedLink = self.__generateCachedLink(cseResultItem.cacheId, cseResultItem.link)
        warppedCachedUrl = '<link href=\'%s\' color=\'blue\'><u>%s</u></link>' % (cachedLink, cachedLink)
        strongedSnippet=self.__StrongKeywords(cseResultItem.snippet,cseResultItem.keywords)

        title = reportlabLibs.Paragraph(cseResultItem.title, reportlabLibs.styleN)
        link = reportlabLibs.Paragraph(warppedUrl, reportlabLibs.styleN)
        cachelink = reportlabLibs.Paragraph(warppedCachedUrl, reportlabLibs.styleN)
        snippet = reportlabLibs.Paragraph(strongedSnippet, reportlabLibs.styleN)
        keywords = reportlabLibs.Paragraph(cseResultItem.keywords, reportlabLibs.styleN)
        matchdegree = reportlabLibs.Paragraph('70%', reportlabLibs.styleN)

        data = \
            [
                [htitle, title],
                [hlink, link],
                [hcachelink, cachelink],
                [hsnippet, snippet],
                [hkeywords, keywords],
                [hmatchdegree, matchdegree]
            ]

        return data

    def __StrongKeywords(self, originalStr, keywords):
        """
            desc:   package keywords with tag to Strong them
            args:   originalStr - String
                    keywords - keywords joined with ','
            return: packaged content
        """

        if not originalStr:
            raise BaseException, 'the arg:originalStr can not be none'

        if not keywords or len(keywords) == 0:
            raise BaseException, 'the arg:keywords can not be none or empty'

        keywordsList = keywords.split(',')
        originalStr=originalStr.lower()
        for keyword in keywordsList:
            newStr = '<font color=\'red\'>%s</font>' % keyword
            originalStr = originalStr.replace(keyword, newStr)

        result = originalStr

        return result

    def generatePDF(self, cseResultList):
        """
            desc:   generate pdf
            args:   cseResultList - cse list
            return: None
        """
        if not cseResultList or len(cseResultList) is 0:
            raise BaseException, 'the cseResultList can not be none or empty'

        textobject = self.getPDFOperater().beginText()
        textobject.setTextOrigin(reportlabLibs.inch, 11 * reportlabLibs.inch)
        textobject.textLine(u'Google Custom Search Engine Results')
        self.getPDFOperater().drawText(textobject)

        for i, cseResultItem in enumerate(cseResultList):
            self.__drawTable(i, cseResultItem)

        self.getPDFOperater().save()