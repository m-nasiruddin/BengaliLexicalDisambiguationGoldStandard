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

# for wordnets in wordnet:
#     print(wordnets)

tree = etree.parse("GS_for_Bangla/text-all/annotator-1/1.text-all.utf-8.uni.pun.sen.tok.mul.lem.pos.xml")
for element in tree.xpath("/corpus/text/sentence/wf"):
    # print('L: ' + element.get('lemma'))
    # print(element.get('pos'))
    for i in range(0, len(wordnet), 5):
        # print(wordnet[i+0])
        # print(wordnet[i+2])
        if wordnet[i+0] == element.get('lemma') and wordnet[i+2] == element.get('pos'):
            print('/' + wordnet[i+3])
