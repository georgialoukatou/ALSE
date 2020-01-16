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

########FUNCTIONS

#Select train files and raise RuntimeError if not
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



#######INTRODUCTION
def showinstructions(string, waittime):
    instructions1=visual.TextStim(win, text=string)
    instructions1.draw()
    win.flip()
    core.wait(waittime)
    clock = core.Clock()
    key = get_keypress()
    stoporcontinue(key)

text1="Bienvenue a cette experience!"
text1_="Dorenavant, appuyes sur ESPACE pour continuer, ou sur ECHAPPER pour quitter."
text2="Tu vas entendre des phrases a une langue unconnue." +"\n"+ "Chaque phrase decrit ce que les animaux font dans l'ecran, quand tu l'entends."
text2_="Merci de faire attention, il y  aura bientot  un test sur tes connaissances sur la langue."
text3="Appuyes sur ESPACE  pour commencer l'apprentissage, et appuyes sur ESPACE chaque fois que tu veux entendre une nouvelle phrase."
showinstructions(text1, 0.5)
showinstructions(text1_, 0.5)
showinstructions(text2, 0.5)
showinstructions(text2_, 0.5)
showinstructions(text3, 0.5)

########TRAINING
random.shuffle(video_list)
for i, video in enumerate(video_list): 
    videoname=str(video).replace("/Users/admin/Documents/artificialLanguageSegmentation/pilot5/new/", "").replace(".mov","")
    print(videoname)
    key = get_keypress()
    stoporcontinue(key)
    fixation.draw()
    win.update()
    core.wait(0.5)
    mov = visual.MovieStim(win, video,flipVert=False, flipHoriz=False)
    nextFlip=win.getFutureFlipTime(clock='ptb')
    while mov.status != visual.FINISHED:
        mov.draw()
        win.flip()

        
#########TEST
win.flip()
core.wait(2)

text4="Maintenant, tu vas entendre DEUX choses."
text4_="Attention, tu vas les entendre juste une fois!"
text5="Quel son va mieux a la langue que tu viens d'entendre?"
text5_="N'y penses pas trop et suis ton instinct!"
text6="Appuyes A si tu penses que le premier son (son 1 ) va mieux a la langue que tu viens d'entendre, et L si tu penses que le deuxieme son (son  2) lui va mieux."
showinstructions(text4, 0.5)
showinstructions(text4_, 0.5)
showinstructions(text5, 0.5)
showinstructions(text5_, 0.5)
showinstructions(text6, 0.5)

win.flip()
core.wait(2)


def presentest(testlist):
 clock0=core.Clock()
 soundNumber=0
 for soun in testlist:
            soundNumber=soundNumber+1
            aud =sound.Sound(soun)
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
            print(onset)
            aud.play(when=nextFlip)
            win.flip()
            print("clock0 after playing" + str(soundNumber))
            onset.append(clock3.getTime())
            print(clock0.getTime())
            if soundNumber <len(testlist):
                core.wait(1)
            else:
                core.wait(0.5)


def trackanswers(testlist):
 results=[]
 clock1 = core.Clock()
 allKeys=event.waitKeys(keyList=["a", "l", "q"], timeStamped=clock1)
 print("clock1 while pressing keys")
 onset.append(allKeys)
 print(onset)
 thisResp=""
 for thisKey in allKeys:
        if thisKey[0]=="a":
            if "c_" in testlist[0]:
              thisResp ="correct" 
              results.append([uniqueid, group, numberoftrial, dt_string, thisResp, testlist])
            else:
              thisResp = "wrong"
              results.append([uniqueid, group, numberoftrial, dt_string, thisResp, testlist])
        elif thisKey[0]=="l":
            if "c_" in testlist[1]:
              thisResp="correct"
              results.append([uniqueid, group, numberoftrial,  dt_string, thisResp, testlist])
            else:
              thisResp = "wrong"
              results.append([uniqueid, group, numberoftrial, dt_string,  thisResp, testlist])
        elif thisKey in ['Esc', 'escape']:         
            event.clearEvents()
        elif thisKey=='p':
            presentest(testlist)
            trackanswers(testlist)
 return(results)


#########TEST TRIALS
numberoftrial=0
for trial in alltesttrials:
    numberoftrial=numberoftrial+1
    onset=[]
    clock3=core.Clock()
    onset.append(clock3.getTime())
    print("clock3 before stimuli function:")
    print(onset)
    presentest(trial)
    win.flip()
    print("clock3 before tracking answer")
    onset.append(clock3.getTime())
    print(onset)
    answer=trackanswers(trial)
    onset.append(clock3.getTime())
    print("clock3 after tracking answer")
    print(onset)
    #sum=float(onset[3][0][1]) + float(onset[2])
    #onset[3]=sum
    tosave=([answer,onset])
    tosave=str(tosave).replace("[", "").replace("]", "")
    listanswer=tosave.split(",")
    datafile.writerow(listanswer)
    core.wait(1)


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

#Attribute  identifier to subject
#for x in range(1):
#  uniqueid=random.randint(1,1000)
"""
