#!/bin#!/bin/bash
RAW_FOLDERAUDIO="/Users/admin/Documents/datafiles/final1/trainsounds1/A"
RAW_FOLDERVIDEO="/Users/admin/Documents/datafiles/final1/videos1"
RESULT_FOLDER="/Users/admin/Documents/datafiles/final1/trainvideostest2/A"


#
#ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/1_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/2_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4 -itsoffset 00:00:03.0 -i $RAW_FOLDERAUDIO/3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4
ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/3_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/4_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/5_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/5_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/1_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/5_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/6_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/6_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/6_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/6_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/7_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/7_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/7_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/7_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/8_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/8_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/8_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/8_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/9_*2.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/10_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4 -i $RAW_FOLDERAUDIO/11_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4 -itsoffset 00:00:02.0  -i $RAW_FOLDERAUDIO/12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/12_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/13_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/13_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/13_*2.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/13_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
"""

#ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/14_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/14_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/14_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/14_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/15_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/15_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/15_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/15_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/16_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/16_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/16_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/16_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/17_*.aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/18_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/19_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/20_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/21_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/22_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/23_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/24_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/25_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/25_Catwalk_25_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/25_*.aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/25_Catwalk_25_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/26_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/26_Catwalking_26_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/26_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/26_Catwalking_26_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/27_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/27_2catwalk_27_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/27_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/27_2catwalk_27_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/28_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/28_2catwalking_28_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/28_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/28_2catwalking_28_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/29_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/29_Catjumping_29_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/29_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/29_Catjumping_29_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/30_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/30_2catjumping_30_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/30_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/30_2catjumping_30_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/31_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/31_Catflip_31_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/31_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/31_Catflip_31_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/32_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/32_2catflip_32_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/32_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/32_2catflip_32_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


###########Disrupter 1 ######################################################################################


#ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/33_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/33_Dogwalk_33_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/33_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/33_Dogwalk_33_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov




#ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/34_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/34_Dogwalking_34_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/34_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/34_Dogwalking_34_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov




#ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/35_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/35_Dogjumping_35_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/35_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/35_Dogjumping_35_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov




#ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/36_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/36_Dogflip_36_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/36_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/36_Dogflip_36_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/37_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/37_Dogwalk_37_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/37_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/37_Dogwalk_37_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/38_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/38_Dogwalking_38_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/38_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/38_Dogwalking_38_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov




#ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/39_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/39_Dogjumping_39_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/39_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/39_Dogjumping_39_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov




#ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/40_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/40_Dogflip_40_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/40_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/40_Dogflip_40_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


"""

#ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/41_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/41_2sheepjumping_41_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/41_*2.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/41_2sheepjumping_41_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/42_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/42_2sheepflip_42_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/42_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/42_2sheepflip_42_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/43_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/43_2sheepwalking_43_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/43_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/43_2sheepwalking_43_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/44_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/44_2sheepwalk_44_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/44_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/44_2sheepwalk_44_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/45_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/45_2sheepjumping_45_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/45_*2.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/45_2sheepjumping_45_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/46_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/46_2sheepflip_46_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/46_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/46_2sheepflip_46_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/47_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/47_2sheepwalking_47_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/47_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/47_2sheepwalking_47_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/48_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/48_2sheepwalk_48_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/48_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/48_2sheepwalk_48_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/49_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/49_Catwalk_49_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/49_*.aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/49_Catwalk_49_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/50_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/50_Catwalking_50_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/50_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/50_Catwalking_50_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/51_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/51_2catwalk_51_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/51_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/51_2catwalk_51_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/52_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/52_2catwalking_52_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/52_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/52_2catwalking_52_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/53_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/53_Catjumping_53_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/53_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/53_Catjumping_53_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov



#ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/54_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/54_2catjumping_54_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/54_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/54_2catjumping_54_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/55_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/55_Catflip_55_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/55_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/55_Catflip_55_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov

#ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/56_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/56_2catflip_56_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/56_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/56_2catflip_56_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/57_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/57_Catwalk_57_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/57_*.aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/57_Catwalk_57_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/58_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/58_Catwalking_58_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/58_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/58_Catwalking_58_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/59_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/59_2catwalk_59_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/59_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/59_2catwalk_59_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mov


#ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/60_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/60_2catwalking_60_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov#
ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/60_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/60_2catwalking_60_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mov


ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/61_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/61_Catjumping_61_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mov



ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/62_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/62_2catjumping_62_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mov

ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/63_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/63_Catflip_63_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mov
ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/64_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/64_2catflip_64_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mov
###########Disrupter 2 ######################################################################################


ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/65_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/65_Dogwalk_65_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/66_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/66_Dogwalking_66_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/67_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/67_Dogjumping_67_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/68_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/68_Dogflip_68_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov

ffmpeg -i $RAW_FOLDERVIDEO/1_Dogwalk_1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/69_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/69_Dogwalk_69_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/2_Dogwalking_2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/70_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/70_Dogwalking_70_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/3_Dogjumping_3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/71_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/71_Dogjumping_71_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/4_Dogflip_4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/72_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/72_Dogflip_72_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov


ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/73_*2.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/73_2sheepjumping_73_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1].mov


ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/74_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/74_2sheepflip_74_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/75_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/75_2sheepwalking_75_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/76_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/76_2sheepwalk_76_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1].mov


ffmpeg -i $RAW_FOLDERVIDEO/9_2sheepjumping_9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/77_*2.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/77_2sheepjumping_77_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1].mov


ffmpeg -i $RAW_FOLDERVIDEO/10_2sheepflip_10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/78_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/78_2sheepflip_78_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/11_2sheepwalking_11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4  -i $RAW_FOLDERAUDIO/79_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/79_2sheepwalking_79_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/12_2sheepwalk_12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/80_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/80_2sheepwalk_80_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1].mov



ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/81_*.aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/81_Catwalk_81_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/82_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/82_Catwalking_82_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/83_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/83_2catwalk_83_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/84_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/84_2catwalking_84_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1].mov

ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/85_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/85_Catjumping_85_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/86_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/86_2catjumping_86_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/87_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/87_Catflip_87_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/88_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/88_2catflip_88_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1].mov


ffmpeg -i $RAW_FOLDERVIDEO/17_Catwalk_17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/89_*.aiff   -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/89_Catwalk_89_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/18_Catwalking_18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/90_*.aiff  -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/90_Catwalking_90_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/19_2catwalk_19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/91_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/91_2catwalk_91_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/20_2catwalking_20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/92_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/92_2catwalking_92_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1].mov

ffmpeg -i $RAW_FOLDERVIDEO/21_Catjumping_21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/93_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/93_Catjumping_93_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/22_2catjumping_22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/94_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/94_2catjumping_94_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/23_Catflip_23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/95_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/95_Catflip_95_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1].mov
ffmpeg -i $RAW_FOLDERVIDEO/24_2catflip_24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0].mp4   -i $RAW_FOLDERAUDIO/96_*.aiff -map 0:0 -map 1:0 -c:v copy -c:a copy $RESULT_FOLDER/96_2catflip_96_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1].mov


