#-----------
# place this file before the directory for which files it will do the statistics.
# e.g. if your text files are in the "new_folder/old_folder", place this file in "new_folder"
# bash corpus-statistics.sh [folder_name]
#-----------
#!/bin/bash
printf "\nSentences\tTokens\tCharacters\tFiles\n-----\t------\t----------\t-----\n"
wc $1/*

cd $1

printf "\nTypes\n-----\n"
for f in *
do
	echo "File - "$f""
	for token in $(cat $f)
	do
    	echo "$token"
	done | sort -u | wc -l
done

echo "Folder - "$1""
for token in $(cat *)
do
	echo "$token"
done | sort -u | wc -l
printf "\n"

printf "\nWords\n-----\n"
for f in *
do
	echo "File - "$f""
	for word in $(cat $f)
	do
    	echo "$word"
	done | tr " " "\n" | tr -d "[:punct:]" | tr -d "[০-৯]" | tr "[:upper:]" "[:lower:]" | tr -s "\n" | sort -u | wc -l
done

echo "Folder - "$1""
for word in $(cat *)
do
	echo "$word"
done | tr " " "\n" | tr -d "[:punct:]" | tr -d "[০-৯]" | tr "[:upper:]" "[:lower:]" | tr -s "\n" | sort -u | wc -l
printf "\n"