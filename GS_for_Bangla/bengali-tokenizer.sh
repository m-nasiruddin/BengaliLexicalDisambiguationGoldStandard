#---------------------------
# Command to run the script
# $ bash bn-script.sh [file name]
# e.g. $ bash bn-script.sh 2000.txt
#---------------------------

#!/bin/bash
# Unicode normalization
#python /Users/Mohammad/Documents/Dropbox/Language_Resources/Text_Normalization/Python\ Script/normalize.py $1 Norm.txt NFD
## Make punctuation normalization
#perl ../normalize-punctuation.pl < text-all.utf-8.uni.tok.txt > text-all.utf-8.uni.tok.pun.txt
# Make paragraphs into sentences (line by line)
#perl -pe 's/(((।|\?|!)(’|”|\)|\]))|(।|\?|!))/$1\n/g' < Norm.txt > Norm1.txt

# Seperating punctuations by spaces, with Dari (।) too and remove any middle, starting and ending whitespaces (tabs/spaces), and new lines
sed -E "s/([[:punct:]])/ \1 /g" < $1 > temp
# Remove any middle, starting and ending whitespaces (tabs/spaces), and new lines
sed 's/ \{1,\}/ /g; s/^ *//; s/ *$//; /^$/d' < temp > $1.tok.txt
# Remove files
rm temp
