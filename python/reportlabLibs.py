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
# Time: 4:07 PM

from reportlab.pdfgen import canvas

#----------------------------------for chinse font and break line start--------------------
import reportlab.rl_config
from reportlab.lib.units import inch

reportlab.rl_config.warnOnMissingFontGlyphs = 0
import reportlab.pdfbase.pdfmetrics
import reportlab.pdfbase.ttfonts

reportlab.pdfbase.pdfmetrics.registerFont(
    reportlab.pdfbase.ttfonts.TTFont('song', '/Library/Fonts/Microsoft/SimSun.ttf'))
import reportlab.lib.fonts

reportlab.lib.fonts.ps2tt = lambda psfn: ('song', 0, 0)
reportlab.lib.fonts.tt2ps = lambda fn, b, i: 'song'

## for CJK Wrap
import reportlab.platypus


def wrap(self, availWidth, availHeight):
    # work out widths array for breaking
    self.width = availWidth
    leftIndent = self.style.leftIndent
    first_line_width = availWidth - (leftIndent + self.style.firstLineIndent) - self.style.rightIndent
    later_widths = availWidth - leftIndent - self.style.rightIndent
    try:
        self.blPara = self.breakLinesCJK([first_line_width, later_widths])
    except:
        self.blPara = self.breakLines([first_line_width, later_widths])
    self.height = len(self.blPara.lines) * self.style.leading
    return (self.width, self.height)


reportlab.platypus.Paragraph.wrap = wrap
#----------------------------------for chinse font and break line end----------------------

#----------------------------------for table start-----------------------------------------
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

width, height = A4
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER

tb_height = 5
tb_margin_v = 1
tb_numPerPage = 4
tb_firstItem_top = 7.6


def coord(x, y, unit=1):
    x, y = x * unit, height - y * unit
    return x, y

#----------------------------------for table end-------------------------------------------




