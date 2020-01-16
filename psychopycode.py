#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import psychtoolbox as ptb
from psychopy import visual, core, event, sound
import os,  csv, random


group="groupA"
uniqueid="1"

################### Variables
datafile = open("/Users/admin/Documents/artificialLanguageSegmentation/datafile.csv", 'a')
datafile = csv.writer(datafile, delimiter=",")
#register=str("uniqueid, group, numberoftrial, datetime, thisResp, stim1, stim2, clock3 before test function,clock0 before playing 1, clock0 after playing 1, clock0 before playing 2, clock0 after playing 2, clock 3 before tracking answer, thisKey, clock1 while pressing key, clock3 after tracking answer").split(",")
#datafile.writerow(register)
path_train_video="/Users/admin/Documents/artificialLanguageSegmentation/pilot5/new/"

###
path_test_audio="/Users/admin/Documents/artificialLanguageSegmentation/pilot5/test_sample/"
test_1=[path_test_audio + 'Atest1f_Pluralnoun_Verb2_ProgressiveY.aiff', path_test_audio + 'Atest1c_Verb2_ProgressiveY_Pluralverb.aiff' ]
test_2=[path_test_audio + 'Atest2c_Noun2_Singularnoun.aiff', path_test_audio + 'Atest2f_Singularnoun_Verb2.aiff' ]
test_3=[path_test_audio + 'Atest3c_Verb0.aiff', path_test_audio + 'Atest3f_2ndofVerb0_ProgressiveN.aiff' ]
test_4=[path_test_audio +  'Atest4f_2ndofNoun1_Pluralnoun.aiff', path_test_audio + 'Atest4c_Noun1.aiff']
alltesttrials=[test_1, test_2]

###
win = visual.Window(fullscr="TRUE")
now = datetime.now() 
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")

#####################


###Select train files and raise RuntimeError if not
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

def get_keypress():
    keys = event.waitKeys()
    if keys:
        return keys[0]
    else:
        return None

def stoporcontinue(key):
 if key == 'space':
      pass
 elif key == 'escape':
      win.close()
      core.quit()

audio_file=list()
sound_list=list()
video_file=list()
video_list=list()

#getfiles(path_train_audio, audio_file, sound_list)
getfiles(path_train_video, video_file, video_list)
print(video_list)


"""
#Attribute  identifier to subject
import random
for x in range(1):
  uniqueid=random.randint(1,1000)
# datetime object containing current date and time


now = datetime.now() 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
print("date and time =", dt_string)
"""
#######TRAIN
#fixation = visual.GratingStim(win=win, size=2, pos=[0,0], sf=0, rgb=-1)
fixation = visual.GratingStim(win=win)
instructions1=visual.TextStim(win, text="Welcome to this experiment."+ "\n" + "From now on, press SPACE to continue, or ESC  to quit.")
instructions1.draw()
win.flip()
core.wait(0.5)
clock = core.Clock()
key = get_keypress()
stoporcontinue(key)


instructions2=visual.TextStim(win, text="You will hear sentences in an unknown language." +"\n"+ "The sentences decsribe what animals do on screen."  )
instructions2.draw()
win.flip()
core.wait(0.5)
clock = core.Clock()
key = get_keypress()
stoporcontinue(key)

instructions3=visual.TextStim(win, text="Please pay attention, there will soon be a test on your knowledge of the language."  +"\n"+ "Press SPACE to start the training phase.")
instructions3.draw()
win.flip()
core.wait(0.5)
clock = core.Clock()
key = get_keypress()
stoporcontinue(key)


mov = visual.MovieStim(myWin, 'A_Disrupter0_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0_2.mov', flipVert=False)
mov.draw()

y=0
random.shuffle(video_list)
for i, video in enumerate(video_list): 
#   y=y+1
#   if y <2:
    #videoname=str(video).replace("/Users/lscpuser/Documents/ALSE/pilot4/train_mov/"+ str(group) + "/", "").replace(".mov","")
    videoname=str(video).replace("/Users/admin/Documents/artificialLanguageSegmentation/pilot5/new/", "").replace(".mov","")
    print(videoname)
    key = get_keypress()
    stoporcontinue(key)
    fixation.draw()
    win.update()
    core.wait(0.5)
    mov = visual.MovieStim(win, video,flipVert=False, flipHoriz=False)
    shouldflip = mov.play() ####playvideo
    nextFlip=win.getFutureFlipTime(clock='ptb')
    while mov.status != visual.FINISHED:
        mov.draw()
        win.flip()
    #  if shouldflip:     
     #    win.flip()
      #else:
       #  time.sleep(0.001)
      #shouldflip = mov.draw()

print("hi")

            


win.flip()
"""

#######TEST

test_1=[path_test_audio + 'Atest1f_Pluralnoun_Verb2_ProgressiveY.aiff', path_test_audio + 'Atest1c_Verb2_ProgressiveY_Pluralverb.aiff' ]
test_2=[path_test_audio + 'Atest2c_Noun2_Singularnoun.aiff', path_test_audio + 'Atest2f_Singularnoun_Verb2.aiff' ]
test_3=[path_test_audio + 'Atest3c_Verb0.aiff', path_test_audio + 'Atest3f_2ndofVerb0_ProgressiveN.aiff' ]
test_4=[path_test_audio +  'Atest4f_2ndofNoun1_Pluralnoun.aiff', path_test_audio + 'Atest4c_Noun1.aiff']

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
            core.wait(0.5)
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
 allKeys=event.waitKeys(keyList=["a", "l", "q"], timeStamped=clock1)
 print("clock1 after pressing")
 onset.append(allKeys)
 thisResp=""
 for thisKey in allKeys:
        if thisKey[0]=="a":
            if "c_" in testlist[0]:
              thisResp ="correct" # correct
#             datafile.writerow([uniqueid, dt_string, thisResp, testlist, thisKey])
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
            else:
              thisResp = "wrong"
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
        elif thisKey[0]=="l":
            if "c_" in testlist[1]:
              thisResp="correct"
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
            else:
              thisResp = "wrong"
              results.append([uniqueid, dt_string, thisResp, testlist, thisKey])
        elif thisKey in ['Esc', 'escape']:         
            event.clearEvents()
        elif thisKey=='p':
            presentest(testlist)
            trackanswers(testlist)
 return(results)

"""
####question 
"""
core.wait(2)
instructions4 = visual.TextStim(win, text="Now, you are going to hear 2 things. You will hear them only once." )
instructions4.draw()
win.flip()
core.wait(0.5)
clock = core.Clock()
key = get_keypress()
stoporcontinue(key)

instructions5 = visual.TextStim(win, text="Which one sounds better for the language you just heard?" + "Don't overthink it and go with your gut." + "\n"+"Press A for 1 and L for 2." )
instructions5.draw()
win.flip()
core.wait(0.5)
clock = core.Clock()
key = get_keypress()
stoporcontinue(key)

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

instructions6=visual.TextStim(win, text="Please press space to continue the test phase and escape to quit")
instructions6.draw()
win.flip()
core.wait(0.5)
clock = core.Clock()
key = get_keypress()
stoporcontinue(key)


fixation = visual.GratingStim(win=win, size=2, pos=[0,0], sf=0, rgb=-1)
instructionslast=visual.TextStim(win, text="Thank you! You can now call the experimenter.")
instructionslast.draw()
win.flip()
core.wait(0.5)
presstocontinue()
win.close()
core.quit()

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


win.flip()



"""
"""
#random.shuffle(sound_list)
#for i, video in enumerate(video_list): 
#    videoname=str(video).replace("/Users/lscpuser/Documents/ALSE/new1/", "").replace(".mov","")
#    print(videoname)
#    for y, audio in enumerate(sound_list):
#        audioname=str(audio).replace("/Users/lscpuser/Documents/ALSE/a/", "").replace(".aiff","")
#        print(audioname)
#        if videoname==audioname:  ####match video to audio
#            presstocontinue()
#            print(video,audio)
#            fixation.draw()
#            win.update()
#            core.wait(0.5) 
#            mov = visual.MovieStim2(win, video, size=640,pos=[0, 100],flipVert=False, flipHoriz=False,loop=False, noAudio=True)
#            shouldflip = mov.play() ####playvideo+audio
#            nextFlip=win.getFutureFlipTime(clock='ptb')
#            audio=sound.Sound(audio, secs=0.5) 
#            audio.play(when=nextFlip)
#            while mov.status != visual.FINISHED:
#                if shouldflip:     
#                    win.flip()
#                else:
#                    time.sleep(0.001)
#                shouldflip = mov.draw()
"""
