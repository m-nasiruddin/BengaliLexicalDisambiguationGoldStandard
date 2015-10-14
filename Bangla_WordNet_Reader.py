# -*- coding: utf-8 -*-
__author__ = 'Mohammad'

import codecs
from collections import Counter

source_wordnet = codecs.open('finalbanglaset.syns', 'r', 'utf-8')  # source corpus path
read_wordnet = source_wordnet.readlines()  # read the entire wordnet at once

# synset_ids_list = []
# pos_tags_list = []
# definitions_list = []
# glosses_list = []
# synsets_list = []
#
# synset_words_list = []
#
# for entry in read_wordnet:
#     synset_ids_list += entry.split('ID			:: ')[1:]
#     pos_tags_list += entry.split('CAT			:: ')[1:]
#     definitions_list += entry.split('CONCEPT		:: ')[1:]
#     glosses_list += entry.split('EXAMPLE		:: ')[1:]
#     synsets_list += entry.split('SYNSET-BENGALI	:: ')[1:]

# ## total element count in wordnet
# print('synset_ids:\t' + str(len(synset_ids_list)))  # result: 36238
# print('pos_tags_list:\t' + str(len(pos_tags_list)))  # result: 36240
# print('definitions_list:\t' + str(len(definitions_list)))  # result: 36239
# print('glosses_list:\t' + str(len(glosses_list)))  # result: 36240
# print('synsets_list:\t' + str(len(synsets_list)))  # result: 36239
# ## counts pos tags
# print(Counter(pos_tags_list))  # NOUN: 27178, ADJECTIVE: 5813, VERB: 2804, ADVERB: 445, total: 36240

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
            #print(wo)
            wordnet.append(synset_id)
            wordnet.append(pos_tag)
            wordnet.append(definition)
            wordnet.append(gloss)
            wordnet.append(word.strip())
        synset_id = []
        pos_tag = []
        definition = []
        gloss = []

# for entry in wordnet:
#     print(entry)

# myDict = {}
# linenum = 0
# for line in read_wordnet:
#     striped_line = line.strip()
#     synset_ids = striped_line.split('ID			:: ')[1:]
#     for synset_id in synset_ids:
#         striped_synset_id = synset_id.strip()
#         if striped_synset_id not in myDict:
#             myDict[striped_synset_id] = []
#     pos_tags = striped_line.split('CAT			:: ')[1:]
#     for pos_tag in pos_tags:
#         myDict[striped_synset_id].append(pos_tag)
#     definitions = striped_line.split('CONCEPT		:: ')[1:]
#     for definition in definitions:
#         myDict[striped_synset_id].append(definition)
#     glosses = striped_line.split('EXAMPLE		:: ')[1:]
#     for glosse in glosses:
#         myDict[striped_synset_id].append(glosse)
#     synsets = striped_line.split('SYNSET-BENGALI	:: ')[1:]
#     for synset in synsets:
#         myDict[striped_synset_id].append(synset)

# wordnet_entries = {}
# key = 0
# for id, value in myDict.items():
#     key += 1
#     if key not in wordnet_entries:
#         wordnet_entries[key] = []
#     wordnet_entries[key].append(id)
#     wordnet_entries[key].append(value[0])
#     wordnet_entries[key].append(value[1])
#     wordnet_entries[key].append(value[2])
#     wordnet_entries[key].append(value[3])
#     words = value[3].split(',')
#     for word in words:
#         striped_word = word.strip()
#        print(striped_word)

# for key in wordnet_entries:
#     print('%-15s %5d: %s' % (key, len(wordnet_entries[key]), wordnet_entries[key]))

# for key in myDict.keys():
#   print (key, myDict[key[3]])

# for key in myDict:
#     val = '%('+key+')s'
#     print key, val % myDict

# for value in myDict.values():
#     words = value[3].split(',')
#     print(words)
#     for word in words:
#         striped_word = word.strip()
#         print(striped_word)

# for key in myDict:
#     #print('%-15s %5d: %s' % (key, len(myDict[key]), myDict[key]))
#     if len(myDict[key]) > 4:
#         print(key)

## for reading synset ids
# for word in synset_ids_list:
#     print(word.strip())

## for reading pos tags
# for word in pos_tags_list:
#     if word.strip() == 'NOUN':
#         print('N')
#     if word.strip() == 'VERB':
#         print('V')
#     if word.strip() == 'ADJECTIVE':
#         print('J')
#     else:
#         print('A')

## for reading bangla synsets, spliting them by comma (,),
# for synset in synsets_list:
#     synset_words = synset.split(',')
#     synset_words_list += synset_words
# for word in synset_words_list:
#     print(word.strip())


source_corpus = codecs.open('text-all.utf-8.uni.pun.sen.txt', 'r', 'utf-8')  # source corpus path
read_corpus = source_corpus.readlines()  # read the entire corpus at once

temp_list = []

output_file = codecs.open('output.txt', 'w', 'utf-8')  # output corpus path
## for reading a corpus and tokenizing by space
for line in read_corpus:
    striped_line = line.strip()
    words = striped_line.split()
    output_file.write('\n')
    for word in words:
        striped_word = word.strip()
        output_file.write('\t' + striped_word)
        for i in range(0, len(wordnet), 5):
            if wordnet[i+4] == striped_word:
                if wordnet[i+1] not in temp_list:
                    temp_list.append(wordnet[i+1])
                    output_file.write('/' + str(wordnet[i+1]))
        temp_list = []
output_file.close()