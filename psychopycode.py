#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import datetime
import psychtoolbox as ptb
from psychopy import visual, core, event, sound
import time, os
import csv, random

group="groupA"

datafile = open("/Users/lscpuser/Desktop/datafile.csv", 'a')
datafile = csv.writer(datafile, delimiter=",")


path_test_audio="/Users/lscpuser/Documents/ALSE/pilot_test_audio/"+ str(group) + "/"
path_train_video="/Users/lscpuser/Documents/ALSE/new1/" + str(group) + "/"
path_train_audio="/Users/lscpuser/Documents/ALSE/a/"+str(group)+"/"



test_1=[path_test_audio + 'Atest1c_Verb0_ProgressiveY_Pluralverb.aiff', path_test_audio + 'Atest1f_Pluralnoun_Verb0_ProgressiveY.aiff' ]
test_2=[path_test_audio + 'Atest2c_Noun0_Singularnoun.aiff', path_test_audio + 'Atest2f_Singularnoun_Verb2_ProgressiveN.aiff' ]
test_3=[path_test_audio + 'Atest3f_Pluralnoun_1syllOFverb1.aiff', path_test_audio + 'Atest3c_ProgressiveY_PluralVerb.aiff' ]
test_4=[path_test_audio +  'Atest4c_Noun2_SingularNoun.aiff', path_test_audio + 'Atest4f_ProgressiveN_SingularVerb.aiff']
test_5=[path_test_audio + 'Atest11c_Verb3_ProgressiveN_Singularverb.aiff' , path_test_audio + 'Atest11f_Pluralnoun_Verb3_ProgressiveN.aiff']
test_6=[path_test_audio + 'Atest22f_Pluralnoun_Verb2_ProgressiveY.aiff', path_test_audio + 'Atest22c_Noun1_Pluralnoun.aiff']
test_7=[path_test_audio + 'Atest33c_ProgressiveN_SingularVerb.aiff', path_test_audio + 'Atest33f_SingularNoun_1syllOFverb0.aiff' ]
test_8=[path_test_audio + 'Atest44f_ProgressiveY_PluralVerb.aiff', path_test_audio + 'Atest44c_Noun2_PluralNoun.aiff']

win = visual.Window([1024, 768], mon ='SonyG500')


#####Select train files and raise RuntimeError if not
def getfiles(path, list, list2):
  items = [f for f in os.listdir(path) if os.path.isfile( os.path.join(path, f) )]
  for item in items:
    list.append(str(path)+str(item) )
  for  file in list:
   path = file
   path = os.path.join(os.getcwd(), path)
   if not os.path.exists(path):
       raise RuntimeError("File could not be found:" + path)
   list2.append(path)




def presstocontinue():
    clock = core.Clock()
    allKeys=event.waitKeys(keyList=["space","q"], timeStamped=clock)
    for thisKey in allKeys:
        print(thisKey)
        if thisKey=="space":
           continue
        if thisKey=="q":
            print(thisKey)
            win.close()
            core.quit()

audio_file=list()
sound_list=list()
video_file=list()
video_list=list()

getfiles(path_train_audio, audio_file, sound_list)
getfiles(path_train_video, video_file, video_list)

print(video_list)
print(sound_list)

#Attribute  identifier to subject
import random
for x in range(1):
  uniqueid=random.randint(1,1000)
# datetime object containing current date and time


now = datetime.now() 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
print("date and time =", dt_string)

#######TRAIN
fixation = visual.GratingStim(win=win, size=2, pos=[0,0], sf=0, rgb=-1)
instructions1=visual.TextStim(win, text="Hi! Welcome to this experiment."+ "\n" + "From now on, you will have to press space to continue, or q if you want to quit")
instructions1.draw()
win.flip()
core.wait(0.5)
presstocontinue()

instructions2=visual.TextStim(win, text="You are going to hear sentences in a language you don't know." +"\n"+ "The sentences decsribe actions done by animals on screen."  )
instructions2.draw()
win.flip()
core.wait(0.5)
presstocontinue()

instructions3=visual.TextStim(win, text="Please pay attention, there will soon be a test on your knowledge on the language."  +"\n"+ "Please press q, or any other key to start the training phase.")
instructions3.draw()
win.flip()
core.wait(0.5)
presstocontinue()

random.shuffle(video_list)
random.shuffle(sound_list)
for i, video in enumerate(video_list): 
    videoname=str(video).replace("/Users/lscpuser/Documents/ALSE/new1/", "").replace(".mov","")
    print(videoname)
    for y, audio in enumerate(sound_list):
        audioname=str(audio).replace("/Users/lscpuser/Documents/ALSE/a/", "").replace(".aiff","")
        print(audioname)
        if videoname==audioname:  ####match video to audio
            presstocontinue()
            print(video,audio)
            fixation.draw()
            win.update()
            core.wait(0.5) 
            mov = visual.MovieStim2(win, video, size=640,pos=[0, 100],flipVert=False, flipHoriz=False,loop=False, noAudio=True)
            shouldflip = mov.play() ####playvideo+audio
            nextFlip=win.getFutureFlipTime(clock='ptb')
            audio=sound.Sound(audio, secs=0.5) 
            audio.play(when=nextFlip)
            while mov.status != visual.FINISHED:
                if shouldflip:     
                    win.flip()
                else:
                    time.sleep(0.001)
                shouldflip = mov.draw()


            


win.flip()


#######TEST
testid=[]
def presentest(testlist):
 clock0=core.Clock()
 soundNumber=0
 for soun in testlist:
            soundNumber=soundNumber+1
            aud =sound.Sound(soun)
            print(aud)
            print(soundNumber)
            if soundNumber==1:
               teststim=visual.TextStim(win, text=soundNumber, pos=(-0.5,0.2))
               teststim.draw()
            elif soundNumber ==2:
               teststim=visual.TextStim(win, text=soundNumber, pos=(0.5,0.2))
               teststim.draw()
            #core.wait(1)
            nextFlip=win.getFutureFlipTime(clock='ptb')           
            print("clock0 before playing"+ str(soundNumber))
            onset.append(clock0.getTime())
            aud.play(when=nextFlip)
            print("clock0 after playing" + str(soundNumber))
            print(clock0.getTime())
            win.flip()
            #if soundNumber <len(testlist):
            core.wait(1)

def trackanswers(testlist):
 results=[]
 clock1 = core.Clock()
 allKeys=event.waitKeys(keyList=["left", "right", "q"], timeStamped=clock1)
 print("clock1 after pressing")
 onset.append(allKeys)
 thisResp=""
 for thisKey in allKeys:
        if thisKey[0]=='left':
            if "c_" in testlist[0]:
              thisResp ="correct" # correct
#             datafile.writerow([uniqueid, dt_string, thisResp, testlist, thisKey])
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
            else:
              thisResp = "wrong"
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
        elif thisKey[0]=='right':
            if "c_" in testlist[1]:
              thisResp="correct"
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
            else:
              thisResp = "wrong"
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
        elif thisKey in ['q', 'escape']:         
            event.clearEvents()
        elif thisKey=='p':
            presentest(testlist)
            trackanswers(testlist)
 return(results)


####question 

core.wait(2)
instructions4 = visual.TextStim(win, text="Now, you are going to hear two things." + "\n"  + "You will hear each thing only once." )
instructions4.draw()
win.flip()
core.wait(0.5)
presstocontinue()

instructions5 = visual.TextStim(win, text="Which one sounds better for the language you just heard?" + "\n"+"Press A for 1 and B for 2."+ "Don't overthink it and go with your gut." )
instructions5.draw()
win.flip()
core.wait(0.5)
presstocontinue()

#present stimuli 1
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_1)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_1)
print("clock3 after collecting")
print(clock3.getTime())



sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])


#present  stimuli 2
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_2)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_2)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])

#present stimuli 3
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_3)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_3)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])



#present stimuli 4
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_4)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_4)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])

#present stimuli 5
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_5)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_5)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])



#present stimuli 6
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_6)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_6)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])

#present stimuli 7
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_7)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_7)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])


#present stimuli 8
onset=[]
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
print("start clock3")
clock3=core.Clock()
presentest(test_8)
#record answer
win.flip()
print("clock3 after presenting and before collecting")
onset.append(clock3.getTime())
answer=trackanswers(test_8)
print("clock3 after collecting")
print(clock3.getTime())

sum=float(onset[3][0][1]) + float(onset[2])
onset[3]=sum
datafile.writerow([answer, onset])
"""
#present stimuli 4
question = visual.TextStim(win, text="")
question.draw()
win.flip()
core.wait(2)
presentest(test_4)
#record answer
win.flip()
trackanswers(test_4)

"""
fixation = visual.GratingStim(win=win, size=2, pos=[0,0], sf=0, rgb=-1)
instructionslast=visual.TextStim(win, text="Thank you! You can now call the experimenter.")
instructionslast.draw()
win.flip()
core.wait(0.5)
presstocontinue()
win.close()
core.quit()
