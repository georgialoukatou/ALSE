#!/usr/bin/env python
# coding: utf8

from datetime import datetime
#import psychtoolbox as ptb
from psychopy import visual, core, event, sound
import os,  csv, random
import pyglet
 
group="groupA"
uniqueid="1"

################### Variables
datafile = open("/Users/admin/Documents/artificialLanguageSegmentation/datafile.csv", 'a')
datafile = csv.writer(datafile, delimiter=",")
#register=str("uniqueid, group, numberoftrial, datetime, thisResp, stim1, stim2, clock3 before test function,clock0 before playing 1, clock0 after playing 1, clock0 before playing 2, clock0 after playing 2, clock 3 before tracking answer, thisKey, clock1 while pressing key, clock3 after tracking answer").split(",")
#datafile.writerow(register)
path_train_video="/Users/admin/Documents/artificialLanguageSegmentation/train_audiovideo/"
####path_train_video="/Users/admin/Documents/artificialLanguageSegmentation/pilot5/new/"


path_test_audio="/Users/admin/Documents/artificialLanguageSegmentation/test/"
test_1=[path_test_audio + 'Atest1c_Verb2_ProgressiveY_Pluralverb.aiff', path_test_audio + 'Atest1f_Pluralnoun_Verb2_ProgressiveY.aiff' ]
test_2=[path_test_audio + 'Atest2f_Singularnoun_Verb2.aiff', path_test_audio + 'Atest2c_Noun2_Singularnoun.aiff' ]
test_3=[path_test_audio + 'Atest3c_Verb0.aiff', path_test_audio + 'Atest3f_2ndofVerb1_ProgressiveY.aiff' ]
test_4=[path_test_audio + 'Atest4c_Noun1.aiff', path_test_audio + 'Atest4f_2ndofNoun1_Pluralnoun.aiff' ]
test_11=[path_test_audio +  'Atest11c_Verb2_ProgressiveY_Singularverb.aiff', path_test_audio + 'Atest11f_Singularnoun_Verb2_ProgressiveY.aiff']
test_22=[path_test_audio + 'Atest22f_Pluralnoun_Verb2.aiff', path_test_audio + 'Atest22c_Noun2_Pluralnoun.aiff' ]
test_33=[path_test_audio + 'Atest33f_2ndofVerb0_ProgressiveN.aiff', path_test_audio + 'Atest33c_Verb1.aiff' ]
test_44=[path_test_audio + 'Atest44c_Noun0.aiff', path_test_audio + 'Atest44f_2ndofNoun0_Singularnoun.aiff' ]
test_111=[path_test_audio + 'Atest111f_Noun1_Pluralnoun_Verb2.aiff', path_test_audio + 'Atest111c_Verb0_ProgressiveN_Singularverb.aiff' ]
test_222=[path_test_audio + 'Atest222c_Noun1_Pluralnoun.aiff', path_test_audio + 'Atest222f_Verb0_ProgressiveN.aiff' ]
test_333=[path_test_audio + 'Atest333c_Verb0.aiff', path_test_audio + 'Atest333f_2ndofNoun0_Singularnoun.aiff' ]
test_444=[path_test_audio + 'Atest444f_2ndofVerb1_ProgressiveY.aiff', path_test_audio + 'Atest444c_Noun1.aiff' ]
test_1111=[path_test_audio + 'Atest1111c_Verb1_ProgressiveY_Pluralverb.aiff', path_test_audio + 'Atest1111f_Noun0_Singularnoun_Verb2.aiff' ]
test_2222=[path_test_audio + 'Atest2222c_Noun0_Singularnoun.aiff', path_test_audio + 'Atest2222f_Verb1_ProgressiveY.aiff' ]
test_3333=[path_test_audio + 'Atest3333c_Verb1.aiff', path_test_audio + 'Atest3333f_2ndofNoun1_Pluralnoun.aiff' ]
test_4444=[path_test_audio + 'Atest4444f_2ndofVerb0_ProgressiveN.aiff', path_test_audio + 'Atest4444c_Noun0.aiff' ]
test_11111=[path_test_audio + 'Atest11111f_Pluralnoun_Verb2_ProgressiveN.aiff', path_test_audio + 'Atest11111c_Verb2_ProgressiveN_Pluralverb.aiff' ]
test_111111=[path_test_audio + 'Atest111111c_Verb2_ProgressiveN_Singularverb.aiff', path_test_audio + 'Atest111111f_Singularnoun_Verb2_ProgressiveN.aiff' ]




alltesttrials=[test_1, test_2, test_3, test_4, test_11, test_22, test_33, test_44, test_111, test_222, test_333, test_444, test_1111, test_2222, test_3333, test_4444, test_11111, test_111111]

###path_test_audio="/Users/admin/Documents/artificialLanguageSegmentation/pilot5/test_sample/"


win = visual.Window(fullscr="TRUE", size=(1440, 900))
#win = visual.Window(size=(1440, 900))
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
fixation=visual.GratingStim(win=win)

#getfiles(path_train_audio, audio_file, sound_list)
getfiles(path_train_video, video_file, video_list)
print(video_list)



#######INTRODUCTION
def showinstructions(string, waittime):
    instructions1=visual.TextStim(win, text=string, pos=[0,0],alignHoriz='center' )
    #instructions1.pos=(0,0)	
    instructions1.draw()
    win.flip()
    core.wait(waittime)
    clock = core.Clock()
    key = get_keypress()
    stoporcontinue(key)

text1=u"Bienvenue à cette expérience!"
text1_=u"A partir de maintenant, appuyez sur SPACE  pour continuer, ou sur ESC pour quitter."
text2=u"Vous entendrez plusieurs phrases dans une langue étrangère." +"\n"+ u"Chaque phrase décrit ce que les animaux font à l'écran."
text2_=u"Veuillez faire attention, il y aura bientôt un test sur votre connaissance de la langue."
text3=u"Appuyez sur SPACE pour démarrer la formation, et pour chaque fois que vous voulez entendre une nouvelle phrase."
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
    mov = visual.MovieStim2(win, video,flipVert=False, flipHoriz=False)
    nextFlip=win.getFutureFlipTime(clock='ptb')
    while mov.status != visual.FINISHED:
        mov.draw()
        win.flip()

        
#########TEST
win.flip()
core.wait(2)

text4=u"Vous allez maintenant entendre deux choses."
text4_=u"Attention, vous ne les entendrez qu'une seule fois!"
text5=u"Quelle chose sonne mieux pour la langue que vous venez d'entendre?"
text5_=u"Ne pas trop y penser et allez avec votre instinct!"
text6=u"Appuyez sur Q si vous pensez que le premier son va mieux avec la langue que vous venez d'entendre, et sur M si le second son va mieux."
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

text7=u"Merci d'avoir participé! Vous pouvez maintenant appeler l'expérimentateur."
showinstructions(text7, 0.5)

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
