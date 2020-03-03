#!/bin/bash
RAW_FOLDERAUDIO="/Users/admin/Documents/artificialLanguageSegmentation-master/train_copie_2"
RAW_FOLDERVIDEO="/Users/admin/Documents/artificialLanguageSegmentation-master/videos"
RESULT_FOLDER="/Users/admin/Documents/artificialLanguageSegmentation-master/train_audiovideo"
RAW_FOLDERAUDIO1="/Users/admin/Documents/artificialLanguageSegmentation-master/train1"

i=0
for file in $RAW_FOLDERAUDIO/*
do
echo $file 
((i=i+1))
sox $file $RAW_FOLDERAUDIO1/$i.aiff pad 2 1  
done
