from os import system
import random

trainoutput=open("/Users/lscpuser/Documents/ALSE/output.csv", 'a')

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

def trainstim(sentence, name):
 count=0
 for element in sentence:
  trainoutput.write(element + str("\n"))
  element=stringtoPhon(element)
  print(element)
  print(count)
  print(Atrainnamelist[count])
  system('say -o  ~/Documents/ALSE/pilot5/train/{}.aiff  {}'.format(name[count], element)) 
  count=count+1

def teststim(list, name):
 count=0
 for example in list:
   #  example=stringtoPhon(example)
   system('say -o  ~/Documents/ALSE/pilot5/test/{}.aiff  {}'.format(name[count],  example))
   count=count+1
   
   
   
   
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

print(ANoun, AVerb, ADisrupter1, ADisrupter2, ASingularNoun, ASingularVerb, APluralNoun, APluralVerb, AProgressiveY, AProgressiveN)

##########Group B

BNoun.append(str(Syllables[17]+ Syllables[16]))
BNoun.append(str(Syllables[15]+ Syllables[14]))
BNoun.append(str(Syllables[13]))


BVerb.append(str(Syllables[12]+ Syllables[11]))
BVerb.append(str(Syllables[10]+ Syllables[9]))
BVerb.append(str(Syllables[8]))


BDisrupter1.append("")
BDisrupter1.append(str(Syllables[7]))
BDisrupter2.append("")
BDisrupter2.append(str(Syllables[6]))



BSingularNoun= str(Syllables[5])
BSingularVerb= str(Syllables[4])
BPluralNoun= str(Syllables[3])
BPluralVerb=  str(Syllables[2])
BProgressiveY= str(Syllables[1])
BProgressiveN= str(Syllables[0])


#print(BNoun, BVerb, BDisrupter1, BDisrupter2, BSingularNoun, BSingularVerb, BPluralNoun, BPluralVerb, BProgressiveY, BProgressiveN)


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

#print(CNoun, CVerb, CDisrupter1, CDisrupter2, CSingularNoun, CSingularVerb, CPluralNoun, CPluralVerb, CProgressiveY, CProgressiveN)



##############Group 4 

DNoun.append(str(Syllables[8]+ Syllables[9]))
DNoun.append(str(Syllables[10]+ Syllables[11]))
DNoun.append(str(Syllables[12]))


DVerb.append(str(Syllables[13]+ Syllables[14]))
DVerb.append(str(Syllables[15]+ Syllables[16]))
DVerb.append(str(Syllables[17]))


DDisrupter1.append("")
DDisrupter1.append(str(Syllables[0]))
DDisrupter2.append("")
DDisrupter2.append(str(Syllables[1]))



DSingularNoun= str(Syllables[2])
DSingularVerb= str(Syllables[3])
DPluralNoun= str(Syllables[4])
DPluralVerb=  str(Syllables[5])
DProgressiveY= str(Syllables[6])
DProgressiveN= str(Syllables[7])


#print(DNoun, DVerb, DDisrupter1, DDisrupter2, DSingularNoun, DSingularVerb, DPluralNoun, DPluralVerb, DProgressiveY, DProgressiveN)



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



#B

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


#for N in DNoun:
 # for V in DVerb:
  #   DSentence.append(random.choice(DDisrupter1)+ " - " + N + DSingularNoun + " - " +  V + DProgressiveY + DSingularVerb + " - " + random.choice(DDisrupter2))
   #  DSentence.append(random.choice(DDisrupter1)+ " - " + N + DPluralNoun + " - " + V + DProgressiveY + DPluralVerb + " - " + random.choice(DDisrupter2))
   #  DSentence.append(random.choice(DDisrupter1)+ " - " + N + DSingularNoun + " - " + V + DProgressiveN + DSingularVerb + " - " + random.choice(DDisrupter2))
    # DSentence.append(random.choice(DDisrupter1)+ " - " + N + DPluralNoun + " - " + V + DProgressiveN + DPluralVerb + " - " + random.choice(DDisrupter2))



Atrainnamelist=["A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter0_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter0_noun0_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter0_2",
"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter0_2",
"A_Disrupter0_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0_2",
"A_Disrupter0_noun0_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter0_2",
"A_Disrupter0_noun1_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter0_noun1_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter0",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter0",
"A_Disrupter0_noun1_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter0_2",
"A_Disrupter0_noun1_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter0_2",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter0_2",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter0_2",
"A_Disrupter0_noun2_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter0_noun2_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter0_noun2_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter0",
"A_Disrupter0_noun2_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter0_noun2_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter0_noun2_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter0_noun2_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter0_noun2_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter0",

"A_Disrupter1_noun0_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter1_noun0_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter1_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter1_noun0_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter1_noun0_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter0_2",
"A_Disrupter1_noun0_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter0_2",
"A_Disrupter1_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0_2",
"A_Disrupter1_noun0_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter0_2",
"A_Disrupter1_noun1_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter1_noun1_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter0",
"A_Disrupter1_noun1_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter1_noun1_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter0",
"A_Disrupter1_noun1_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter0_2",
"A_Disrupter1_noun1_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter0_2",
"A_Disrupter1_noun1_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter0_2",
"A_Disrupter1_noun1_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter0_2",
"A_Disrupter1_noun2_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter1_noun2_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter1_noun2_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter0",
"A_Disrupter1_noun2_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter1_noun2_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter0",
"A_Disrupter1_noun2_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter0",
"A_Disrupter1_noun2_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter0",
"A_Disrupter1_noun2_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter0",

"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter1",
"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter1",
"A_Disrupter0_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter1",
"A_Disrupter0_noun0_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter1",
"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter1_2",
"A_Disrupter0_noun0_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter1_2",
"A_Disrupter0_noun0_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter1_2",
"A_Disrupter0_noun0_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter1_2",
"A_Disrupter0_noun1_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter1",
"A_Disrupter0_noun1_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter1",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter1",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter1",
"A_Disrupter0_noun1_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter1_2",
"A_Disrupter0_noun1_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter1_2",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter1_2",
"A_Disrupter0_noun1_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter1_2",
"A_Disrupter0_noun2_Singularnoun_verb2_ProgressiveN_Singularverb_Disrupter1",
"A_Disrupter0_noun2_Singularnoun_verb2_ProgressiveY_Singularverb_Disrupter1",
"A_Disrupter0_noun2_Pluralnoun_verb2_ProgressiveN_Pluralverb_Disrupter1",
"A_Disrupter0_noun2_Pluralnoun_verb2_ProgressiveY_Pluralverb_Disrupter1",
"A_Disrupter0_noun2_Singularnoun_verb1_ProgressiveY_Singularverb_Disrupter1",
"A_Disrupter0_noun2_Pluralnoun_verb1_ProgressiveY_Pluralverb_Disrupter1",
"A_Disrupter0_noun2_Singularnoun_verb0_ProgressiveN_Singularverb_Disrupter1",
"A_Disrupter0_noun2_Pluralnoun_verb0_ProgressiveN_Pluralverb_Disrupter1"]



trainstim(ASentence, Atrainnamelist)
"""
trainstim(BSentence,  Btrainnamelist)
trainstim(CSentence,  Ctrainnamelist)
trainstim(DSentence, Dtrainnamelist)
"""


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
 


#noun vs non-noun
Atest2c_Noun2_Singularnoun = ANoun[2] + ASingularNoun
Atest2f_Singularnoun_Verb2 = ASingularNoun + AVerb[2]

Atest22c_Noun2_Pluralnoun = ANoun[2] + APluralNoun
Atest22f_Pluralnoun_Verb2 = APluralNoun + AVerb[2]

Atest222c_Noun1_Pluralnoun = ANoun[1] + APluralNoun
Atest222f_2ndofVerb0_ProgressiveN  = str(Syllables[1]) + AProgressiveN

Atest2222c_Noun0_Singularnoun = ANoun[0] + ASingularNoun
Atest2222f_2ndofVerb1_ProgressiveY  = str(Syllables[3]) + AProgressiveY



#verbstem vs non-verbstem

Atest3c_Verb0  = AVerb[0]
Atest3f_2ndofVerb0_ProgressiveN = str(Syllables[6]) + AProgressiveN

Atest33c_Verb1  = AVerb[1]
Atest33f_2ndofVerb1_ProgressiveY = str(Syllables[8]) + AProgressiveY

Atest333c_Verb0  = AVerb[0]
Atest333f_2ndofNoun0_Singularnoun  =  str(Syllables[1]) + ASingularNoun

Atest3333c_Verb0  = AVerb[0]
Atest3333f_2ndofVerb1_ProgressiveY = str(Syllables[8]) + AProgressiveY

Atest33333c__Verb1  = AVerb[1]
Atest33333f_2ndofVerb0_ProgressiveN = str(Syllables[6]) + AProgressiveN

Atest333333c_Verb1  = AVerb[1]
Atest333333f_2ndofNoun1_Pluralnoun  =  str(Syllables[3]) + APluralNoun



#nounstem vs  non-nounstem

Atest4c_Noun1 = ANoun[1]
Atest4f_2ndofNoun1_Pluralnoun  =  str(Syllables[3]) + APluralNoun

Atest44c_Noun0 = ANoun[0]
Atest44f_2ndofNoun0_Singularnoun  =  str(Syllables[1]) + ASingularNoun

Atest444c_Noun1 =  ANoun[1]
Atest444f_2ndofVerb1_ProgressiveY = str(Syllables[8]) + AProgressiveY

Atest4444c_Noun0 =  ANoun[0]
Atest4444f_2ndofNoun1_Pluralnoun  =  str(Syllables[3]) + APluralNoun

Atest44444c_Noun0 =  ANoun[0]
Atest44444f_2ndofVerb0_ProgressiveN = str(Syllables[6]) + AProgressiveN

Atest444444c_Noun1 = ANoun[1]
Atest444444f_2ndofNoun0_Singularnoun  =  str(Syllables[1]) + ASingularNoun


Atest.extend((Atest1c_Verb2_ProgressiveY_Pluralverb,Atest1f_Pluralnoun_Verb2_ProgressiveY,
Atest11c_Verb2_ProgressiveY_Singularverb, Atest11f_Singularnoun_Verb2_ProgressiveY, 
Atest111c_Verb0_ProgressiveN_Singularverb, Atest111f_Noun1_Pluralnoun_Verb2,
Atest1111c_Verb1_ProgressiveY_Pluralverb,  Atest1111f_Noun0_Singularnoun_Verb2,
Atest11111c_Verb2_ProgressiveN_Pluralverb, Atest11111f_Pluralnoun_Verb2_ProgressiveN,
Atest111111c_Verb2_ProgressiveN_Singularverb, Atest111111f_Singularnoun_Verb2_ProgressiveN,
Atest2c_Noun2_Singularnoun, Atest2f_Singularnoun_Verb2,
Atest22c_Noun2_Pluralnoun, Atest22f_Pluralnoun_Verb2,
Atest222c_Noun1_Pluralnoun, Atest222f_2ndofVerb0_ProgressiveN,
Atest2222c_Noun0_Singularnoun,  Atest2222f_2ndofVerb1_ProgressiveY,
Atest3c_Verb0, Atest3f_2ndofVerb0_ProgressiveN,
Atest33c_Verb1, Atest33f_2ndofVerb1_ProgressiveY,
Atest333c_Verb0, Atest333f_2ndofNoun0_Singularnoun,
Atest3333c_Verb0, Atest3333f_2ndofVerb1_ProgressiveY,
Atest33333c__Verb1, Atest33333f_2ndofVerb0_ProgressiveN,
Atest333333c_Verb1, Atest333333f_2ndofNoun1_Pluralnoun,
Atest4c_Noun1, Atest4f_2ndofNoun1_Pluralnoun,
Atest44c_Noun0, Atest44f_2ndofNoun0_Singularnoun,
Atest444c_Noun1, Atest444f_2ndofVerb1_ProgressiveY,
Atest4444c_Noun0, Atest4444f_2ndofNoun1_Pluralnoun,
Atest44444c_Noun0, Atest44444f_2ndofVerb0_ProgressiveN,
Atest444444c_Noun1, Atest444444f_2ndofNoun0_Singularnoun))


Atestnamelist=("Atest1c_Verb2_ProgressiveY_Pluralverb","Atest1f_Pluralnoun_Verb2_ProgressiveY",
"Atest11c_Verb2_ProgressiveY_Singularverb", "Atest11f_Singularnoun_Verb2_ProgressiveY", 
"Atest111c_Verb0_ProgressiveN_Singularverb", "Atest111f_Noun1_Pluralnoun_Verb2",
"Atest1111c_Verb1_ProgressiveY_Pluralverb",  "Atest1111f_Noun0_Singularnoun_Verb2",
"Atest11111c_Verb2_ProgressiveN_Pluralverb", "Atest11111f_Pluralnoun_Verb2_ProgressiveN",
"Atest111111c_Verb2_ProgressiveN_Singularverb", "Atest111111f_Singularnoun_Verb2_ProgressiveN",
"Atest2c_Noun2_Singularnoun", "Atest2f_Singularnoun_Verb2",
"Atest22c_Noun2_Pluralnoun", "Atest22f_Pluralnoun_Verb2",
"Atest222c_Noun1_Pluralnoun", "Atest222f_2ndofVerb0_ProgressiveN",
"Atest2222c_Noun0_Singularnoun",  "Atest2222f_2ndofVerb1_ProgressiveY",
"Atest3c_Verb0", "Atest3f_2ndofVerb0_ProgressiveN",
"Atest33c_Verb1", "Atest33f_2ndofVerb1_ProgressiveY",
"Atest333c_Verb0", "Atest333f_2ndofNoun0_Singularnoun",
"Atest3333c_Verb0", "Atest3333f_2ndofVerb1_ProgressiveY",
"Atest33333c__Verb1", "Atest33333f_2ndofVerb0_ProgressiveN",
"Atest333333c_Verb1", "Atest333333f_2ndofNoun1_Pluralnoun",
"Atest4c_Noun1", "Atest4f_2ndofNoun1_Pluralnoun",
"Atest44c_Noun0", "Atest44f_2ndofNoun0_Singularnoun",
"Atest444c_Noun1", "Atest444f_2ndofVerb1_ProgressiveY",
"Atest4444c_Noun0", "Atest4444f_2ndofNoun1_Pluralnoun",
"Atest44444c_Noun0", "Atest44444f_2ndofVerb0_ProgressiveN",
"Atest444444c_Noun1", "Atest444444f_2ndofNoun0_Singularnoun")


teststim(Atest, Atestnamelist)



"""
teststim(Btest,  Btestnamelist)
teststim(Ctest,  Ctestnamelist)
teststim(Dtest,  Dtestnamelist)

"""
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
