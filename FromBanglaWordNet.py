#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Mohammad'

import codecs
from BeautifulSoup import BeautifulStoneSoup as Soup

# xml = """
# <TrdCaptRpt RptID="10000001" TransTyp="0">
#     <RptSide Side="1" Txt1="XXXXX">
#         <Pty ID="XXXXX" R="1"/>
#     </RptSide>
# </TrdCaptRpt>
# """

source_wordnet = codecs.open('finalbanglaset.syns', 'r', 'utf-8')  # source corpus path
read_wordnet = source_wordnet.readlines()  # read the entire wordnet at once

xml = codecs.open('GS_for_Bangla/text-all/annotator-1/1.text-all.utf-8.uni.pun.sen.tok.mul.lem.xml', 'r', 'utf-8')
#read_xml = source_wordnet.readlines()  # read the entire xml at once

soup = Soup(xml)
wf = soup.corpus.sentence.wf
wf['pos'] = 'Update'
#corpus.text['id'] = 'Updated'

print soup