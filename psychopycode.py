#!/usr/bin/env python
# coding: utf8

from datetime import datetime
from psychopy import visual, core, event, sound
import os,  csv, random, sys
import pyglet

uniqueid=sys.argv[1] #subject initials 
group=sys.argv[2] #indicate which of the four groups the subject will be tested on


################### Registering files
datafile = open("/Users/admin/Documents/datafiles/" + str(uniqueid)   + "_data.csv", 'a')
datafile = csv.writer(datafile, delimiter=",")
register=str("uniqueid, group, numberoftrial, datetime, thisResp, stim1, stim2, 1.clock2 before presenttest function, 2.clock0 before playing 1, 3.clock0 after playing 1, 4.clock0 before playing 2, 5.clock0 after playing 2, 6.clock2 before trackanswer function, thisKey, 7.clock1 pressing key, 8.clock2 after trackanswer function").split(",")
datafile.writerow(register)

logfile = open("/Users/admin/Documents/datafiles/" + str(uniqueid)   + "_log.csv", 'a')
orig_stdout = sys.stdout
sys.stdout = logfile


#################  paths
path_train_video="/Users/admin/Documents/datafiles/final/trainvideos/"+ str(group)+ "/" 

path_test_audio="/Users/admin/Documents/datafiles/final/testsounds/"+ str(group)+ "/"


test_1=[path_test_audio + str(group) + 'test1c_Verb2_ProgressiveY_Pluralverb_sil.aiff', path_test_audio +  str(group) + 'test1f_Pluralnoun_Verb2_ProgressiveY_sil.aiff' ]
test_2=[path_test_audio + str(group) + 'test2f_Singularnoun_Verb2_sil.aiff', path_test_audio +  str(group) + 'test2c_Noun2_Singularnoun_sil.aiff' ]
test_3=[path_test_audio + str(group) + 'test3c_Verb0_sil.aiff', path_test_audio +  str(group) + 'test3f_2ndofVerb1_ProgressiveY_sil.aiff' ]
test_4=[path_test_audio + str(group) + 'test4c_Noun1_sil.aiff', path_test_audio + str(group) + 'test4f_2ndofNoun1_Pluralnoun_sil.aiff' ]
test_11=[path_test_audio + str(group) +  'test11c_Verb2_ProgressiveY_Singularverb_sil.aiff', path_test_audio + str(group) + 'test11f_Singularnoun_Verb2_ProgressiveY_sil.aiff']
test_22=[path_test_audio + str(group) + 'test22f_Pluralnoun_Verb2_sil.aiff', path_test_audio + str(group) + 'test22c_Noun2_Pluralnoun_sil.aiff' ]
test_33=[path_test_audio + str(group) + 'test33f_2ndofVerb0_ProgressiveN_sil.aiff', path_test_audio + str(group) + 'test33c_Verb1_sil.aiff' ]
test_44=[path_test_audio + str(group) + 'test44c_Noun0_sil.aiff', path_test_audio + str(group) + 'test44f_2ndofNoun0_Singularnoun_sil.aiff' ]
test_111=[path_test_audio + str(group) + 'test111f_Noun1_Pluralnoun_Verb2_sil.aiff', path_test_audio + str(group) + 'test111c_Verb0_ProgressiveN_Singularverb_sil.aiff' ]
test_222=[path_test_audio + str(group) + 'test222c_Noun1_Pluralnoun_sil.aiff', path_test_audio + str(group) + 'test222f_Verb0_ProgressiveN_sil.aiff' ]
test_333=[path_test_audio + str(group) + 'test333c_Verb0_sil.aiff', path_test_audio + str(group) + 'test333f_2ndofNoun0_Singularnoun_sil.aiff' ]
test_444=[path_test_audio + str(group) + 'test444f_2ndofVerb1_ProgressiveY_sil.aiff', path_test_audio + str(group) + 'test444c_Noun1_sil.aiff' ]
test_1111=[path_test_audio + str(group) + 'test1111c_Verb1_ProgressiveY_Pluralverb_sil.aiff', path_test_audio + str(group) + 'test1111f_Noun0_Singularnoun_Verb2_sil.aiff' ]
test_2222=[path_test_audio + str(group) + 'test2222c_Noun0_Singularnoun_sil.aiff', path_test_audio + str(group) + 'test2222f_Verb1_ProgressiveY_sil.aiff' ]
test_3333=[path_test_audio + str(group) + 'test3333c_Verb1_sil.aiff', path_test_audio + str(group) + 'test3333f_2ndofNoun1_Pluralnoun_sil.aiff' ]
test_4444=[path_test_audio + str(group) + 'test4444f_2ndofVerb0_ProgressiveN_sil.aiff', path_test_audio + str(group) + 'test4444c_Noun0_sil.aiff' ]
test_11111=[path_test_audio + str(group) + 'test11111f_Pluralnoun_Verb2_ProgressiveN_sil.aiff', path_test_audio + str(group) + 'test11111c_Verb2_ProgressiveN_Pluralverb_sil.aiff' ]
test_22222=[path_test_audio + str(group) + 'test22222f_Verb1_ProgressiveY_sil.aiff', path_test_audio + str(group) + 'test22222c_Noun1_Pluralnoun_sil.aiff' ]
test_33333=[path_test_audio + str(group) + 'test33333c_Verb0_sil.aiff', path_test_audio + str(group) + 'test33333f_2ndofNoun1_Pluralnoun_sil.aiff' ]
test_44444=[path_test_audio + str(group) + 'test44444f_2ndofVerb0_ProgressiveN_sil.aiff', path_test_audio + str(group) + 'test44444c_Noun1_sil.aiff' ]
test_111111=[path_test_audio + str(group) + 'test111111c_Verb2_ProgressiveN_Singularverb_sil.aiff', path_test_audio  + str(group) + 'test111111f_Singularnoun_Verb2_ProgressiveN_sil.aiff' ]
test_333333=[path_test_audio + str(group) + 'test333333f_2ndofVerb1_ProgressiveY_sil.aiff', path_test_audio + str(group) + 'test333333c_Verb1_sil.aiff']
test_222222=[path_test_audio + str(group) + 'test222222f_Verb0_ProgressiveN_sil.aiff',  path_test_audio + str(group) + 'test222222c_Noun0_Singularnoun_sil.aiff']
test_444444=[path_test_audio + str(group) + 'test444444c_Noun0_sil.aiff', path_test_audio + str(group) + 'test444444f_2ndofVerb1_ProgressiveY_sil.aiff']
test_1111111=[path_test_audio + str(group) + 'test1111111c_Verb0_ProgressiveN_Singularverb_sil.aiff', path_test_audio + str(group) + 'test1111111f_Noun0_Singularnoun_Verb2_sil.aiff']
test_3333333=[path_test_audio + str(group) + 'test3333333c_Verb0_sil.aiff', path_test_audio + str(group) + 'test3333333f_2ndofVerb0_ProgressiveN_sil.aiff']
test_4444444=[path_test_audio + str(group) + 'test4444444f_2ndofNoun1_Pluralnoun_sil.aiff', path_test_audio + str(group) + 'test4444444c_Noun1_sil.aiff']
test_33333333=[path_test_audio + str(group) + 'test33333333f_2ndofNoun0_Singularnoun_sil.aiff', path_test_audio + str(group) + 'test33333333c_Verb1_sil.aiff']
test_11111111=[path_test_audio + str(group) + 'test11111111c_Verb1_ProgressiveY_Pluralverb_sil.aiff', path_test_audio + str(group) + 'test11111111f_Noun1_Pluralnoun_Verb2_sil.aiff']
test_44444444=[path_test_audio + str(group) + 'test44444444f_2ndofNoun0_Singularnoun_sil.aiff', path_test_audio + str(group) + 'test44444444c_Noun0_sil.aiff']


alltesttrials=[test_1, test_2, test_3, test_4, test_11, test_22, test_33, test_44, test_111, test_222, test_333, test_444, test_1111, test_2222, test_3333, test_4444, test_11111, test_22222, test_33333, test_44444,  test_111111, test_333333, test_222222, test_444444, test_1111111, test_3333333, test_4444444, test_33333333, test_11111111, test_44444444]


######### Window and time 
win = visual.Window(fullscr="TRUE", size=(1440, 900))
now = datetime.now() 
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
fixation=visual.GratingStim(win=win)


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


def showinstructions(string, waittime):
    instructions1=visual.TextStim(win, text=string,  font='Times New Roman',  pos=[0,0],alignHoriz='center' )
    #instructions1.pos=(0,0)    
    instructions1.draw()
    win.flip()
    core.wait(waittime)
    clock = core.Clock()
    key = get_keypress()
    stoporcontinue(key)

########################## prepare train stimuli
audio_file=list()
sound_list=list()
video_file=list()
video_list=list()


getfiles(path_train_video, video_file, video_list)
random.shuffle(video_list)
for element in video_list:
        if "DS_Store" in element:
                 video_list.remove(element)
print("list of video stimuli to be presented after shuffle")
print(video_list)



#######INTRODUCTION

text1=u"Bienvenue à cette expérience! A partir de maintenant, appuyez sur la barre d'ESPACE pour continuer."
text2=u"Vous entendrez plusieurs phrases dans une langue étrangère. Chaque phrase décrit ce que les animaux font à l'écran."
text2_=u"Veuillez faire attention, il y aura bientôt un test sur votre connaissance de la langue!"
text3=u"Appuyez sur la barre d'ESPACE pour démarrer la formation, et à chaque fois que vous voulez entendre une nouvelle phrase."
showinstructions(text1, 0.5)
showinstructions(text2, 0.5)
showinstructions(text2_, 0.5)
showinstructions(text3, 0.5)
 
########TRAINING

text4ta=u"Félicitations! Vous venez de terminer un quart de votre formation."
text4tb=u"Félicitations! Vous venez de terminer la moitié de votre formation."
text4tc=u"Félicitations! Vous venez de terminer les trois quarts de votre formation. Attention, il y aura bientôt un test sur vos connaissances de la langue."
text4td=u"Félicitations! Vous venez de terminer votre formation."


c=0
movies=[]  
for i, video in enumerate(video_list): 
  #  videoname=str(video).replace("/Users/admin/Documents/datafiles/final/trainvideos/playset/", "").replace(".mov","")
    print(str(video))
    if c > 0 : 
     key = get_keypress()
     stoporcontinue(key)	
    c=c+1
    win.update()
    core.wait(0.5)
    if c == len(video_list)/4:
      showinstructions(text4ta, 0.5)
    if c == len(video_list)/2:
      showinstructions(text4tb, 0.5)
    if c == (len(video_list)/2 + len(video_list)/4 ):
      showinstructions(text4tc, 0.5)	
    fixation.draw()
    win.update()
    core.wait(0.5)
    mov = visual.MovieStim3(win, video,flipVert=False, flipHoriz=False)
    while mov.status != visual.FINISHED:
        mov.draw()
        win.flip()


win.flip()
core.wait(2)        

#########TEST INSTRUCTIONS

text4=u"Vous allez maintenant entendre deux sons."
text4_=u"Attention, vous ne les entendrez qu'une seule fois!"
text5=u"Quel son ressemble le plus à la langue que vous venez d'entendre?"
text5_=u"Ne réfléchissez pas trop et allez-y avec votre instinct!"
text6=u"Appuyez sur la touche Q si vous pensez que le premier son ressemble le plus à la langue que vous venez d'entendre, et sur la touche M si le second son est mieux."

showinstructions(text4td, 0.5)
showinstructions(text4, 0.5)
showinstructions(text4_, 0.5)
showinstructions(text5, 0.5)
showinstructions(text5_, 0.5)
showinstructions(text6, 0.5)


win.flip()
core.wait(2)

############# TEST
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
            print("2.clock0 before playing"+ str(soundNumber) + ",from beginning of turn in loop to sound")
            onset.append(clock0.getTime())
            print(onset)
            aud.play(when=nextFlip)
            win.flip()
            print("3.clock0 after playing" + str(soundNumber)+ ",from beginning of turn in loop to sound")
            onset.append(clock0.getTime())
            print(clock0.getTime())
            if soundNumber <len(testlist):
                core.wait(1)
            else:
                core.wait(0.5)


def trackanswers(testlist):
 results=[]
 clock1 = core.Clock()
 allKeys=event.waitKeys(keyList=["q", "m", "p"], timeStamped=clock1)
 print("5.clock1 while pressing keys, onset")
 onset.append(allKeys)
 print(onset)
 thisResp=""
 for thisKey in allKeys:
        if thisKey[0]=="q":
            if "c_" in testlist[0]:
              thisResp ="correct" 
              results.append([uniqueid, group, numberoftrial, dt_string, thisResp, testlist])
            else:
              thisResp = "wrong"
              results.append([uniqueid, group, numberoftrial, dt_string, thisResp, testlist])
        elif thisKey[0]=="m":
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
 print("Unique id, group, number of the trial, date, response, time of response")
 print(results)
 return(results)


#########TEST TRIALS
numberoftrial=0
for trial in alltesttrials:
    numberoftrial=numberoftrial+1
    onset=[]
    clock2=core.Clock()
    append1=str("1.clock2 before stimuli function:" + " "  + str(clock2.getTime()))
    onset.append(clock2.getTime())
    print("1.clock2 before stimuli function:")
    print("onset for each trial:")
    print(onset)
    presentest(trial)
    win.flip()
    print("6.clock2 before tracking answer")
    onset.append(clock2.getTime())
    print(onset)
    answer=trackanswers(trial)
    onset.append(clock2.getTime())
    print("8.clock2 after tracking answer")
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

sys.stdout = orig_stdout
logfile.close()



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

