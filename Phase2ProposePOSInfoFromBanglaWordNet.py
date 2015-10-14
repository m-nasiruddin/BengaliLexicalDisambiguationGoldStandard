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

source_corpus = codecs.open('GS_for_Bangla/text-all/annotator-3/text-all.utf-8.uni.pun.sen.tok.mul.lem.xml', 'r', 'utf-8')
# source corpus path
read_corpus = source_corpus.readlines()  # read the entire corpus at once
target_file = codecs.open('GS_for_Bangla/text-all/annotator-3/text-all.utf-8.uni.pun.sen.tok.mul.pos.xml', 'w+')
for corpus_entry in read_corpus:
    #print(corpus_entry)
    begining_xml_tags = corpus_entry.split('" pos="')[:1]
    for begining_xml_tag in begining_xml_tags:
        target_file.write(begining_xml_tag.encode('utf-8'))
    xml_tags = corpus_entry.split('lemma="')[1:]
    for begining_xml_tag in xml_tags:
        lemmas = begining_xml_tag.split('" pos="')[:1]

        for lemma in lemmas:
            target_file.write('" pos="')
            temp_list = []
            for i in range(0, len(wordnet), 5):
                if wordnet[i+4] == lemma:
                    if wordnet[i+1] not in temp_list:
                        temp_list.append(wordnet[i+1])
                        for pos in wordnet[i+1]:
                            target_file.write(pos.strip() + '/')
            temp_list = []

    ending_xml_tags = corpus_entry.split('" pos="')[1:]
    for ending_xml_tag in ending_xml_tags:
        target_file.write(ending_xml_tag.encode('utf-8'))
target_file.close()