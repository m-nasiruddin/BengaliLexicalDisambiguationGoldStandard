# -*- coding: utf-8 -*-
__author__ = 'Mohammad'

import codecs

source_corpus = codecs.open('GS_for_Bangla/text-all/annotator-2/text-all.utf-8.uni.pun.sen.tok.mul.txt', 'r', 'utf-8')
# source corpus path
read_corpus = source_corpus.read()  # read the entire corpus at once

target_file = codecs.open('GS_for_Bangla/text-all/annotator-2/text-all.utf-8.uni.pun.sen.tok.mul.xml', 'w+')
#  header
target_file.write('<?xml version="1.0" encoding="UTF-8" ?>\n'
                    '<!DOCTYPE corpus SYSTEM \"Bengali-all-words.dtd\">\n'
                    '<corpus lang=\"en\">\n'
                    '<text id="d001" source="">')
target_file.write('\n')
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
                            '">')
        target_file.write('\n')
        # for beginning of tokens
        tokens = sentence.split(' ')
        for token_index, token in enumerate(tokens, start=1):  # read the line word by word
            word = token.strip()
            target_file.write('   <wf id="d'+str(document_index).zfill(3) +
                                '.s'+str(sentence_index).zfill(3) +
                                '.t'+str(token_index).zfill(3) +
                                '" lemma=\"' +
                                word.encode('utf-8') +  # lemma
                                '\" pos=\"X\">' +
                                word.encode('utf-8') +  # pos
                                '</wf>')
            target_file.write('\n')
        # for ending of sentences
        target_file.write('  </sentence>')
        target_file.write('\n')
# footer
target_file.write('</text>\n'
                    '</corpus>')
target_file.close()
