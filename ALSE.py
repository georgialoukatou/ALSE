from os import system
import random
import os.path
import sox
import subprocess

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')

trainpath='/Users/admin/Documents/datafiles/final1/trainsounds1/'
#testpath='/Users/admin/Documents/datafiles/final1/testsounds/'
trainoutput=open("/Users/admin/Documents/datafiles/final1/output.csv", 'a')
testoutput=open("/Users/admin/Documents/datafiles/final1/testoutput.csv", 'a')

Syllables=[]

ANoun=[]
BNoun=[]
CNoun=[]
DNoun=[]

AVerb=[]
BVerb=[]
CVerb=[]
DVerb=[]

ASentence=[]
BSentence=[]
CSentence=[]
DSentence=[]

ADisrupter1=[]
ADisrupter2=[]
BDisrupter1=[]
BDisrupter2=[]
CDisrupter1=[]
CDisrupter2=[]
DDisrupter1=[]
DDisrupter2=[]

Atest=[]
Btest=[]
Ctest=[]
Dtest=[]


def stringtoPhon(string):
  phon=str(string).replace("[","").replace("]","").replace("'","").replace(" - ","").replace(", ", "")
  return phon

def trainstim(sentence, name, group):
 count=0
 for element in sentence:
#  trainoutput.write(element + str("\n"))
  element=stringtoPhon(element)
  system('say -o  /Users/admin/Documents/datafiles/final1/trainsounds1/{}.aiff  -v Paulina -r 140 {}'.format(name[count], element)) 
  title=name[count]
  print(title)
  title1=str(trainpath) + str(title) + '.aiff'
  print(title1)
  title2=str(trainpath) + str(group)+ '/'  + str(title) + '_sil.aiff'
  title_=sox.Transformer()
  title_.pad(1.8,1)    #  bash_command('sox title1 title2 pad 1 1')
  title_.build(title1, title2)
  title_.effects_log
  count=count+1

"""
#!!! Attention for group C, test 3F, 444F, 444444F 'single' has a weird pronunciation
def teststim(list, name, group):
 count=0
 for example in list:
   #  example=stringtoPhon(example)
   system('say -o  /Users/admin/Documents/datafiles/final1/testsounds/{}.aiff -v Paulina -r 140 {}'.format(name[count],  example))
   title=name[count]
   print(title)
   title1=str(testpath) + str(title) + '.aiff'
   print(title1)
   title2=str(testpath) + str(group)+ '/'  + str(title) + '_sil.aiff'
   title_=sox.Transformer()
   title_.pad(0.4,0.1)    #  bash_command('sox title1 title2 pad 1 1')
   title_.build(title1, title2)
   title_.effects_log
   count=count+1
   
 """  
   
   
Syllables=["glu","sin",  "ga",  "kli",  "ten",  "ko",  "blu", "tun",  "man",  "blo", "ti", "gle" ,"da", "pun",  "go", "kan", "fen", "bi"]

######################PREP PHASE
#######Group  A


ANoun.append(str(Syllables[0]+ Syllables[1]))
ANoun.append(str(Syllables[2]+ Syllables[3]))
ANoun.append(str(Syllables[4]))


AVerb.append(str(Syllables[5]+ Syllables[6]))
AVerb.append(str(Syllables[7]+ Syllables[8]))
AVerb.append(str(Syllables[9]))

ADisrupter1.append("")
ADisrupter1.append(str(Syllables[10]))
ADisrupter2.append("")
ADisrupter2.append(str(Syllables[11]))


ASingularNoun= str(Syllables[12])
ASingularVerb= str(Syllables[13])
APluralNoun= str(Syllables[14])
APluralVerb=  str(Syllables[15])
AProgressiveY= str(Syllables[16])
AProgressiveN= str(Syllables[17])

print("ANoun, AVerb, ADisrupter1, ADisrupter2, ASingularNoun, ASingularVerb, APluralNoun, APluralVerb, AProgressiveY, AProgressiveN")

print(ANoun, AVerb, ADisrupter1, ADisrupter2, ASingularNoun, ASingularVerb, APluralNoun, APluralVerb, AProgressiveY, AProgressiveN)


##########Group B

BNoun.append(str(Syllables[6]+ Syllables[16]))
BNoun.append(str(Syllables[15]+ Syllables[14]))
BNoun.append(str(Syllables[13]))


BVerb.append(str(Syllables[12]+ Syllables[11]))
BVerb.append(str(Syllables[10]+ Syllables[9]))
BVerb.append(str(Syllables[8]))


BDisrupter1.append("")
BDisrupter1.append(str(Syllables[7]))
BDisrupter2.append("")
BDisrupter2.append(str(Syllables[17]))



BSingularNoun= str(Syllables[5])
BSingularVerb= str(Syllables[4])
BPluralNoun= str(Syllables[3])
BPluralVerb=  str(Syllables[2])
BProgressiveY= str(Syllables[1])
BProgressiveN= str(Syllables[0])


print(BNoun, BVerb, BDisrupter1, BDisrupter2, BSingularNoun, BSingularVerb, BPluralNoun, BPluralVerb, BProgressiveY, BProgressiveN)


###########Group 3

CNoun.append(str(Syllables[9]+ Syllables[8]))
CNoun.append(str(Syllables[7]+ Syllables[6]))
CNoun.append(str(Syllables[5]))


CVerb.append(str(Syllables[4]+ Syllables[3]))
CVerb.append(str(Syllables[2]+ Syllables[1]))
CVerb.append(str(Syllables[0]))



CDisrupter1.append("")
CDisrupter1.append(str(Syllables[17]))
CDisrupter2.append("")
CDisrupter2.append(str(Syllables[16]))

CSingularNoun= str(Syllables[15])
CSingularVerb= str(Syllables[14])
CPluralNoun= str(Syllables[13])
CPluralVerb=  str(Syllables[12])
CProgressiveY= str(Syllables[11])
CProgressiveN= str(Syllables[10])

print(CNoun, CVerb, CDisrupter1, CDisrupter2, CSingularNoun, CSingularVerb, CPluralNoun, CPluralVerb, CProgressiveY, CProgressiveN)



##############Group 4 

DNoun.append(str(Syllables[8]+ Syllables[9]))
DNoun.append(str(Syllables[10]+ Syllables[11]))
DNoun.append(str(Syllables[12]))


DVerb.append(str(Syllables[13]+ Syllables[14]))
DVerb.append(str(Syllables[3]+ Syllables[16]))
DVerb.append(str(Syllables[17]))


DDisrupter1.append("")
DDisrupter1.append(str(Syllables[0]))
DDisrupter2.append("")
DDisrupter2.append(str(Syllables[1]))



DSingularNoun= str(Syllables[2])
DSingularVerb= str(Syllables[15])
DPluralNoun= str(Syllables[4])
DPluralVerb=  str(Syllables[5])
DProgressiveY= str(Syllables[6])
DProgressiveN= str(Syllables[7])


print(DNoun, DVerb, DDisrupter1, DDisrupter2, DSingularNoun, DSingularVerb, DPluralNoun, DPluralVerb, DProgressiveY, DProgressiveN)



#############################################TRAINING

ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep jumping (plural)
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats flip

ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #dog jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #dog flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep jumping (plural)
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #sheep walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #sheep walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats walk
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats walking
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[0]) #cat jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[0]) #cats jumping
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[0]) #cat flip
ASentence.append(ADisrupter1[1] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[0]) #cats flip
#
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #dog walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #dog walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #dog jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #dog flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #dog walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #dog walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #dog jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[0] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #dog flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #sheep jumping (plural)
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #sheep flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #sheep walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #sheep walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #sheep jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #sheep flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #sheep walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[1] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #sheep walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #cat walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #cat walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #cats walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #cats walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #cat jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #cats jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #cat flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #cats flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #cat walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[2] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #cat walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #cats walk
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[2] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #cats walking
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[1] + AProgressiveY + ASingularVerb + " - " + ADisrupter2[1]) #cat jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[1] + AProgressiveY + APluralVerb + " - " + ADisrupter2[1]) #cats jumping
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + ASingularNoun + " - " +  AVerb[0] + AProgressiveN + ASingularVerb + " - " + ADisrupter2[1]) #cat flip
ASentence.append(ADisrupter1[0] + " - " + ANoun[2] + APluralNoun + " - " +  AVerb[0] + AProgressiveN + APluralVerb + " - " + ADisrupter2[1]) #cats flip



########B
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep jumping (plural)
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats flip

BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #dog jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #dog flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep jumping (plural)
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #sheep walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #sheep walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats walk
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats walking
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[0]) #cat jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[0]) #cats jumping
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[0]) #cat flip
BSentence.append(BDisrupter1[1] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[0]) #cats flip
#
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #dog walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #dog walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #dog jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #dog flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #dog walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #dog walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #dog jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[0] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #dog flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #sheep jumping (plural)
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #sheep flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #sheep walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #sheep walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #sheep jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #sheep flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #sheep walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[1] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #sheep walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #cat walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #cat walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #cats walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #cats walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #cat jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #cats jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #cat flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #cats flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #cat walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[2] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #cat walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #cats walk
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[2] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #cats walking
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[1] + BProgressiveY + BSingularVerb + " - " + BDisrupter2[1]) #cat jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[1] + BProgressiveY + BPluralVerb + " - " + BDisrupter2[1]) #cats jumping
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BSingularNoun + " - " +  BVerb[0] + BProgressiveN + BSingularVerb + " - " + BDisrupter2[1]) #cat flip
BSentence.append(BDisrupter1[0] + " - " + BNoun[2] + BPluralNoun + " - " +  BVerb[0] + BProgressiveN + BPluralVerb + " - " + BDisrupter2[1]) #cats flip







#C
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep jumping (plural)
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats flip

CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #dog jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #dog flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep jumping (plural)
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #sheep walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #sheep walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats walk
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats walking
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[0]) #cat jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[0]) #cats jumping
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[0]) #cat flip
CSentence.append(CDisrupter1[1] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[0]) #cats flip
#
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #dog walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #dog walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #dog jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #dog flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #dog walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #dog walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #dog jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[0] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #dog flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #sheep jumping (plural)
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #sheep flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #sheep walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #sheep walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #sheep jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #sheep flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #sheep walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[1] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #sheep walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #cat walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #cat walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #cats walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #cats walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #cat jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #cats jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #cat flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #cats flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #cat walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[2] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #cat walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #cats walk
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[2] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #cats walking
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[1] + CProgressiveY + CSingularVerb + " - " + CDisrupter2[1]) #cat jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[1] + CProgressiveY + CPluralVerb + " - " + CDisrupter2[1]) #cats jumping
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CSingularNoun + " - " +  CVerb[0] + CProgressiveN + CSingularVerb + " - " + CDisrupter2[1]) #cat flip
CSentence.append(CDisrupter1[0] + " - " + CNoun[2] + CPluralNoun + " - " +  CVerb[0] + CProgressiveN + CPluralVerb + " - " + CDisrupter2[1]) #cats flip




#D
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep jumping (plural)
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats flip

DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #dog jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #dog flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep jumping (plural)
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #sheep walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #sheep walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats walk
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats walking
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[0]) #cat jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[0]) #cats jumping
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[0]) #cat flip
DSentence.append(DDisrupter1[1] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[0]) #cats flip
#
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #dog walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #dog walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #dog jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #dog flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #dog walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #dog walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #dog jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[0] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #dog flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #sheep jumping (plural)
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #sheep flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #sheep walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #sheep walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #sheep jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #sheep flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #sheep walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[1] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #sheep walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #cat walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #cat walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #cats walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #cats walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #cat jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #cats jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #cat flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #cats flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #cat walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[2] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #cat walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #cats walk
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[2] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #cats walking
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[1] + DProgressiveY + DSingularVerb + " - " + DDisrupter2[1]) #cat jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[1] + DProgressiveY + DPluralVerb + " - " + DDisrupter2[1]) #cats jumping
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DSingularNoun + " - " +  DVerb[0] + DProgressiveN + DSingularVerb + " - " + DDisrupter2[1]) #cat flip
DSentence.append(DDisrupter1[0] + " - " + DNoun[2] + DPluralNoun + " - " +  DVerb[0] + DProgressiveN + DPluralVerb + " - " + DDisrupter2[1]) #cats flip



#for N in DNoun:
 # for V in DVerb:
  #   DSentence.append(random.choice(DDisrupter1)+ " - " + N + DSingularNoun + " - " +  V + DProgressiveY + DSingularVerb + " - " + random.choice(DDisrupter2))
   #  DSentence.append(random.choice(DDisrupter1)+ " - " + N + DPluralNoun + " - " + V + DProgressiveY + DPluralVerb + " - " + random.choice(DDisrupter2))
   #  DSentence.append(random.choice(DDisrupter1)+ " - " + N + DSingularNoun + " - " + V + DProgressiveN + DSingularVerb + " - " + random.choice(DDisrupter2))
    # DSentence.append(random.choice(DDisrupter1)+ " - " + N + DPluralNoun + " - " + V + DProgressiveN + DPluralVerb + " - " + random.choice(DDisrupter2))







Atrainnamelist=["1_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"2_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"3_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"4_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"5_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]", 
"6_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"7_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"8_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]", 
"9_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"10_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"11_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"12_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"13_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"14_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"15_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"16_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"17_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"18_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]", 
"19_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"20_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"21_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"22_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"23_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"24_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"25_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"26_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"27_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"28_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"29_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"30_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"31_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"32_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"33_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"34_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"35_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"36_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"37_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]", 
"38_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"39_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"40_ADisrupter1[1]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]", 
"41_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"42_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"43_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"44_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"45_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"46_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"47_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"48_ADisrupter1[1]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]", 
"49_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"50_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]", 
"51_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"52_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"53_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"54_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"55_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"56_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"57_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"58_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"59_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"60_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"61_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[0]",
"62_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[0]",
"63_ADisrupter1[1]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[0]",
"64_ADisrupter1[1]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[0]",
"65_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1]",
"66_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"67_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"68_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1]",
"69_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1]", 
"70_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"71_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"72_ADisrupter1[0]_ANoun[0]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1]", 
"73_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"74_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1]", 
"75_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"76_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1]", 
"77_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"78_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1]", 
"79_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"80_ADisrupter1[0]_ANoun[1]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1]", 
"81_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1]",
"82_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1]", 
"83_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1]",
"84_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"85_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"86_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"87_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1]",
"88_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1]",
"89_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveN_ASingularVerb_ADisrupter2[1]",
"90_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[2]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"91_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveN_APluralVerb_ADisrupter2[1]",
"92_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[2]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"93_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[1]_AProgressiveY_ASingularVerb_ADisrupter2[1]",
"94_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[1]_AProgressiveY_APluralVerb_ADisrupter2[1]",
"95_ADisrupter1[0]_ANoun[2]_ASingularNoun_AVerb[0]_AProgressiveN_ASingularVerb_ADisrupter2[1]",
"96_ADisrupter1[0]_ANoun[2]_APluralNoun_AVerb[0]_AProgressiveN_APluralVerb_ADisrupter2[1]"
]


print(len(ASentence))
print(len(Atrainnamelist))




Btrainnamelist=["1_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"2_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"3_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"4_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"5_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]", 
"6_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"7_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"8_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]", 
"9_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"10_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"11_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"12_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"13_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"14_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"15_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"16_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"17_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"18_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]", 
"19_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"20_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"21_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"22_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"23_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"24_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"25_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"26_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"27_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"28_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"29_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"30_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"31_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"32_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"33_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"34_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"35_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"36_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"37_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]", 
"38_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"39_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"40_BDisrupter1[1]_BNoun[0]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]", 
"41_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"42_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"43_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"44_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"45_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"46_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"47_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"48_BDisrupter1[1]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]", 
"49_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"50_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]", 
"51_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"52_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"53_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"54_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"55_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"56_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"57_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"58_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"59_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"60_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"61_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[0]",
"62_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[0]",
"63_BDisrupter1[1]_BNoun[2]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[0]",
"64_BDisrupter1[1]_BNoun[2]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[0]",
"65_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[1]",
"66_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"67_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"68_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[1]",
"69_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[1]", 
"70_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"71_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"72_BDisrupter1[0]_BNoun[0]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[1]", 
"73_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"74_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[1]", 
"75_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"76_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[1]", 
"77_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"78_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[1]", 
"79_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"80_BDisrupter1[0]_BNoun[1]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[1]", 
"81_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[1]",
"82_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[1]", 
"83_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[1]",
"84_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"85_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"86_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"87_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[1]",
"88_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[1]",
"89_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveN_BSingularVerb_BDisrupter2[1]",
"90_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[2]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"91_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveN_BPluralVerb_BDisrupter2[1]",
"92_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[2]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"93_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[1]_BProgressiveY_BSingularVerb_BDisrupter2[1]",
"94_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[1]_BProgressiveY_BPluralVerb_BDisrupter2[1]",
"95_BDisrupter1[0]_BNoun[2]_BSingularNoun_BVerb[0]_BProgressiveN_BSingularVerb_BDisrupter2[1]",
"96_BDisrupter1[0]_BNoun[2]_BPluralNoun_BVerb[0]_BProgressiveN_BPluralVerb_BDisrupter2[1]"
]


print(len(BSentence))
print(len(Btrainnamelist))



Ctrainnamelist=["1_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"2_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"3_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"4_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"5_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]", 
"6_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"7_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"8_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]", 
"9_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"10_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"11_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"12_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"13_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"14_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"15_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"16_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"17_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"18_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]", 
"19_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"20_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"21_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"22_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"23_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"24_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"25_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"26_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"27_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"28_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"29_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"30_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"31_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"32_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"33_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"34_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"35_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"36_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"37_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]", 
"38_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"39_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"40_CDisrupter1[1]_CNoun[0]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]", 
"41_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"42_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"43_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"44_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"45_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"46_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"47_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"48_CDisrupter1[1]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]", 
"49_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"50_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]", 
"51_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"52_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"53_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"54_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"55_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"56_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"57_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"58_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"59_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"60_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"61_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[0]",
"62_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[0]",
"63_CDisrupter1[1]_CNoun[2]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[0]",
"64_CDisrupter1[1]_CNoun[2]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[0]",
"65_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[1]",
"66_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"67_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"68_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[1]",
"69_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[1]", 
"70_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"71_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"72_CDisrupter1[0]_CNoun[0]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[1]", 
"73_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"74_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[1]", 
"75_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"76_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[1]", 
"77_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"78_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[1]", 
"79_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"80_CDisrupter1[0]_CNoun[1]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[1]", 
"81_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[1]",
"82_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[1]", 
"83_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[1]",
"84_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"85_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"86_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"87_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[1]",
"88_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[1]",
"89_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveN_CSingularVerb_CDisrupter2[1]",
"90_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[2]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"91_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveN_CPluralVerb_CDisrupter2[1]",
"92_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[2]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"93_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[1]_CProgressiveY_CSingularVerb_CDisrupter2[1]",
"94_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[1]_CProgressiveY_CPluralVerb_CDisrupter2[1]",
"95_CDisrupter1[0]_CNoun[2]_CSingularNoun_CVerb[0]_CProgressiveN_CSingularVerb_CDisrupter2[1]",
"96_CDisrupter1[0]_CNoun[2]_CPluralNoun_CVerb[0]_CProgressiveN_CPluralVerb_CDisrupter2[1]"
]

print(len(CSentence))
print(len(Ctrainnamelist))


Dtrainnamelist=["1_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"2_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"3_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"4_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"5_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]", 
"6_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"7_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"8_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]", 
"9_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"10_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"11_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"12_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"13_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"14_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"15_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"16_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"17_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"18_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]", 
"19_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"20_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"21_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"22_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"23_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"24_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"25_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"26_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"27_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"28_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"29_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"30_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"31_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"32_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"33_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"34_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"35_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"36_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"37_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]", 
"38_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"39_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"40_DDisrupter1[1]_DNoun[0]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]", 
"41_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"42_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"43_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"44_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"45_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"46_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"47_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"48_DDisrupter1[1]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]", 
"49_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"50_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]", 
"51_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"52_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"53_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"54_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"55_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"56_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"57_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"58_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"59_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"60_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"61_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[0]",
"62_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[0]",
"63_DDisrupter1[1]_DNoun[2]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[0]",
"64_DDisrupter1[1]_DNoun[2]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[0]",
"65_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[1]",
"66_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"67_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"68_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[1]",
"69_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[1]", 
"70_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"71_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"72_DDisrupter1[0]_DNoun[0]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[1]", 
"73_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"74_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[1]", 
"75_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"76_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[1]", 
"77_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"78_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[1]", 
"79_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"80_DDisrupter1[0]_DNoun[1]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[1]", 
"81_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[1]",
"82_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[1]", 
"83_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[1]",
"84_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"85_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"86_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"87_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[1]",
"88_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[1]",
"89_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveN_DSingularVerb_DDisrupter2[1]",
"90_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[2]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"91_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveN_DPluralVerb_DDisrupter2[1]",
"92_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[2]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"93_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[1]_DProgressiveY_DSingularVerb_DDisrupter2[1]",
"94_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[1]_DProgressiveY_DPluralVerb_DDisrupter2[1]",
"95_DDisrupter1[0]_DNoun[2]_DSingularNoun_DVerb[0]_DProgressiveN_DSingularVerb_DDisrupter2[1]",
"96_DDisrupter1[0]_DNoun[2]_DPluralNoun_DVerb[0]_DProgressiveN_DPluralVerb_DDisrupter2[1]"
]




print(len(DSentence))
print(len(Dtrainnamelist))





#############TEST



##GroupA
#verb vs non-verb
Atest1c_Verb2_ProgressiveY_Pluralverb = AVerb[2] + AProgressiveY + APluralVerb # 0.5  0.5
Atest1f_Pluralnoun_Verb2_ProgressiveY = APluralNoun + AVerb[2] + AProgressiveY 
Atest11c_Verb2_ProgressiveY_Singularverb = AVerb[2] + AProgressiveY + ASingularVerb # 0.5  + 0.5
Atest11f_Singularnoun_Verb2_ProgressiveY = ASingularNoun + AVerb[2] + AProgressiveY 
Atest111c_Verb0_ProgressiveN_Singularverb = AVerb[0] + AProgressiveN + ASingularVerb # 1 + 1  + 0.5
Atest111f_Noun1_Pluralnoun_Verb2 = ANoun[1] + APluralNoun + AVerb[2]
Atest1111c_Verb1_ProgressiveY_Pluralverb = AVerb[1] + AProgressiveY + APluralVerb # 1 + 1 + 0.5
Atest1111f_Noun0_Singularnoun_Verb2 = ANoun[0] + ASingularNoun +  AVerb[2] 
Atest11111c_Verb2_ProgressiveN_Pluralverb = AVerb[2] + AProgressiveN + APluralVerb #0.5 0.5
Atest11111f_Pluralnoun_Verb2_ProgressiveN = APluralNoun + AVerb[2] + AProgressiveN
Atest111111c_Verb2_ProgressiveN_Singularverb = AVerb[2] + AProgressiveN + ASingularVerb #0.5 0.5
Atest111111f_Singularnoun_Verb2_ProgressiveN = ASingularNoun + AVerb[2] + AProgressiveN
Atest1111111c_Verb0_ProgressiveN_Singularverb = AVerb[0] + AProgressiveN + ASingularVerb # 1 + 1  + 0.5
Atest1111111f_Noun0_Singularnoun_Verb2 = ANoun[0] + ASingularNoun +  AVerb[2] 
Atest11111111c_Verb1_ProgressiveY_Pluralverb = AVerb[1] + AProgressiveY + APluralVerb # 1 + 1 + 0.5
Atest11111111f_Noun1_Pluralnoun_Verb2 = ANoun[1] + APluralNoun + AVerb[2]





Btest1c_Verb2_ProgressiveY_Pluralverb = BVerb[2] + BProgressiveY + BPluralVerb # 0.5  0.5
Btest1f_Pluralnoun_Verb2_ProgressiveY = BPluralNoun + BVerb[2] + BProgressiveY 
Btest11c_Verb2_ProgressiveY_Singularverb = BVerb[2] + BProgressiveY + BSingularVerb # 0.5  + 0.5
Btest11f_Singularnoun_Verb2_ProgressiveY = BSingularNoun + BVerb[2] + BProgressiveY 
Btest111c_Verb0_ProgressiveN_Singularverb = BVerb[0] + BProgressiveN + BSingularVerb # 1 + 1  + 0.5
Btest111f_Noun1_Pluralnoun_Verb2 = BNoun[1] + BPluralNoun + BVerb[2]
Btest1111c_Verb1_ProgressiveY_Pluralverb = BVerb[1] + BProgressiveY + BPluralVerb # 1 + 1 + 0.5
Btest1111f_Noun0_Singularnoun_Verb2 = BNoun[0] + BSingularNoun +  BVerb[2] 
Btest11111c_Verb2_ProgressiveN_Pluralverb = BVerb[2] + BProgressiveN + BPluralVerb #0.5 0.5
Btest11111f_Pluralnoun_Verb2_ProgressiveN = BPluralNoun + BVerb[2] + BProgressiveN
Btest111111c_Verb2_ProgressiveN_Singularverb = BVerb[2] + BProgressiveN + BSingularVerb #0.5 0.5
Btest111111f_Singularnoun_Verb2_ProgressiveN = BSingularNoun + BVerb[2] + BProgressiveN
Btest1111111c_Verb0_ProgressiveN_Singularverb = BVerb[0] + BProgressiveN + BSingularVerb # 1 + 1  + 0.5
Btest1111111f_Noun0_Singularnoun_Verb2 = BNoun[0] + BSingularNoun +  BVerb[2] 
Btest11111111c_Verb1_ProgressiveY_Pluralverb = BVerb[1] + BProgressiveY + BPluralVerb # 1 + 1 + 0.5
Btest11111111f_Noun1_Pluralnoun_Verb2 = BNoun[1] + BPluralNoun + BVerb[2]



Ctest1c_Verb2_ProgressiveY_Pluralverb = CVerb[2] + CProgressiveY + CPluralVerb # 0.5  0.5
Ctest1f_Pluralnoun_Verb2_ProgressiveY = CPluralNoun + CVerb[2] + CProgressiveY 
Ctest11c_Verb2_ProgressiveY_Singularverb = CVerb[2] + CProgressiveY + CSingularVerb # 0.5  + 0.5
Ctest11f_Singularnoun_Verb2_ProgressiveY = CSingularNoun + CVerb[2] + CProgressiveY 
Ctest111c_Verb0_ProgressiveN_Singularverb = CVerb[0] + CProgressiveN + CSingularVerb # 1 + 1  + 0.5
Ctest111f_Noun1_Pluralnoun_Verb2 = CNoun[1] + CPluralNoun + CVerb[2]
Ctest1111c_Verb1_ProgressiveY_Pluralverb = CVerb[1] + CProgressiveY + CPluralVerb # 1 + 1 + 0.5
Ctest1111f_Noun0_Singularnoun_Verb2 = CNoun[0] + CSingularNoun +  CVerb[2] 
Ctest11111c_Verb2_ProgressiveN_Pluralverb = CVerb[2] + CProgressiveN + CPluralVerb #0.5 0.5
Ctest11111f_Pluralnoun_Verb2_ProgressiveN = CPluralNoun + CVerb[2] + CProgressiveN
Ctest111111c_Verb2_ProgressiveN_Singularverb = CVerb[2] + CProgressiveN + CSingularVerb #0.5 0.5
Ctest111111f_Singularnoun_Verb2_ProgressiveN = CSingularNoun + CVerb[2] + CProgressiveN
Ctest1111111c_Verb0_ProgressiveN_Singularverb = CVerb[0] + CProgressiveN + CSingularVerb # 1 + 1  + 0.5
Ctest1111111f_Noun0_Singularnoun_Verb2 = CNoun[0] + CSingularNoun +  CVerb[2] 
Ctest11111111c_Verb1_ProgressiveY_Pluralverb = CVerb[1] + CProgressiveY + CPluralVerb # 1 + 1 + 0.5
Ctest11111111f_Noun1_Pluralnoun_Verb2 = CNoun[1] + CPluralNoun + CVerb[2]





Dtest1c_Verb2_ProgressiveY_Pluralverb = DVerb[2] + DProgressiveY + DPluralVerb # 0.5  0.5
Dtest1f_Pluralnoun_Verb2_ProgressiveY = DPluralNoun + DVerb[2] + DProgressiveY 
Dtest11c_Verb2_ProgressiveY_Singularverb = DVerb[2] + DProgressiveY + DSingularVerb # 0.5  + 0.5
Dtest11f_Singularnoun_Verb2_ProgressiveY = DSingularNoun + DVerb[2] + DProgressiveY 
Dtest111c_Verb0_ProgressiveN_Singularverb = DVerb[0] + DProgressiveN + DSingularVerb # 1 + 1  + 0.5
Dtest111f_Noun1_Pluralnoun_Verb2 = DNoun[1] + DPluralNoun + DVerb[2]
Dtest1111c_Verb1_ProgressiveY_Pluralverb = DVerb[1] + DProgressiveY + DPluralVerb # 1 + 1 + 0.5
Dtest1111f_Noun0_Singularnoun_Verb2 = DNoun[0] + DSingularNoun +  DVerb[2] 
Dtest11111c_Verb2_ProgressiveN_Pluralverb = DVerb[2] + DProgressiveN + DPluralVerb #0.5 0.5
Dtest11111f_Pluralnoun_Verb2_ProgressiveN = DPluralNoun + DVerb[2] + DProgressiveN
Dtest111111c_Verb2_ProgressiveN_Singularverb = DVerb[2] + DProgressiveN + DSingularVerb #0.5 0.5
Dtest111111f_Singularnoun_Verb2_ProgressiveN = DSingularNoun + DVerb[2] + DProgressiveN
Dtest1111111c_Verb0_ProgressiveN_Singularverb = DVerb[0] + DProgressiveN + DSingularVerb # 1 + 1  + 0.5
Dtest1111111f_Noun0_Singularnoun_Verb2 = DNoun[0] + DSingularNoun +  DVerb[2] 
Dtest11111111c_Verb1_ProgressiveY_Pluralverb = DVerb[1] + DProgressiveY + DPluralVerb # 1 + 1 + 0.5
Dtest11111111f_Noun1_Pluralnoun_Verb2 = DNoun[1] + DPluralNoun + DVerb[2]





#noun vs non-noun
Atest2c_Noun2_Singularnoun = ANoun[2] + ASingularNoun
Atest2f_Singularnoun_Verb2 = ASingularNoun + AVerb[2]
Atest22c_Noun2_Pluralnoun = ANoun[2] + APluralNoun
Atest22f_Pluralnoun_Verb2 = APluralNoun + AVerb[2]
Atest222c_Noun1_Pluralnoun = ANoun[1] + APluralNoun
Atest222f_Verb0_ProgressiveN  = AVerb[0] + AProgressiveN  
Atest2222c_Noun0_Singularnoun = ANoun[0] + ASingularNoun
Atest2222f_Verb1_ProgressiveY  = AVerb[1] + AProgressiveY  
Atest22222c_Noun1_Pluralnoun = ANoun[1] + APluralNoun
Atest22222f_Verb1_ProgressiveY  = AVerb[1] + AProgressiveY 
Atest222222c_Noun0_Singularnoun = ANoun[0] + ASingularNoun
Atest222222f_Verb0_ProgressiveN  = AVerb[0] + AProgressiveN 


Btest2c_Noun2_Singularnoun = BNoun[2] + BSingularNoun
Btest2f_Singularnoun_Verb2 = BSingularNoun + BVerb[2]
Btest22c_Noun2_Pluralnoun = BNoun[2] + BPluralNoun
Btest22f_Pluralnoun_Verb2 = BPluralNoun + BVerb[2]
Btest222c_Noun1_Pluralnoun = BNoun[1] + BPluralNoun
Btest222f_Verb0_ProgressiveN  = BVerb[0] + BProgressiveN  #smallPROBLEM
Btest2222c_Noun0_Singularnoun = BNoun[0] + BSingularNoun
Btest2222f_Verb1_ProgressiveY  = BVerb[1] + BProgressiveY  #smallPROBLEM
Btest22222c_Noun1_Pluralnoun = BNoun[1] + BPluralNoun
Btest22222f_Verb1_ProgressiveY  = BVerb[1] + BProgressiveY 
Btest222222c_Noun0_Singularnoun = BNoun[0] + BSingularNoun
Btest222222f_Verb0_ProgressiveN  = BVerb[0] + BProgressiveN 


Ctest2c_Noun2_Singularnoun = CNoun[2] + CSingularNoun
Ctest2f_Singularnoun_Verb2 = CSingularNoun + CVerb[2]
Ctest22c_Noun2_Pluralnoun = CNoun[2] + CPluralNoun
Ctest22f_Pluralnoun_Verb2 = CPluralNoun + CVerb[2]
Ctest222c_Noun1_Pluralnoun = CNoun[1] + CPluralNoun
Ctest222f_Verb0_ProgressiveN  = CVerb[0] + CProgressiveN  #smallPROCLEM
Ctest2222c_Noun0_Singularnoun = CNoun[0] + CSingularNoun
Ctest2222f_Verb1_ProgressiveY  = CVerb[1] + CProgressiveY  #smallPROCLEM
Ctest22222c_Noun1_Pluralnoun = CNoun[1] + CPluralNoun
Ctest22222f_Verb1_ProgressiveY  = CVerb[1] + CProgressiveY 
Ctest222222c_Noun0_Singularnoun = CNoun[0] + CSingularNoun
Ctest222222f_Verb0_ProgressiveN  = CVerb[0] + CProgressiveN 


Dtest2c_Noun2_Singularnoun = DNoun[2] + DSingularNoun
Dtest2f_Singularnoun_Verb2 = DSingularNoun + DVerb[2]
Dtest22c_Noun2_Pluralnoun = DNoun[2] + DPluralNoun
Dtest22f_Pluralnoun_Verb2 = DPluralNoun + DVerb[2]
Dtest222c_Noun1_Pluralnoun = DNoun[1] + DPluralNoun
Dtest222f_Verb0_ProgressiveN  = DVerb[0] + DProgressiveN  #smallPRODLEM
Dtest2222c_Noun0_Singularnoun = DNoun[0] + DSingularNoun
Dtest2222f_Verb1_ProgressiveY  = DVerb[1] + DProgressiveY  #smallPRODLEM
Dtest22222c_Noun1_Pluralnoun = DNoun[1] + DPluralNoun
Dtest22222f_Verb1_ProgressiveY  = DVerb[1] + DProgressiveY 
Dtest222222c_Noun0_Singularnoun = DNoun[0] + DSingularNoun
Dtest222222f_Verb0_ProgressiveN  = DVerb[0] + DProgressiveN 

#verbstem vs non-verbstem
Atest3c_Verb0  = AVerb[0]
Atest3f_2ndofVerb1_ProgressiveY = AVerb[1][3:6]+ AProgressiveY
Atest33c_Verb1  = AVerb[1]
Atest33f_2ndofVerb0_ProgressiveN = AVerb[0][2:5] + AProgressiveN
Atest333c_Verb0  = AVerb[0]
Atest333f_2ndofNoun0_Singularnoun  =  ANoun[0][3:6]+ ASingularNoun 
Atest3333c_Verb1  = AVerb[1]
Atest3333f_2ndofNoun1_Pluralnoun  = ANoun[1][2:5]+ APluralNoun 
Atest33333c_Verb0  = AVerb[0]
Atest33333f_2ndofNoun1_Pluralnoun  = ANoun[1][2:5]+ APluralNoun 
Atest333333c_Verb1  = AVerb[1]
Atest333333f_2ndofVerb1_ProgressiveY = AVerb[1][3:6]+ AProgressiveY
Atest3333333c_Verb0  = AVerb[0]
Atest3333333f_2ndofVerb0_ProgressiveN = AVerb[0][2:5] + AProgressiveN
Atest33333333c_Verb1  = AVerb[1]
Atest33333333f_2ndofNoun0_Singularnoun  =  ANoun[0][3:6]+ ASingularNoun 


Btest3c_Verb0  = BVerb[0]
Btest3f_2ndofVerb1_ProgressiveY = BVerb[1][3:6]+ BProgressiveY
Btest33c_Verb1  = BVerb[1]
Btest33f_2ndofVerb0_ProgressiveN = BVerb[0][3:6] + BProgressiveN
Btest333c_Verb0  = BVerb[0]
Btest333f_2ndofNoun0_Singularnoun  =  BNoun[0][3:6]+ BSingularNoun 
Btest3333c_Verb1  = BVerb[1]
Btest3333f_2ndofNoun1_Pluralnoun  = BNoun[1][3:6]+ BPluralNoun 
Btest33333c_Verb0  = BVerb[0]
Btest33333f_2ndofNoun1_Pluralnoun  = BNoun[1][3:6]+ BPluralNoun 
Btest333333c_Verb1  = BVerb[1]
Btest333333f_2ndofVerb1_ProgressiveY = BVerb[1][3:6]+ BProgressiveY
Btest3333333c_Verb0  = BVerb[0]
Btest3333333f_2ndofVerb0_ProgressiveN = BVerb[0][3:6] + BProgressiveN
Btest33333333c_Verb1  = BVerb[1]
Btest33333333f_2ndofNoun0_Singularnoun  =  BNoun[0][3:6]+ BSingularNoun 



Ctest3c_Verb0  = CVerb[0]
Ctest3f_2ndofVerb1_ProgressiveY = CVerb[1][2:5]+ CProgressiveY
Ctest33c_Verb1  = CVerb[1]
Ctest33f_2ndofVerb0_ProgressiveN = CVerb[0][3:6] + CProgressiveN
Ctest333c_Verb0  = CVerb[0]
Ctest333f_2ndofNoun0_Singularnoun  =  CNoun[0][3:6]+ CSingularNoun 
Ctest3333c_Verb1  = CVerb[1]
Ctest3333f_2ndofNoun1_Pluralnoun  = CNoun[1][3:6]+ CPluralNoun 
Ctest33333c_Verb0  = CVerb[0]
Ctest33333f_2ndofNoun1_Pluralnoun  = CNoun[1][3:6]+ CPluralNoun 
Ctest333333c_Verb1  = CVerb[1]
Ctest333333f_2ndofVerb1_ProgressiveY = CVerb[1][2:5]+ CProgressiveY
Ctest3333333c_Verb0  = CVerb[0]
Ctest3333333f_2ndofVerb0_ProgressiveN = CVerb[0][3:6] + CProgressiveN
Ctest33333333c_Verb1  = CVerb[1]
Ctest33333333f_2ndofNoun0_Singularnoun  =  CNoun[0][3:6]+ CSingularNoun 

Dtest3c_Verb0  = DVerb[0]
Dtest3f_2ndofVerb1_ProgressiveY = DVerb[1][3:6]+ DProgressiveY
Dtest33c_Verb1  = DVerb[1]
Dtest33f_2ndofVerb0_ProgressiveN = DVerb[0][3:6] + DProgressiveN
Dtest333c_Verb0  = DVerb[0]
Dtest333f_2ndofNoun0_Singularnoun  =  DNoun[0][3:6]+ DSingularNoun 
Dtest3333c_Verb1  = DVerb[1]
Dtest3333f_2ndofNoun1_Pluralnoun  = DNoun[1][2:5]+ DPluralNoun 
Dtest33333c_Verb0  = DVerb[0]
Dtest33333f_2ndofNoun1_Pluralnoun  = DNoun[1][2:5]+ DPluralNoun 
Dtest333333c_Verb1  = DVerb[1]
Dtest333333f_2ndofVerb1_ProgressiveY = DVerb[1][3:6]+ DProgressiveY
Dtest3333333c_Verb0  = DVerb[0]
Dtest3333333f_2ndofVerb0_ProgressiveN = DVerb[0][3:6] + DProgressiveN
Dtest33333333c_Verb1  = DVerb[1]
Dtest33333333f_2ndofNoun0_Singularnoun  =  DNoun[0][3:6]+ DSingularNoun 









#nounstem vs non-nounstem
Atest4c_Noun1 = ANoun[1]
Atest4f_2ndofNoun1_Pluralnoun  =  ANoun[1][2:5]+ APluralNoun
Atest44c_Noun0 = ANoun[0]
Atest44f_2ndofNoun0_Singularnoun  =  ANoun[0][3:6]+ ASingularNoun 
Atest444c_Noun1 =  ANoun[1]
Atest444f_2ndofVerb1_ProgressiveY =  AVerb[1][3:6]+ AProgressiveY
Atest4444c_Noun0 =  ANoun[0]
Atest4444f_2ndofVerb0_ProgressiveN = AVerb[0][2:5] + AProgressiveN
Atest44444c_Noun1 = ANoun[1]
Atest44444f_2ndofVerb0_ProgressiveN = AVerb[0][2:5] + AProgressiveN
Atest444444c_Noun0 =  ANoun[0]
Atest444444f_2ndofVerb1_ProgressiveY =  AVerb[1][3:6]+ AProgressiveY
Atest4444444c_Noun1 = ANoun[1]
Atest4444444f_2ndofNoun1_Pluralnoun  =  ANoun[1][2:5]+ APluralNoun
Atest44444444c_Noun0 = ANoun[0]
Atest44444444f_2ndofNoun0_Singularnoun  =  ANoun[0][3:6]+ ASingularNoun 



Btest4c_Noun1 = BNoun[1]
Btest4f_2ndofNoun1_Pluralnoun  =  BNoun[1][3:6]+ BPluralNoun
Btest44c_Noun0 = BNoun[0]
Btest44f_2ndofNoun0_Singularnoun  =  BNoun[0][3:6]+ BSingularNoun 
Btest444c_Noun1 =  BNoun[1]
Btest444f_2ndofVerb1_ProgressiveY =  BVerb[1][2:5]+ BProgressiveY
Btest4444c_Noun0 =  BNoun[0]
Btest4444f_2ndofVerb0_ProgressiveN = BVerb[0][2:5] + BProgressiveN
Btest44444c_Noun1 = BNoun[1]
Btest44444f_2ndofVerb0_ProgressiveN = BVerb[0][2:5] + BProgressiveN
Btest444444c_Noun0 =  BNoun[0]
Btest444444f_2ndofVerb1_ProgressiveY =  BVerb[1][2:5]+ BProgressiveY
Btest4444444c_Noun1 = BNoun[1]
Btest4444444f_2ndofNoun1_Pluralnoun  =  BNoun[1][3:6]+ BPluralNoun
Btest44444444c_Noun0 = BNoun[0]
Btest44444444f_2ndofNoun0_Singularnoun  =  BNoun[0][3:6]+ BSingularNoun 


Ctest4c_Noun1 = CNoun[1]
Ctest4f_2ndofNoun1_Pluralnoun  =  CNoun[1][3:6]+ CPluralNoun
Ctest44c_Noun0 = CNoun[0]
Ctest44f_2ndofNoun0_Singularnoun  =  CNoun[0][3:6]+ CSingularNoun 
Ctest444c_Noun1 =  CNoun[1]
Ctest444f_2ndofVerb1_ProgressiveY =  CVerb[1][2:5]+ CProgressiveY
Ctest4444c_Noun0 =  CNoun[0]
Ctest4444f_2ndofVerb0_ProgressiveN = CVerb[0][3:6] + CProgressiveN
Ctest44444c_Noun1 = CNoun[1]
Ctest44444f_2ndofVerb0_ProgressiveN = CVerb[0][3:6] + CProgressiveN
Ctest444444c_Noun0 =  CNoun[0]
Ctest444444f_2ndofVerb1_ProgressiveY =  CVerb[1][2:5]+ CProgressiveY
Ctest4444444c_Noun1 = CNoun[1]
Ctest4444444f_2ndofNoun1_Pluralnoun  =  CNoun[1][3:6]+ CPluralNoun
Ctest44444444c_Noun0 = CNoun[0]
Ctest44444444f_2ndofNoun0_Singularnoun  =  CNoun[0][3:6]+ CSingularNoun 


Dtest4c_Noun1 = DNoun[1]
Dtest4f_2ndofNoun1_Pluralnoun  =  DNoun[1][2:5]+ DPluralNoun
Dtest44c_Noun0 = DNoun[0]
Dtest44f_2ndofNoun0_Singularnoun  =  DNoun[0][3:6]+ DSingularNoun 
Dtest444c_Noun1 =  DNoun[1]
Dtest444f_2ndofVerb1_ProgressiveY =  DVerb[1][3:6]+ DProgressiveY
Dtest4444c_Noun0 =  DNoun[0]
Dtest4444f_2ndofVerb0_ProgressiveN = DVerb[0][3:6] + DProgressiveN
Dtest44444c_Noun1 = DNoun[1]
Dtest44444f_2ndofVerb0_ProgressiveN = DVerb[0][3:6] + DProgressiveN
Dtest444444c_Noun0 =  DNoun[0]
Dtest444444f_2ndofVerb1_ProgressiveY =  DVerb[1][3:6]+ DProgressiveY
Dtest4444444c_Noun1 = DNoun[1]
Dtest4444444f_2ndofNoun1_Pluralnoun  =  DNoun[1][2:5]+ DPluralNoun
Dtest44444444c_Noun0 = DNoun[0]
Dtest44444444f_2ndofNoun0_Singularnoun  =  DNoun[0][3:6]+ DSingularNoun 






Atest.extend((Atest1c_Verb2_ProgressiveY_Pluralverb,Atest1f_Pluralnoun_Verb2_ProgressiveY,
Atest11c_Verb2_ProgressiveY_Singularverb,Atest11f_Singularnoun_Verb2_ProgressiveY,
Atest111c_Verb0_ProgressiveN_Singularverb, Atest111f_Noun1_Pluralnoun_Verb2,
Atest1111c_Verb1_ProgressiveY_Pluralverb,Atest1111f_Noun0_Singularnoun_Verb2,
Atest11111c_Verb2_ProgressiveN_Pluralverb,Atest11111f_Pluralnoun_Verb2_ProgressiveN,
Atest111111c_Verb2_ProgressiveN_Singularverb, Atest111111f_Singularnoun_Verb2_ProgressiveN,
Atest1111111c_Verb0_ProgressiveN_Singularverb, Atest1111111f_Noun0_Singularnoun_Verb2,
Atest11111111c_Verb1_ProgressiveY_Pluralverb,Atest11111111f_Noun1_Pluralnoun_Verb2,
Atest2c_Noun2_Singularnoun, Atest2f_Singularnoun_Verb2,
Atest22c_Noun2_Pluralnoun, Atest22f_Pluralnoun_Verb2,
Atest222c_Noun1_Pluralnoun, Atest222f_Verb0_ProgressiveN,
Atest2222c_Noun0_Singularnoun,Atest2222f_Verb1_ProgressiveY,
Atest22222c_Noun1_Pluralnoun, Atest22222f_Verb1_ProgressiveY,
Atest222222c_Noun0_Singularnoun, Atest222222f_Verb0_ProgressiveN,
Atest3c_Verb0, Atest3f_2ndofVerb1_ProgressiveY,
Atest33c_Verb1, Atest33f_2ndofVerb0_ProgressiveN,
Atest333c_Verb0, Atest333f_2ndofNoun0_Singularnoun,
Atest3333c_Verb1, Atest3333f_2ndofNoun1_Pluralnoun,
Atest33333c_Verb0, Atest33333f_2ndofNoun1_Pluralnoun,
Atest333333c_Verb1,Atest333333f_2ndofVerb1_ProgressiveY,
Atest3333333c_Verb0, Atest3333333f_2ndofVerb0_ProgressiveN,
Atest33333333c_Verb1,Atest33333333f_2ndofNoun0_Singularnoun,
Atest4c_Noun1, Atest4f_2ndofNoun1_Pluralnoun ,
Atest44c_Noun0,Atest44f_2ndofNoun0_Singularnoun,
Atest444c_Noun1, Atest444f_2ndofVerb1_ProgressiveY,
Atest4444c_Noun0,Atest4444f_2ndofVerb0_ProgressiveN ,
Atest44444c_Noun1,Atest44444f_2ndofVerb0_ProgressiveN,
Atest444444c_Noun0,Atest444444f_2ndofVerb1_ProgressiveY,
Atest4444444c_Noun1 ,Atest4444444f_2ndofNoun1_Pluralnoun,
Atest44444444c_Noun0,Atest44444444f_2ndofNoun0_Singularnoun
))


Atestnamelist=("Atest1c_Verb2_ProgressiveY_Pluralverb","Atest1f_Pluralnoun_Verb2_ProgressiveY",
"Atest11c_Verb2_ProgressiveY_Singularverb","Atest11f_Singularnoun_Verb2_ProgressiveY",
"Atest111c_Atest1111111c_Verb0_ProgressiveN_Singularverb", "Atest111f_Atest11111111f_Noun1_Pluralnoun_Verb2",
"Atest1111c_Atest11111111c_Verb1_ProgressiveY_Pluralverb","Atest1111111f_Atest1111f_Noun0_Singularnoun_Verb2",
"Atest11111c_Verb2_ProgressiveN_Pluralverb","Atest11111f_Pluralnoun_Verb2_ProgressiveN",
"Atest111111c_Verb2_ProgressiveN_Singularverb", "Atest111111f_Singularnoun_Verb2_ProgressiveN",
"Atest1111111c_Atest111c_Verb0_ProgressiveN_Singularverb", "Atest1111111f_Atest1111f_Noun0_Singularnoun_Verb2",
"Atest11111111c_Atest1111c_Verb1_ProgressiveY_Pluralverb","Atest11111111f_Atest111f_Noun1_Pluralnoun_Verb2",
"Atest2c_Noun2_Singularnoun", "Atest2f_Singularnoun_Verb2",
"Atest22c_Noun2_Pluralnoun", "Atest22f_Pluralnoun_Verb2",
"Atest222c_Noun1_Pluralnoun", "Atest222f_Verb0_ProgressiveN",
"Atest2222c_Noun0_Singularnoun","Atest2222f_Verb1_ProgressiveY",
"Atest22222c_Noun1_Pluralnoun", "Atest22222f_Verb1_ProgressiveY",
"Atest222222c_Noun0_Singularnoun", "Atest222222f_Verb0_ProgressiveN",
"Atest3c_Verb0", "Atest3f_Atest333333f_2ndofVerb1_ProgressiveY",
"Atest33c_Verb1", "Atest33f_Atest3333333f_2ndofVerb0_ProgressiveN",
"Atest333c_Verb0", "Atest333f_Atest33333333f_2ndofNoun0_Singularnoun",
"Atest3333c_Verb1", "Atest3333f_Atest33333f_2ndofNoun1_Pluralnoun",
"Atest33333c_Verb0", "Atest33333f_Atest3333f_2ndofNoun1_Pluralnoun",
"Atest333333c_Verb1","Atest333333f_Atest3f_2ndofVerb1_ProgressiveY",
"Atest3333333c_Verb0", "Atest3333333f_Atest33f_2ndofVerb0_ProgressiveN",
"Atest33333333c_Verb1","Atest33333333f_Atest333f_2ndofNoun0_Singularnoun",
"Atest4c_Noun1", "Atest4f_Atest4444444f_2ndofNoun1_Pluralnoun" ,
"Atest44c_Noun0","Atest44f_Atest44444444f_2ndofNoun0_Singularnoun",
"Atest444c_Noun1", "Atest444f_Atest444444f_2ndofVerb1_ProgressiveY",
"Atest4444c_Noun0","Atest4444f_Atest44444f_2ndofVerb0_ProgressiveN", 
"Atest44444c_Noun1","Atest44444f_Atest4444f_2ndofVerb0_ProgressiveN",
"Atest444444c_Noun0","Atest444444f_Atest444f_2ndofVerb1_ProgressiveY",
"Atest4444444c_Noun1" ,"Atest4444444f_Atest4f_2ndofNoun1_Pluralnoun",
"Atest44444444c_Noun0","Atest44444444f_Atest44f_2ndofNoun0_Singularnoun"
)

print(len(Atest))
print(len(Atestnamelist))





Btest.extend((Btest1c_Verb2_ProgressiveY_Pluralverb,Btest1f_Pluralnoun_Verb2_ProgressiveY,
Btest11c_Verb2_ProgressiveY_Singularverb,Btest11f_Singularnoun_Verb2_ProgressiveY,
Btest111c_Verb0_ProgressiveN_Singularverb, Btest111f_Noun1_Pluralnoun_Verb2,
Btest1111c_Verb1_ProgressiveY_Pluralverb,Btest1111f_Noun0_Singularnoun_Verb2,
Btest11111c_Verb2_ProgressiveN_Pluralverb,Btest11111f_Pluralnoun_Verb2_ProgressiveN,
Btest111111c_Verb2_ProgressiveN_Singularverb, Btest111111f_Singularnoun_Verb2_ProgressiveN,
Btest1111111c_Verb0_ProgressiveN_Singularverb, Btest1111111f_Noun0_Singularnoun_Verb2,
Btest11111111c_Verb1_ProgressiveY_Pluralverb,Btest11111111f_Noun1_Pluralnoun_Verb2,
Btest2c_Noun2_Singularnoun, Btest2f_Singularnoun_Verb2,
Btest22c_Noun2_Pluralnoun, Btest22f_Pluralnoun_Verb2,
Btest222c_Noun1_Pluralnoun, Btest222f_Verb0_ProgressiveN,
Btest2222c_Noun0_Singularnoun,Btest2222f_Verb1_ProgressiveY,
Btest22222c_Noun1_Pluralnoun, Btest22222f_Verb1_ProgressiveY,
Btest222222c_Noun0_Singularnoun, Btest222222f_Verb0_ProgressiveN,
Btest3c_Verb0, Btest3f_2ndofVerb1_ProgressiveY,
Btest33c_Verb1, Btest33f_2ndofVerb0_ProgressiveN,
Btest333c_Verb0, Btest333f_2ndofNoun0_Singularnoun,
Btest3333c_Verb1, Btest3333f_2ndofNoun1_Pluralnoun,
Btest33333c_Verb0, Btest33333f_2ndofNoun1_Pluralnoun,
Btest333333c_Verb1,Btest333333f_2ndofVerb1_ProgressiveY,
Btest3333333c_Verb0, Btest3333333f_2ndofVerb0_ProgressiveN,
Btest33333333c_Verb1,Btest33333333f_2ndofNoun0_Singularnoun,
Btest4c_Noun1, Btest4f_2ndofNoun1_Pluralnoun ,
Btest44c_Noun0,Btest44f_2ndofNoun0_Singularnoun,
Btest444c_Noun1, Btest444f_2ndofVerb1_ProgressiveY,
Btest4444c_Noun0,Btest4444f_2ndofVerb0_ProgressiveN ,
Btest44444c_Noun1,Btest44444f_2ndofVerb0_ProgressiveN,
Btest444444c_Noun0,Btest444444f_2ndofVerb1_ProgressiveY,
Btest4444444c_Noun1 ,Btest4444444f_2ndofNoun1_Pluralnoun,
Btest44444444c_Noun0,Btest44444444f_2ndofNoun0_Singularnoun
))


Btestnamelist=("Btest1c_Verb2_ProgressiveY_Pluralverb","Btest1f_Pluralnoun_Verb2_ProgressiveY",
"Btest11c_Verb2_ProgressiveY_Singularverb","Btest11f_Singularnoun_Verb2_ProgressiveY",
"Btest111c_Btest1111111c_Verb0_ProgressiveN_Singularverb", "Btest111f_Btest11111111f_Noun1_Pluralnoun_Verb2",
"Btest1111c_Btest11111111c_Verb1_ProgressiveY_Pluralverb","Btest1111111f_Btest1111f_Noun0_Singularnoun_Verb2",
"Btest11111c_Verb2_ProgressiveN_Pluralverb","Btest11111f_Pluralnoun_Verb2_ProgressiveN",
"Btest111111c_Verb2_ProgressiveN_Singularverb", "Btest111111f_Singularnoun_Verb2_ProgressiveN",
"Btest1111111c_Btest111c_Verb0_ProgressiveN_Singularverb", "Btest1111111f_Btest1111f_Noun0_Singularnoun_Verb2",
"Btest11111111c_Btest1111c_Verb1_ProgressiveY_Pluralverb","Btest11111111f_Btest111f_Noun1_Pluralnoun_Verb2",
"Btest2c_Noun2_Singularnoun", "Btest2f_Singularnoun_Verb2",
"Btest22c_Noun2_Pluralnoun", "Btest22f_Pluralnoun_Verb2",
"Btest222c_Noun1_Pluralnoun", "Btest222f_Verb0_ProgressiveN",
"Btest2222c_Noun0_Singularnoun","Btest2222f_Verb1_ProgressiveY",
"Btest22222c_Noun1_Pluralnoun", "Btest22222f_Verb1_ProgressiveY",
"Btest222222c_Noun0_Singularnoun", "Btest222222f_Verb0_ProgressiveN",
"Btest3c_Verb0", "Btest3f_Btest333333f_2ndofVerb1_ProgressiveY",
"Btest33c_Verb1", "Btest33f_Btest3333333f_2ndofVerb0_ProgressiveN",
"Btest333c_Verb0", "Btest333f_Btest33333333f_2ndofNoun0_Singularnoun",
"Btest3333c_Verb1", "Btest3333f_Btest33333f_2ndofNoun1_Pluralnoun",
"Btest33333c_Verb0", "Btest33333f_Btest3333f_2ndofNoun1_Pluralnoun",
"Btest333333c_Verb1","Btest333333f_Btest3f_2ndofVerb1_ProgressiveY",
"Btest3333333c_Verb0", "Btest3333333f_Btest33f_2ndofVerb0_ProgressiveN",
"Btest33333333c_Verb1","Btest33333333f_Btest333f_2ndofNoun0_Singularnoun",
"Btest4c_Noun1", "Btest4f_Btest4444444f_2ndofNoun1_Pluralnoun" ,
"Btest44c_Noun0","Btest44f_Btest44444444f_2ndofNoun0_Singularnoun",
"Btest444c_Noun1", "Btest444f_Btest444444f_2ndofVerb1_ProgressiveY",
"Btest4444c_Noun0","Btest4444f_Btest44444f_2ndofVerb0_ProgressiveN", 
"Btest44444c_Noun1","Btest44444f_Btest4444f_2ndofVerb0_ProgressiveN",
"Btest444444c_Noun0","Btest444444f_Btest444f_2ndofVerb1_ProgressiveY",
"Btest4444444c_Noun1" ,"Btest4444444f_Btest4f_2ndofNoun1_Pluralnoun",
"Btest44444444c_Noun0","Btest44444444f_Btest44f_2ndofNoun0_Singularnoun"
)


print(len(Btest))
print(len(Btestnamelist))



Ctest.extend((Ctest1c_Verb2_ProgressiveY_Pluralverb,Ctest1f_Pluralnoun_Verb2_ProgressiveY,
Ctest11c_Verb2_ProgressiveY_Singularverb,Ctest11f_Singularnoun_Verb2_ProgressiveY,
Ctest111c_Verb0_ProgressiveN_Singularverb, Ctest111f_Noun1_Pluralnoun_Verb2,
Ctest1111c_Verb1_ProgressiveY_Pluralverb,Ctest1111f_Noun0_Singularnoun_Verb2,
Ctest11111c_Verb2_ProgressiveN_Pluralverb,Ctest11111f_Pluralnoun_Verb2_ProgressiveN,
Ctest111111c_Verb2_ProgressiveN_Singularverb, Ctest111111f_Singularnoun_Verb2_ProgressiveN,
Ctest1111111c_Verb0_ProgressiveN_Singularverb, Ctest1111111f_Noun0_Singularnoun_Verb2,
Ctest11111111c_Verb1_ProgressiveY_Pluralverb,Ctest11111111f_Noun1_Pluralnoun_Verb2,
Ctest2c_Noun2_Singularnoun, Ctest2f_Singularnoun_Verb2,
Ctest22c_Noun2_Pluralnoun, Ctest22f_Pluralnoun_Verb2,
Ctest222c_Noun1_Pluralnoun, Ctest222f_Verb0_ProgressiveN,
Ctest2222c_Noun0_Singularnoun,Ctest2222f_Verb1_ProgressiveY,
Ctest22222c_Noun1_Pluralnoun, Ctest22222f_Verb1_ProgressiveY,
Ctest222222c_Noun0_Singularnoun, Ctest222222f_Verb0_ProgressiveN,
Ctest3c_Verb0, Ctest3f_2ndofVerb1_ProgressiveY,
Ctest33c_Verb1, Ctest33f_2ndofVerb0_ProgressiveN,
Ctest333c_Verb0, Ctest333f_2ndofNoun0_Singularnoun,
Ctest3333c_Verb1, Ctest3333f_2ndofNoun1_Pluralnoun,
Ctest33333c_Verb0, Ctest33333f_2ndofNoun1_Pluralnoun,
Ctest333333c_Verb1,Ctest333333f_2ndofVerb1_ProgressiveY,
Ctest3333333c_Verb0, Ctest3333333f_2ndofVerb0_ProgressiveN,
Ctest33333333c_Verb1,Ctest33333333f_2ndofNoun0_Singularnoun,
Ctest4c_Noun1, Ctest4f_2ndofNoun1_Pluralnoun ,
Ctest44c_Noun0,Ctest44f_2ndofNoun0_Singularnoun,
Ctest444c_Noun1, Ctest444f_2ndofVerb1_ProgressiveY,
Ctest4444c_Noun0,Ctest4444f_2ndofVerb0_ProgressiveN ,
Ctest44444c_Noun1,Ctest44444f_2ndofVerb0_ProgressiveN,
Ctest444444c_Noun0,Ctest444444f_2ndofVerb1_ProgressiveY,
Ctest4444444c_Noun1 ,Ctest4444444f_2ndofNoun1_Pluralnoun,
Ctest44444444c_Noun0,Ctest44444444f_2ndofNoun0_Singularnoun
))


Ctestnamelist=("Ctest1c_Verb2_ProgressiveY_Pluralverb","Ctest1f_Pluralnoun_Verb2_ProgressiveY",
"Ctest11c_Verb2_ProgressiveY_Singularverb","Ctest11f_Singularnoun_Verb2_ProgressiveY",
"Ctest111c_Ctest1111111c_Verb0_ProgressiveN_Singularverb", "Ctest111f_Ctest11111111f_Noun1_Pluralnoun_Verb2",
"Ctest1111c_Ctest11111111c_Verb1_ProgressiveY_Pluralverb","Ctest1111111f_Ctest1111f_Noun0_Singularnoun_Verb2",
"Ctest11111c_Verb2_ProgressiveN_Pluralverb","Ctest11111f_Pluralnoun_Verb2_ProgressiveN",
"Ctest111111c_Verb2_ProgressiveN_Singularverb", "Ctest111111f_Singularnoun_Verb2_ProgressiveN",
"Ctest1111111c_Ctest111c_Verb0_ProgressiveN_Singularverb", "Ctest1111111f_Ctest1111f_Noun0_Singularnoun_Verb2",
"Ctest11111111c_Ctest1111c_Verb1_ProgressiveY_Pluralverb","Ctest11111111f_Ctest111f_Noun1_Pluralnoun_Verb2",
"Ctest2c_Noun2_Singularnoun", "Ctest2f_Singularnoun_Verb2",
"Ctest22c_Noun2_Pluralnoun", "Ctest22f_Pluralnoun_Verb2",
"Ctest222c_Noun1_Pluralnoun", "Ctest222f_Verb0_ProgressiveN",
"Ctest2222c_Noun0_Singularnoun","Ctest2222f_Verb1_ProgressiveY",
"Ctest22222c_Noun1_Pluralnoun", "Ctest22222f_Verb1_ProgressiveY",
"Ctest222222c_Noun0_Singularnoun", "Ctest222222f_Verb0_ProgressiveN",
"Ctest3c_Verb0", "Ctest3f_Ctest333333f_2ndofVerb1_ProgressiveY",
"Ctest33c_Verb1", "Ctest33f_Ctest3333333f_2ndofVerb0_ProgressiveN",
"Ctest333c_Verb0", "Ctest333f_Ctest33333333f_2ndofNoun0_Singularnoun",
"Ctest3333c_Verb1", "Ctest3333f_Ctest33333f_2ndofNoun1_Pluralnoun",
"Ctest33333c_Verb0", "Ctest33333f_Ctest3333f_2ndofNoun1_Pluralnoun",
"Ctest333333c_Verb1","Ctest333333f_Ctest3f_2ndofVerb1_ProgressiveY",
"Ctest3333333c_Verb0", "Ctest3333333f_Ctest33f_2ndofVerb0_ProgressiveN",
"Ctest33333333c_Verb1","Ctest33333333f_Ctest333f_2ndofNoun0_Singularnoun",
"Ctest4c_Noun1", "Ctest4f_Ctest4444444f_2ndofNoun1_Pluralnoun" ,
"Ctest44c_Noun0","Ctest44f_Ctest44444444f_2ndofNoun0_Singularnoun",
"Ctest444c_Noun1", "Ctest444f_Ctest444444f_2ndofVerb1_ProgressiveY",
"Ctest4444c_Noun0","Ctest4444f_Ctest44444f_2ndofVerb0_ProgressiveN", 
"Ctest44444c_Noun1","Ctest44444f_Ctest4444f_2ndofVerb0_ProgressiveN",
"Ctest444444c_Noun0","Ctest444444f_Ctest444f_2ndofVerb1_ProgressiveY",
"Ctest4444444c_Noun1" ,"Ctest4444444f_Ctest4f_2ndofNoun1_Pluralnoun",
"Ctest44444444c_Noun0","Ctest44444444f_Ctest44f_2ndofNoun0_Singularnoun"
)


print(len(Ctest))
print(len(Ctestnamelist))


Dtest.extend((Dtest1c_Verb2_ProgressiveY_Pluralverb,Dtest1f_Pluralnoun_Verb2_ProgressiveY,
Dtest11c_Verb2_ProgressiveY_Singularverb,Dtest11f_Singularnoun_Verb2_ProgressiveY,
Dtest111c_Verb0_ProgressiveN_Singularverb, Dtest111f_Noun1_Pluralnoun_Verb2,
Dtest1111c_Verb1_ProgressiveY_Pluralverb,Dtest1111f_Noun0_Singularnoun_Verb2,
Dtest11111c_Verb2_ProgressiveN_Pluralverb,Dtest11111f_Pluralnoun_Verb2_ProgressiveN,
Dtest111111c_Verb2_ProgressiveN_Singularverb, Dtest111111f_Singularnoun_Verb2_ProgressiveN,
Dtest1111111c_Verb0_ProgressiveN_Singularverb, Dtest1111111f_Noun0_Singularnoun_Verb2,
Dtest11111111c_Verb1_ProgressiveY_Pluralverb,Dtest11111111f_Noun1_Pluralnoun_Verb2,
Dtest2c_Noun2_Singularnoun, Dtest2f_Singularnoun_Verb2,
Dtest22c_Noun2_Pluralnoun, Dtest22f_Pluralnoun_Verb2,
Dtest222c_Noun1_Pluralnoun, Dtest222f_Verb0_ProgressiveN,
Dtest2222c_Noun0_Singularnoun,Dtest2222f_Verb1_ProgressiveY,
Dtest22222c_Noun1_Pluralnoun, Dtest22222f_Verb1_ProgressiveY,
Dtest222222c_Noun0_Singularnoun, Dtest222222f_Verb0_ProgressiveN,
Dtest3c_Verb0, Dtest3f_2ndofVerb1_ProgressiveY,
Dtest33c_Verb1, Dtest33f_2ndofVerb0_ProgressiveN,
Dtest333c_Verb0, Dtest333f_2ndofNoun0_Singularnoun,
Dtest3333c_Verb1, Dtest3333f_2ndofNoun1_Pluralnoun,
Dtest33333c_Verb0, Dtest33333f_2ndofNoun1_Pluralnoun,
Dtest333333c_Verb1,Dtest333333f_2ndofVerb1_ProgressiveY,
Dtest3333333c_Verb0, Dtest3333333f_2ndofVerb0_ProgressiveN,
Dtest33333333c_Verb1,Dtest33333333f_2ndofNoun0_Singularnoun,
Dtest4c_Noun1, Dtest4f_2ndofNoun1_Pluralnoun ,
Dtest44c_Noun0,Dtest44f_2ndofNoun0_Singularnoun,
Dtest444c_Noun1, Dtest444f_2ndofVerb1_ProgressiveY,
Dtest4444c_Noun0,Dtest4444f_2ndofVerb0_ProgressiveN, 
Dtest44444c_Noun1,Dtest44444f_2ndofVerb0_ProgressiveN,
Dtest444444c_Noun0,Dtest444444f_2ndofVerb1_ProgressiveY,
Dtest4444444c_Noun1 ,Dtest4444444f_2ndofNoun1_Pluralnoun,
Dtest44444444c_Noun0,Dtest44444444f_2ndofNoun0_Singularnoun
))

Dtestnamelist=("Dtest1c_Verb2_ProgressiveY_Pluralverb","Dtest1f_Pluralnoun_Verb2_ProgressiveY",
"Dtest11c_Verb2_ProgressiveY_Singularverb","Dtest11f_Singularnoun_Verb2_ProgressiveY",
"Dtest111c_Dtest1111111c_Verb0_ProgressiveN_Singularverb", "Dtest111f_Dtest11111111f_Noun1_Pluralnoun_Verb2",
"Dtest1111c_Dtest11111111c_Verb1_ProgressiveY_Pluralverb","Dtest1111111f_Dtest1111f_Noun0_Singularnoun_Verb2",
"Dtest11111c_Verb2_ProgressiveN_Pluralverb","Dtest11111f_Pluralnoun_Verb2_ProgressiveN",
"Dtest111111c_Verb2_ProgressiveN_Singularverb", "Dtest111111f_Singularnoun_Verb2_ProgressiveN",
"Dtest1111111c_Dtest111c_Verb0_ProgressiveN_Singularverb", "Dtest1111111f_Dtest1111f_Noun0_Singularnoun_Verb2",
"Dtest11111111c_Dtest1111c_Verb1_ProgressiveY_Pluralverb","Dtest11111111f_Dtest111f_Noun1_Pluralnoun_Verb2",
"Dtest2c_Noun2_Singularnoun", "Dtest2f_Singularnoun_Verb2",
"Dtest22c_Noun2_Pluralnoun", "Dtest22f_Pluralnoun_Verb2",
"Dtest222c_Noun1_Pluralnoun", "Dtest222f_Verb0_ProgressiveN",
"Dtest2222c_Noun0_Singularnoun","Dtest2222f_Verb1_ProgressiveY",
"Dtest22222c_Noun1_Pluralnoun", "Dtest22222f_Verb1_ProgressiveY",
"Dtest222222c_Noun0_Singularnoun", "Dtest222222f_Verb0_ProgressiveN",
"Dtest3c_Verb0", "Dtest3f_Dtest333333f_2ndofVerb1_ProgressiveY",
"Dtest33c_Verb1", "Dtest33f_Dtest3333333f_2ndofVerb0_ProgressiveN",
"Dtest333c_Verb0", "Dtest333f_Dtest33333333f_2ndofNoun0_Singularnoun",
"Dtest3333c_Verb1", "Dtest3333f_Dtest33333f_2ndofNoun1_Pluralnoun",
"Dtest33333c_Verb0", "Dtest33333f_Dtest3333f_2ndofNoun1_Pluralnoun",
"Dtest333333c_Verb1","Dtest333333f_Dtest3f_2ndofVerb1_ProgressiveY",
"Dtest3333333c_Verb0", "Dtest3333333f_Dtest33f_2ndofVerb0_ProgressiveN",
"Dtest33333333c_Verb1","Dtest33333333f_Dtest333f_2ndofNoun0_Singularnoun",
"Dtest4c_Noun1", "Dtest4f_Dtest4444444f_2ndofNoun1_Pluralnoun" ,
"Dtest44c_Noun0","Dtest44f_Dtest44444444f_2ndofNoun0_Singularnoun",
"Dtest444c_Noun1", "Dtest444f_Dtest444444f_2ndofVerb1_ProgressiveY",
"Dtest4444c_Noun0","Dtest4444f_Dtest44444f_2ndofVerb0_ProgressiveN", 
"Dtest44444c_Noun1","Dtest44444f_Dtest4444f_2ndofVerb0_ProgressiveN",
"Dtest444444c_Noun0","Dtest444444f_Dtest444f_2ndofVerb1_ProgressiveY",
"Dtest4444444c_Noun1" ,"Dtest4444444f_Dtest4f_2ndofNoun1_Pluralnoun",
"Dtest44444444c_Noun0","Dtest44444444f_Dtest44f_2ndofNoun0_Singularnoun"
)


print(len(Dtest))
print(len(Dtestnamelist))


#trainstim(ASentence, Atrainnamelist, "A")
#trainstim(BSentence, Btrainnamelist, "B")
#trainstim(CSentence, Ctrainnamelist, "C")
trainstim(DSentence, Dtrainnamelist, "D")

#teststim(Atest, Atestnamelist, "A")
#teststim(Btest, Btestnamelist, "B")
#teststim(Ctest, Ctestnamelist, "C")
#teststim(Dtest, Dtestnamelist, "D")

#for element in Btest:
#	testoutput.write(element + str("\n"))


##########################





#######

#######LANGUAGE
#for cons in consonants:
#  consonant_list=[]
#  for vowel in vowels: 
#     consonant_list.append(str(cons)+str(vowel))
#  Syllables.append(consonant_list)
#print(Syllables)

#vowels=["a", "e", "i", "o", "u"]
#consonants=["b","d","f","g","k","l","m","n","p","s","t","v","w","sh"]
#for syllableGroup in Syllables:
#   Use.append(random.sample(syllableGroup, k=1))
#random.shuffle(Syllables)
#random.shuffle(Syllables)

