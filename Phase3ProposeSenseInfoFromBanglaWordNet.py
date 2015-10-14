#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Mohammad'

import codecs

from lxml import etree

source_wordnet = codecs.open('finalbanglaset.syns', 'r', 'utf-8')  # source corpus path
read_wordnet = source_wordnet.readlines()  # read the entire wordnet at once
synset_ids = []  # for storing synset ids
pos_tags = []  # for storing pos tags
definitions = []  # for storing definitions
examples = []  # for storing examples
wordnet = []  # for storing the entire wordnet
for line in read_wordnet:
    synset_ids.extend(line.split('ID			:: ')[1:])  # divide each entry by 'ID			:: ' and store synset ids
    pos_tags.extend(line.split('CAT			:: ')[1:])  # divide each entry by 'CAT			:: ' and store pos tags
    definitions.extend(line.split('CONCEPT		:: ')[1:])  # divide each entry by 'CONCEPT		:: ' and store definitions
    examples.extend(line.split('EXAMPLE		:: ')[1:])  # divide each entry by 'EXAMPLE		:: ' and store examples
    synsets = line.split('SYNSET-BENGALI	:: ')[1:]  # divide each entry by 'SYNSET-BENGALI	:: ' and store synsets
    for synset in synsets:
        lemmas = synset.split(',')
        for lemma in lemmas:
            wordnet.append(lemma.strip())
            # print(word)
            for synset_id in synset_ids:
                wordnet.append(synset_id.strip())
            for pos_tag in pos_tags:
                wordnet.append(pos_tag.strip())
            for definition in definitions:
                wordnet.append(definition.strip())
            for example in examples:
                striped_example = example.strip()
                wordnet.append(striped_example.strip('"'))
        synset_ids = []
        pos_tags = []
        definitions = []
        examples = []

tree = etree.parse('GS_for_Bangla/text-all/annotator-2/2.text-all.utf-8.uni.pun.sen.tok.mul.lem.pos.xml')
# source corpus path
target_file = codecs.open('GS_for_Bangla/text-all/annotator-2/2.text-all.utf-8.uni.pun.sen.tok.mul.lem.pos.sen.xml', 'w+')
for element in tree.xpath("/corpus/text/sentence/wf"):
    temp_list = []
    for i in range(0, len(wordnet), 5):
        if wordnet[i+0] == element.get('lemma') and wordnet[i+2] == element.get('pos'):
            if element.get('id') not in temp_list:
                target_file.write(element.get('id') + '\t' + element.get('id') + '\t')
                target_file.write('bwn:' + wordnet[i+1].zfill(5).encode('utf-8') + '[' + wordnet[i+3].encode('utf-8') + ' # ' + wordnet[i+4].encode('utf-8') + ']' + '\n')
                temp_list.append(element.get('id'))
            else:
                target_file.write('bwn:' + wordnet[i+1].zfill(5).encode('utf-8') + '[' + wordnet[i+3].encode('utf-8') + ' # ' + wordnet[i+4].encode('utf-8') + ']' + '\n')
    temp_list = []
target_file.close()
