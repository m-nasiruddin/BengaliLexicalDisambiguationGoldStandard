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

source_corpus = codecs.open('GS_for_Bangla/text-all/annotator-1/1.text-all.utf-8.uni.pun.sen.tok.mul.txt', 'r', 'utf-8')
# source corpus path
read_corpus = source_corpus.read()  # read the entire corpus at once
tree = etree.parse("GS_for_Bangla/text-all/annotator-1/1.text-all.utf-8.uni.pun.sen.tok.mul.lem.xml")
target_file = codecs.open('GS_for_Bangla/text-all/annotator-1/1.text-all.utf-8.uni.pun.sen.tok.mul.pos.xml', 'w+')
#  header
target_file.write('<?xml version="1.0" encoding="UTF-8" ?>\n'
                    '<!DOCTYPE corpus SYSTEM \"Bengali-all-words.dtd\">\n'
                    '<corpus lang=\"en\">\n'
                    '<text id="d001" source="">' + '\n')
documents = read_corpus.split('\n\n')  # split the corpus with double new line (for each document)
# for beginning of document
for document_index, document in enumerate(documents, start=1):  # read the corpus line by line
    sentences = document.split('\n')
    # for beginning of sentences
    for sentence_index, sentence in enumerate(sentences, start=1):  # read the corpus line by line
        target_file.write('  <sentence id="d' +
                            str(document_index).zfill(3) +
                            '.s' +
                            str(sentence_index).zfill(3) +
                            '">' + '\n')
        # for beginning of tokens
        tokens = sentence.split(' ')
        for token_index, token in enumerate(tokens, start=1):  # read the line word by word
            word = token.strip()
            target_file.write('   <wf id="d'+str(document_index).zfill(3) +
                                '.s'+str(sentence_index).zfill(3) +
                                '.t'+str(token_index).zfill(3) +
                                '" lemma=\"')
            # PROBLEM
            for element in tree.xpath("/corpus/text/sentence/wf"):
                target_file.write(element.get('lemma').encode('utf-8') +  # lemma.encode('utf-8') +  # lemma
                                '\" pos=\"' +
                                element.get('pos').encode('utf-8'))
                #
                temp_list = []
                for i in range(0, len(wordnet), 5):
                    if wordnet[i+4] == element.get('lemma'):
                        if wordnet[i+1] not in temp_list:
                            temp_list.append(wordnet[i+1])
                            #print('/' + str(wordnet[i+1]))
                            target_file.write('/' + str(wordnet[i+1]))  # word.encode('utf-8') +  # pos
                temp_list = []
                #
                target_file.write('\">' + word.encode('utf-8') + '</wf>\n')
        # for ending of sentences
        target_file.write('  </sentence>' + '\n')
# footer
target_file.write('</text>\n'
                    '</corpus>')
target_file.close()
