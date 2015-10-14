#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Mohammad'

import codecs
from lxml import etree

source_wordnet = codecs.open('finalbanglaset.syns', 'r', 'utf-8')  # source corpus path
read_wordnet = source_wordnet.readlines()  # read the entire wordnet at once
wordnet = []
synset_id = []
pos_tag = []
definition = []
gloss = []
for entry in read_wordnet:
    synset_id += entry.split('ID			:: ')[1:]
    pos_tag += entry.split('CAT			:: ')[1:]
    definition += entry.split('CONCEPT		:: ')[1:]
    gloss += entry.split('EXAMPLE		:: ')[1:]
    synset = entry.split('SYNSET-BENGALI	:: ')[1:]
    for word in synset:
        words = word.split(',')
        for word in words:
            #print(word)
            wordnet.append(synset_id)
            wordnet.append(pos_tag)
            wordnet.append(definition)
            wordnet.append(gloss)
            wordnet.append(word.strip())
        synset_id = []
        pos_tag = []
        definition = []
        gloss = []

temp_list = []
tree = etree.parse("GS_for_Bangla/text-all/annotator-1/1.text-all.utf-8.uni.pun.sen.tok.mul.lem.xml")
for element in tree.xpath("/corpus/text/sentence/wf"):
    print(element.get('lemma'))
    print(element.get('pos'))
    for i in range(0, len(wordnet), 5):
        if wordnet[i+4] == element.get('lemma'):
            if wordnet[i+1] not in temp_list:
                temp_list.append(wordnet[i+1])
                print('/' + str(wordnet[i+1]))
    temp_list = []
