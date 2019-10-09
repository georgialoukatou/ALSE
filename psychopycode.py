#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import psychtoolbox as ptb
from psychopy import visual, core, event, sound
import time, os
import csv

path_train_video="/Users/lscpuser/Documents/ALSE/pilot_train_video/"
path_train_audio="/Users/lscpuser/Documents/ALSE/pilot_train_audio/"

datafile = open("/Users/lscpuser/Desktop/datafile.csv", 'w')
test_file=['/Users/lscpuser/Documents/ALSE/pilot2alex/test1c.aiff', '/Users/lscpuser/Documents/ALSE/pilot2alex/test2f.aiff' ]


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


audio_file=list()
sound_list=list()
video_file=list()
video_list=list()

getfiles(path_train_audio, audio_file, sound_list)
getfiles(path_train_video, video_file, video_list)


#######TRAIN
fixation = visual.GratingStim(win=win, size=1.4, pos=[0,0], sf=0, rgb=-1)

for i, video in enumerate(video_list):
    for y, audio in enumerate(sound_list):
        if i==y:  ####match video to audio
            fixation.draw()
            win.update()
            core.wait(2.0) 
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
####question 
question = visual.TextStim(win, text="Which of the following two sounds is a unit in the language?")


question.draw()
win.flip()
core.wait(4)

#present stimuli
for soun in test_file:
            aud =sound.Sound(soun, secs=0.5)
            print(aud)
            nextFlip=win.getFutureFlipTime(clock='ptb')
            aud.play(when=nextFlip)
            win.flip()
            core.wait(3)


#record answer
win.flip()
allKeys=event.waitKeys()
thisResp=""
for thisKey in allKeys:
        if thisKey=='left':
            thisResp ="correct" # correct
            datafile.write(thisResp + ";")
        elif thisKey=='right':
            thisResp=="incorrect"
            datafile.write(thisResp + ";")
        elif thisKey in ['q', 'escape']:         
            event.clearEvents()
win.close()
core.quit()
