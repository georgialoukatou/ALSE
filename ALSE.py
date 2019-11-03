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
  system('say -o  ~/Documents/ALSE/pilot4/train/{}.aiff  {}'.format(name[count], element)) 
  count=count+1

def teststim(list, name):
 count=0
 for example in list:
   #  example=stringtoPhon(example)
   system('say -o  ~/Documents/ALSE/pilot4/test/{}.aiff  {}'.format(name[count],  example))
   count=count+1
   
   
   
   
Syllables=["dlu",  "ga",  "sin",  "blu", "ko", "dle", "ti", "man", "gle", "blo", "da", "pun", "kli", "go", "tla", "fen", "bi", "glu"]

######################PREP PHASE
#######Group  A


ANoun.append(str(Syllables[0]+ Syllables[1]))
ANoun.append(str(Syllables[2]+ Syllables[3]))
ANoun.append(str(Syllables[4]))


AVerb.append(str(Syllables[5]+ Syllables[6]))
AVerb.append(str(Syllables[7]+ Syllables[8]))
AVerb.append(str(Syllables[9]))


ADisrupter1.append(str(Syllables[10]))
ADisrupter1.append("")
ADisrupter2.append(str(Syllables[11]))
ADisrupter2.append("")


ASingularNoun= str(Syllables[12])
ASingularVerb= str(Syllables[13])
APluralNoun= str(Syllables[14])
APluralVerb=  str(Syllables[15])
AProgressiveY= str(Syllables[16])
AProgressiveN= str(Syllables[17])

#print("ANoun, AVerb, ADisrupter1, ADisrupter2, ASingularNoun, ASingularVerb, APluralNoun, APluralVerb, AProgressiveY, AProgressiveN")
print(ANoun, AVerb, ADisrupter1, ADisrupter2, ASingularNoun, ASingularVerb, APluralNoun, APluralVerb, AProgressiveY, AProgressiveN)

##########Group B

BNoun.append(str(Syllables[17]+ Syllables[16]))
BNoun.append(str(Syllables[15]+ Syllables[14]))
BNoun.append(str(Syllables[13]))


BVerb.append(str(Syllables[12]+ Syllables[11]))
BVerb.append(str(Syllables[10]+ Syllables[9]))
BVerb.append(str(Syllables[8]))


BDisrupter1.append(str(Syllables[7]))
BDisrupter1.append("")
BDisrupter2.append(str(Syllables[6]))
BDisrupter2.append("")


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


CDisrupter1.append(str(Syllables[17]))
CDisrupter1.append("")
CDisrupter2.append(str(Syllables[16]))
CDisrupter2.append("")


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


DDisrupter1.append(str(Syllables[0]))
DDisrupter1.append("")
DDisrupter2.append(str(Syllables[1]))
DDisrupter2.append("")


DSingularNoun= str(Syllables[2])
DSingularVerb= str(Syllables[3])
DPluralNoun= str(Syllables[4])
DPluralVerb=  str(Syllables[5])
DProgressiveY= str(Syllables[6])
DProgressiveN= str(Syllables[7])


#print(DNoun, DVerb, DDisrupter1, DDisrupter2, DSingularNoun, DSingularVerb, DPluralNoun, DPluralVerb, DProgressiveY, DProgressiveN)



#############################################TRAINING

for N in ANoun:
  for V in AVerb:
     ASentence.append(random.choice(ADisrupter1)+ " - " + N + ASingularNoun + " - " +  V + AProgressiveY + ASingularVerb + " - " + random.choice(ADisrupter2))
     ASentence.append(random.choice(ADisrupter1)+ " - " + N + APluralNoun + " - " + V + AProgressiveY + APluralVerb + " - " + random.choice(ADisrupter2))
     ASentence.append(random.choice(ADisrupter1)+ " - " + N + ASingularNoun + " - " + V + AProgressiveN + ASingularVerb + " - " + random.choice(ADisrupter2))
     ASentence.append(random.choice(ADisrupter1)+ " - " + N + APluralNoun + " - " + V + AProgressiveN + APluralVerb + " - " + random.choice(ADisrupter2))


for N in BNoun:
  for V in BVerb:
     BSentence.append(random.choice(BDisrupter1)+ " - " + N + BSingularNoun + " - " +  V + BProgressiveY + BSingularVerb + " - " + random.choice(BDisrupter2))
     BSentence.append(random.choice(BDisrupter1)+ " - " + N + BPluralNoun + " - " + V + BProgressiveY + BPluralVerb + " - " + random.choice(BDisrupter2))
     BSentence.append(random.choice(BDisrupter1)+ " - " + N + BSingularNoun + " - " + V + BProgressiveN + BSingularVerb + " - " + random.choice(BDisrupter2))
     BSentence.append(random.choice(BDisrupter1)+ " - " + N + BPluralNoun + " - " + V + BProgressiveN + BPluralVerb + " - " + random.choice(BDisrupter2))

for N in CNoun:
  for V in CVerb:
     CSentence.append(random.choice(CDisrupter1)+ " - " + N + CSingularNoun + " - " +  V + CProgressiveY + CSingularVerb + " - " + random.choice(CDisrupter2))
     CSentence.append(random.choice(CDisrupter1)+ " - " + N + CPluralNoun + " - " + V + CProgressiveY + CPluralVerb + " - " + random.choice(CDisrupter2))
     CSentence.append(random.choice(CDisrupter1)+ " - " + N + CSingularNoun + " - " + V + CProgressiveN + CSingularVerb + " - " + random.choice(CDisrupter2))
     CSentence.append(random.choice(CDisrupter1)+ " - " + N + CPluralNoun + " - " + V + CProgressiveN + CPluralVerb + " - " + random.choice(CDisrupter2))

for N in DNoun:
  for V in DVerb:
     DSentence.append(random.choice(DDisrupter1)+ " - " + N + DSingularNoun + " - " +  V + DProgressiveY + DSingularVerb + " - " + random.choice(DDisrupter2))
     DSentence.append(random.choice(DDisrupter1)+ " - " + N + DPluralNoun + " - " + V + DProgressiveY + DPluralVerb + " - " + random.choice(DDisrupter2))
     DSentence.append(random.choice(DDisrupter1)+ " - " + N + DSingularNoun + " - " + V + DProgressiveN + DSingularVerb + " - " + random.choice(DDisrupter2))
     DSentence.append(random.choice(DDisrupter1)+ " - " + N + DPluralNoun + " - " + V + DProgressiveN + DPluralVerb + " - " + random.choice(DDisrupter2))



Atrainnamelist=["Anoun0_Singularnoun_verb0_ProgressiveY_Singularverb","Anoun0_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Anoun0_Singularnoun_verb0_ProgressiveN_Singularverb","Anoun0_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Anoun0_Singularnoun_verb1_ProgressiveY_Singularverb", "Anoun0_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Anoun0_Singularnoun_verb1_ProgressiveN_Singularverb", "Anoun0_Pluralnoun_verb1_ProgressiveN_Pluralverb", "Anoun0_Singularnoun_verb2_ProgressiveY_Singularverb","Anoun0_Pluralnoun_verb2_ProgressiveY_Pluralverb", "Anoun0_Singularnoun_verb2_ProgressiveN_Singularverb","Anoun0_Pluralnoun_verb2_ProgressiveN_Pluralverb", "Anoun1_Singularnoun_verb0_ProgressiveY_Singularverb","Anoun1_Pluralnoun_verb0_ProgressiveY_Pluralverb","Anoun1_Singularnoun_verb0_ProgressiveN_Singularverb","Anoun1_Pluralnoun_verb0_ProgressiveN_Pluralverb",  "Anoun1_Singularnoun_verb1_ProgressiveY_Singularverb", "Anoun1_Pluralnoun_verb1_ProgressiveY_Pluralverb",  "Anoun1_Singularnoun_verb1_ProgressiveN_Singularverb", "Anoun1_Pluralnoun_verb1_ProgressiveN_Pluralverb",   "Anoun1_Singularnoun_verb2_ProgressiveY_Singularverb","Anoun1_Pluralnoun_verb2_ProgressiveY_Pluralverb",  "Anoun1_Singularnoun_verb2_ProgressiveN_Singularverb","Anoun1_Pluralnoun_verb2_ProgressiveN_Pluralverb",    "Anoun2_Singularnoun_verb0_ProgressiveY_Singularverb","Anoun2_Pluralnoun_verb0_ProgressiveY_Pluralverb",      "Anoun2_Singularnoun_verb0_ProgressiveN_Singularverb","Anoun2_Pluralnoun_verb0_ProgressiveN_Pluralverb",      "Anoun2_Singularnoun_verb1_ProgressiveY_Singularverb", "Anoun2_Pluralnoun_verb1_ProgressiveY_Pluralverb",       "Anoun2_Singularnoun_verb1_ProgressiveN_Singularverb", "Anoun2_Pluralnoun_verb1_ProgressiveN_Pluralverb",        "Anoun2_Singularnoun_verb2_ProgressiveY_Singularverb","Anoun2_Pluralnoun_verb2_ProgressiveY_Pluralverb",      "Anoun2_Singularnoun_verb2_ProgressiveN_Singularverb","Anoun2_Pluralnoun_verb2_ProgressiveN_Pluralverb"]
Btrainnamelist=["Bnoun0_Singularnoun_verb0_ProgressiveY_Singularverb","Bnoun0_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Bnoun0_Singularnoun_verb0_ProgressiveN_Singularverb","Bnoun0_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Bnoun0_Singularnoun_verb1_ProgressiveY_Singularverb", "Bnoun0_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Bnoun0_Singularnoun_verb1_ProgressiveN_Singularverb", "Bnoun0_Pluralnoun_verb1_ProgressiveN_Pluralverb", "Bnoun0_Singularnoun_verb2_ProgressiveY_Singularverb","Bnoun0_Pluralnoun_verb2_ProgressiveY_Pluralverb", "Bnoun0_Singularnoun_verb2_ProgressiveN_Singularverb", "Bnoun0_Pluralnoun_verb2_ProgressiveN_Pluralverb", "Bnoun1_Singularnoun_verb0_ProgressiveY_Singularverb","Bnoun1_Pluralnoun_verb0_ProgressiveY_Pluralverb",  "Bnoun1_Singularnoun_verb0_ProgressiveN_Singularverb", "Bnoun1_Pluralnoun_verb0_ProgressiveN_Pluralverb",  "Bnoun1_Singularnoun_verb1_ProgressiveY_Singularverb", "Bnoun1_Pluralnoun_verb1_ProgressiveY_Pluralverb",  "Bnoun1_Singularnoun_verb1_ProgressiveN_Singularverb",  "Bnoun1_Pluralnoun_verb1_ProgressiveN_Pluralverb",  "Bnoun1_Singularnoun_verb2_ProgressiveY_Singularverb","Bnoun1_Pluralnoun_verb2_ProgressiveY_Pluralverb",  "Bnoun1_Singularnoun_verb2_ProgressiveN_Singularverb", "Bnoun1_Pluralnoun_verb2_ProgressiveN_Pluralverb",   "Bnoun2_Singularnoun_verb0_ProgressiveY_Singularverb","Bnoun2_Pluralnoun_verb0_ProgressiveY_Pluralverb",  "Bnoun2_Singularnoun_verb0_ProgressiveN_Singularverb","Bnoun2_Pluralnoun_verb0_ProgressiveN_Pluralverb",    "Bnoun2_Singularnoun_verb1_ProgressiveY_Singularverb", "Bnoun2_Pluralnoun_verb1_ProgressiveY_Pluralverb",     "Bnoun2_Singularnoun_verb1_ProgressiveN_Singularverb", "Bnoun2_Pluralnoun_verb1_ProgressiveN_Pluralverb",    "Bnoun2_Singularnoun_verb2_ProgressiveY_Singularverb","Bnoun2_Pluralnoun_verb2_ProgressiveY_Pluralverb",    "Bnoun2_Singularnoun_verb2_ProgressiveN_Singularverb","Bnoun2_Pluralnoun_verb2_ProgressiveN_Pluralverb"]
Ctrainnamelist=["Cnoun0_Singularnoun_verb0_ProgressiveY_Singularverb","Cnoun0_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Cnoun0_Singularnoun_verb0_ProgressiveN_Singularverb","Cnoun0_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Cnoun0_Singularnoun_verb1_ProgressiveY_Singularverb", "Cnoun0_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Cnoun0_Singularnoun_verb1_ProgressiveN_Singularverb", "Cnoun0_Pluralnoun_verb1_ProgressiveN_Pluralverb","Cnoun0_Singularnoun_verb2_ProgressiveY_Singularverb","Cnoun0_Pluralnoun_verb2_ProgressiveY_Pluralverb","Cnoun0_Singularnoun_verb2_ProgressiveN_Singularverb", "Cnoun0_Pluralnoun_verb2_ProgressiveN_Pluralverb","Cnoun1_Singularnoun_verb0_ProgressiveY_Singularverb","Cnoun1_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Cnoun1_Singularnoun_verb0_ProgressiveN_Singularverb", "Cnoun1_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Cnoun1_Singularnoun_verb1_ProgressiveY_Singularverb", "Cnoun1_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Cnoun1_Singularnoun_verb1_ProgressiveN_Singularverb",  "Cnoun1_Pluralnoun_verb1_ProgressiveN_Pluralverb","Cnoun1_Singularnoun_verb2_ProgressiveY_Singularverb","Cnoun1_Pluralnoun_verb2_ProgressiveY_Pluralverb","Cnoun1_Singularnoun_verb2_ProgressiveN_Singularverb", "Cnoun1_Pluralnoun_verb2_ProgressiveN_Pluralverb", "Cnoun2_Singularnoun_verb0_ProgressiveY_Singularverb","Bnoun2_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Cnoun2_Singularnoun_verb0_ProgressiveN_Singularverb","Cnoun2_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Cnoun2_Singularnoun_verb1_ProgressiveY_Singularverb", "Bnoun2_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Cnoun2_Singularnoun_verb1_ProgressiveN_Singularverb", "Cnoun2_Pluralnoun_verb1_ProgressiveN_Pluralverb","Cnoun2_Singularnoun_verb2_ProgressiveY_Singularverb","Cnoun2_Pluralnoun_verb2_ProgressiveY_Pluralverb","Cnoun2_Singularnoun_verb2_ProgressiveN_Singularverb","Cnoun2_Pluralnoun_verb2_ProgressiveN_Pluralverb"]
Dtrainnamelist=["Dnoun0_Singularnoun_verb0_ProgressiveY_Singularverb","Dnoun0_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Dnoun0_Singularnoun_verb0_ProgressiveN_Singularverb","Dnoun0_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Dnoun0_Singularnoun_verb1_ProgressiveY_Singularverb", "Dnoun0_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Dnoun0_Singularnoun_verb1_ProgressiveN_Singularverb", "Dnoun0_Pluralnoun_verb1_ProgressiveN_Pluralverb","Dnoun0_Singularnoun_verb2_ProgressiveY_Singularverb","Dnoun0_Pluralnoun_verb2_ProgressiveY_Pluralverb","Dnoun0_Singularnoun_verb2_ProgressiveN_Singularverb", "Dnoun0_Pluralnoun_verb2_ProgressiveN_Pluralverb","Dnoun1_Singularnoun_verb0_ProgressiveY_Singularverb","Dnoun1_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Dnoun1_Singularnoun_verb0_ProgressiveN_Singularverb", "Dnoun1_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Dnoun1_Singularnoun_verb1_ProgressiveY_Singularverb", "Dnoun1_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Dnoun1_Singularnoun_verb1_ProgressiveN_Singularverb",  "Dnoun1_Pluralnoun_verb1_ProgressiveN_Pluralverb","Dnoun1_Singularnoun_verb2_ProgressiveY_Singularverb","Dnoun1_Pluralnoun_verb2_ProgressiveY_Pluralverb","Dnoun1_Singularnoun_verb2_ProgressiveN_Singularverb", "Dnoun1_Pluralnoun_verb2_ProgressiveN_Pluralverb", "Dnoun2_Singularnoun_verb0_ProgressiveY_Singularverb","Dnoun2_Pluralnoun_verb0_ProgressiveY_Pluralverb", "Dnoun2_Singularnoun_verb0_ProgressiveN_Singularverb","Dnoun2_Pluralnoun_verb0_ProgressiveN_Pluralverb", "Dnoun2_Singularnoun_verb1_ProgressiveY_Singularverb", "Dnoun2_Pluralnoun_verb1_ProgressiveY_Pluralverb", "Dnoun2_Singularnoun_verb1_ProgressiveN_Singularverb", "Dnoun2_Pluralnoun_verb1_ProgressiveN_Pluralverb","Dnoun2_Singularnoun_verb2_ProgressiveY_Singularverb","Dnoun2_Pluralnoun_verb2_ProgressiveY_Pluralverb","Dnoun2_Singularnoun_verb2_ProgressiveN_Singularverb","Dnoun2_Pluralnoun_verb2_ProgressiveN_Pluralverb"]



#trainstim(ASentence, Atrainnamelist)
"""
trainstim(BSentence,  Btrainnamelist)
trainstim(CSentence,  Ctrainnamelist)
trainstim(DSentence, Dtrainnamelist)
"""

#############TEST

##GroupA
#verb vs non-verb
Atest1c_Verb0_ProgressiveY_Pluralverb = AVerb[0] + AProgressiveY + APluralVerb
Atest1f_Pluralnoun_Verb0_ProgressiveY = APluralNoun + AVerb[0] + AProgressiveY

Atest11c_Verb2_ProgressiveN_Singularverb = AVerb[2] + AProgressiveN + ASingularVerb
Atest11f_Pluralnoun_Verb2_ProgressiveN = APluralNoun + AVerb[2] + AProgressiveN

#Atest111c_Verb1_ProgressiveY_Singularverb = AVerb[1] + AProgressiveY + ASingularVerb
#Atest111f_2syllOFverb1_ProgressiveY_Singularverb_Disruptor2 =  str(AVerb[1])[1:3] +  AProgressiveY + ASingularVerb + ADisrupter2[0]



#noun vs non-word
Atest2c_Noun0_Singularnoun = ANoun[0] + ASingularNoun
Atest2f_Singularnoun_Verb2_ProgressiveN = ASingularNoun+ AVerb[2] + AProgressiveN

Atest22c_Noun1_Pluralnoun = ANoun[1] + APluralNoun
Atest22f_Pluralnoun_Verb2_ProgressiveY = APluralNoun + AVerb[2] + AProgressiveY

#Atest222c_Noun0_PluralNoun = ANoun[0] +  APluralNoun
#Atest222f_Disruptor1_Noun0 = ADisrupter1[0] + ANoun[0] 


#morpheme vs non-morpheme
Atest3c_ProgressiveY_PluralVerb=AProgressiveY + APluralVerb
Atest3f_Pluralnoun_1syllOFverb1=APluralNoun +  str(AVerb[1])[0:3]  #first syllable of 2 syllable  verb DOESNT WORK

Atest33c_ProgressiveN_SingularVerb= AProgressiveN + ASingularVerb
Atest33f_SingularNoun_1syllOFverb0= ASingularNoun + str(AVerb[0])[0:3] #first syllable of 2 syllable  verb DOESNT WORK

Atest333c_ProgressiveY_SingularVerb = AProgressiveY + ASingularVerb
Atest333f_2syllOFverb1_SingularVerb =   str(AVerb[1])[3:6]  + AProgressiveY 

Atest3333c_ProgressiveN_PluralVerb = AProgressiveN + APluralVerb
Atest3333f_2syllOFverb0_ProgressiveN =   str(AVerb[0])[3:5]  + AProgressiveN 

#noun vs morpheme
Atest4c_Noun2_SingularNoun=ANoun[2]  + ASingularNoun
Atest4f_ProgressiveN_SingularVerb=AProgressiveN + ASingularVerb


Atest44c_Noun2_PluralNoun = ANoun[2] + APluralNoun
Atest44f_ProgressiveY_PluralVerb = AProgressiveY + APluralVerb

#stem vs affix
Atest444c_ProgressiveN_PluralVerb = AProgressiveN +  APluralVerb
Atest444f_Verb0 =  AVerb[0]


Atest.extend((Atest1c_Verb0_ProgressiveY_Pluralverb,Atest1f_Pluralnoun_Verb0_ProgressiveY,Atest11c_Verb2_ProgressiveN_Singularverb,Atest11f_Pluralnoun_Verb2_ProgressiveN,  Atest2c_Noun0_Singularnoun, Atest2f_Singularnoun_Verb2_ProgressiveN, Atest22c_Noun1_Pluralnoun, Atest22f_Pluralnoun_Verb2_ProgressiveY, Atest3c_ProgressiveY_PluralVerb, Atest3f_Pluralnoun_1syllOFverb1, Atest33c_ProgressiveN_SingularVerb, Atest33f_SingularNoun_1syllOFverb0, Atest333c_ProgressiveY_SingularVerb, Atest333f_2syllOFverb1_SingularVerb,Atest3333c_ProgressiveN_PluralVerb, Atest3333f_2syllOFverb0_ProgressiveN ,  Atest4c_Noun2_SingularNoun,Atest4f_ProgressiveN_SingularVerb, Atest44c_Noun2_PluralNoun, Atest44f_ProgressiveY_PluralVerb, Atest444c_ProgressiveN_PluralVerb, Atest444f_Verb0))
Atestnamelist=("Atest1c_Verb0_ProgressiveY_Pluralverb","Atest1f_Pluralnoun_Verb0_ProgressiveY","Atest11c_Verb2_ProgressiveN_Singularverb","Atest11f_Pluralnoun_Verb2_ProgressiveN","Atest2c_Noun0_Singularnoun", "Atest2f_Singularnoun_Verb2_ProgressiveN", "Atest22c_Noun1_Pluralnoun", "Atest22f_Pluralnoun_Verb2_ProgressiveY","Atest3c_ProgressiveY_PluralVerb", "Atest3f_Pluralnoun_1syllOFverb1", "Atest33c_ProgressiveN_SingularVerb", "Atest33f_SingularNoun_1syllOFverb0", "Atest333c_ProgressiveY_SingularVerb","Atest333f_2syllOFverb1_SingularVerb", "Atest3333c_ProgressiveN_PluralVerb", "Atest3333f_2syllOFverb0_ProgressiveN",   "Atest4c_Noun2_SingularNoun",   "Atest4f_ProgressiveN_SingularVerb", "Atest44c_Noun2_PluralNoun", "Atest44f_ProgressiveY_PluralVerb", "Atest444c_ProgressiveN_PluralVerb", "Atest444f_Verb0")



#Atest.extend((Atest1c_Verb0_ProgressiveY_Pluralverb,Atest1f_Pluralnoun_Verb0_ProgressiveY,Atest11c_Verb2_ProgressiveN_Singularverb,Atest11f_Pluralnoun_Verb2_ProgressiveN,Atest111c_Verb1_ProgressiveY_Singularverb, Atest111f_2syllOFverb1_ProgressiveY_Singularverb_Disruptor2, Atest2c_Noun0_Singularnoun, Atest2f_Singularnoun_Verb2_ProgressiveN, Atest22c_Noun1_Pluralnoun, Atest22f_Pluralnoun_Verb2_ProgressiveY,Atest222c_Noun0_PluralNoun,Atest222f_Disruptor1_Noun0,  Atest3c_ProgressiveY_PluralVerb, Atest3f_Pluralnoun_1syllOFverb1, Atest33c_ProgressiveN_SingularVerb, Atest33f_SingularNoun_1syllOFverb0, Atest333c_ProgressiveY_SingularVerb,Atest333f_SingularVerb_Disruptor2,   Atest4c_Noun2_SingularNoun,Atest4f_ProgressiveN_SingularVerb, Atest44c_Noun2_PluralNoun, Atest44f_ProgressiveY_PluralVerb, Atest444c_ProgressiveN_PluralVerb, Atest444f_Verb0))
#Atestnamelist=("Atest1c_Verb0_ProgressiveY_Pluralverb","Atest1f_Pluralnoun_Verb0_ProgressiveY","Atest11c_Verb2_ProgressiveN_Singularverb","Atest11f_Pluralnoun_Verb2_ProgressiveN","Atest111c_Verb1_ProgressiveY_Singularverb", "Atest111f_2syllOFverb1_ProgressiveY_Singularverb_Disruptor2", "Atest2c_Noun0_Singularnoun", "Atest2f_Singularnoun_Verb2_ProgressiveN", "Atest22c_Noun1_Pluralnoun", "Atest22f_Pluralnoun_Verb2_ProgressiveY","Atest222c_Noun0_PluralNoun","Atest222f_Disruptor1_Noun0",  "Atest3c_ProgressiveY_PluralVerb", "Atest3f_Pluralnoun_1syllOFverb1", "Atest33c_ProgressiveN_SingularVerb", "Atest33f_SingularNoun_1syllOFverb0", "Atest333c_ProgressiveY_SingularVerb","Atest333f_SingularVerb_Disruptor2",   "Atest4c_Noun2_SingularNoun",   "Atest4f_ProgressiveN_SingularVerb", "Atest44c_Noun2_PluralNoun", "Atest44f_ProgressiveY_PluralVerb", "Atest444c_ProgressiveN_PluralVerb", "Atest444f_Verb0")

"""
Btest1c_Verb0_ProgressiveY_Pluralverb = BVerb[0] + BProgressiveY + BPluralVerb
Btest1f_Pluralnoun_Verb0_ProgressiveY = BPluralNoun + BVerb[0] + BProgressiveY

Btest11c_Verb3_ProgressiveN_Singularverb = BVerb[2] + BProgressiveN + BSingularVerb
Btest11f_Pluralnoun_Verb3_ProgressiveN = BPluralNoun + BVerb[2] + BProgressiveN

#noun vs non-word
Btest2c_Noun0_Singularnoun = BNoun[0] + BSingularNoun
Btest2f_Singularnoun_Verb2_ProgressiveN = BSingularNoun+ BVerb[2] + BProgressiveN

Btest22c_Noun1_Pluralnoun = BNoun[1] + BPluralNoun
Btest22f_Pluralnoun_Verb2_ProgressiveY = BPluralNoun + BVerb[2] + BProgressiveY

#morpheme vs non-word
Btest3c_ProgressiveY_PluralVerb=BProgressiveY + BPluralVerb
Btest3f_Pluralnoun_1syllOFverb1=BPluralNoun +  str(BVerb[1])[0:2]  #first syllable of 2 syllable  verb DOESNT WORK

Btest33c_ProgressiveN_SingularVerb= BProgressiveN + BSingularVerb
Btest33f_SingularNoun_1syllOFverb0= BSingularNoun + str(BVerb[0])[0:2] #first syllable of 2 syllable  verb DOESNT WORK

#noun vs morpheme
Btest4c_Noun2_SingularNoun=BNoun[2]  + BSingularNoun
Btest4f_ProgressiveN_SingularVerb=BProgressiveN + BSingularVerb  

Btest44c_Noun2_PluralNoun=BNoun[2] + BPluralNoun
Btest44f_ProgressiveY_PluralVerb=BProgressiveY + BPluralVerb
Btest.extend((Btest1c_Verb0_ProgressiveY_Pluralverb,Btest1f_Pluralnoun_Verb0_ProgressiveY,Btest11c_Verb3_ProgressiveN_Singularverb,Btest11f_Pluralnoun_Verb3_ProgressiveN, Btest2c_Noun0_Singularnoun, Btest2f_Singularnoun_Verb2_ProgressiveN, Btest22c_Noun1_Pluralnoun, Btest22f_Pluralnoun_Verb2_ProgressiveY, Btest3c_ProgressiveY_PluralVerb, Btest3f_Pluralnoun_1syllOFverb1, Btest33c_ProgressiveN_SingularVerb, Btest33f_SingularNoun_1syllOFverb0, Btest4c_Noun2_SingularNoun,Btest4f_ProgressiveN_SingularVerb, Btest44c_Noun2_PluralNoun, Btest44f_ProgressiveY_PluralVerb))
Btestnamelist=("Btest1c_Verb0_ProgressiveY_Pluralverb","Btest1f_Pluralnoun_Verb0_ProgressiveY","Btest11c_Verb3_ProgressiveN_Singularverb","Btest11f_Pluralnoun_Verb3_ProgressiveN", "Btest2c_Noun0_Singularnoun", "Btest2f_Singularnoun_Verb2_ProgressiveN", "Btest22c_Noun1_Pluralnoun", "Btest22f_Pluralnoun_Verb2_ProgressiveY", "Btest3c_ProgressiveY_PluralVerb", "Btest3f_Pluralnoun_1syllOFverb1", "Btest33c_ProgressiveN_SingularVerb", "Btest33f_SingularNoun_1syllOFverb0", "Btest4c_Noun2_SingularNoun","Btest4f_ProgressiveN_SingularVerb", "Btest44c_Noun2_PluralNoun", "Btest44f_ProgressiveY_PluralVerb")

Ctest1c_Verb0_ProgressiveY_Pluralverb = CVerb[0] + CProgressiveY + CPluralVerb
Ctest1f_Pluralnoun_Verb0_ProgressiveY = CPluralNoun + CVerb[0] + CProgressiveY

Ctest11c_Verb3_ProgressiveN_Singularverb = CVerb[2] + CProgressiveN + CSingularVerb
Ctest11f_Pluralnoun_Verb3_ProgressiveN = CPluralNoun + CVerb[2] + CProgressiveN

#noun vs non-word
Ctest2c_Noun0_Singularnoun = CNoun[0] + CSingularNoun
Ctest2f_Singularnoun_Verb2_ProgressiveN = CSingularNoun+ CVerb[2] + CProgressiveN

Ctest22c_Noun1_Pluralnoun = CNoun[1] + CPluralNoun
Ctest22f_Pluralnoun_Verb2_ProgressiveY = CPluralNoun + CVerb[2] + CProgressiveY

#morpheme vs non-word
Ctest3c_ProgressiveY_PluralVerb=CProgressiveY + CPluralVerb
Ctest3f_Pluralnoun_1syllOFverb1=CPluralNoun +  str(CVerb[1])[0:2]  #first syllable of 2 syllable  verb DOESNT WORK

Ctest33c_ProgressiveN_SingularVerb= CProgressiveN + CSingularVerb
Ctest33f_SingularNoun_1syllOFverb0= CSingularNoun + str(CVerb[0])[0:2] #first syllable of 2 syllable  verb DOESNT WORK

#noun vs morpheme
Ctest4c_Noun2_SingularNoun=CNoun[2]  +  CSingularNoun
Ctest4f_ProgressiveN_SingularVerb=CProgressiveN + CSingularVerb  

Ctest44c_Noun2_PluralNoun=CNoun[2] + CPluralNoun
Ctest44f_ProgressiveY_PluralVerb=CProgressiveY + CPluralVerb

Ctest.extend((Ctest1c_Verb0_ProgressiveY_Pluralverb,Ctest1f_Pluralnoun_Verb0_ProgressiveY,Ctest11c_Verb3_ProgressiveN_Singularverb,Ctest11f_Pluralnoun_Verb3_ProgressiveN, Ctest2c_Noun0_Singularnoun, Ctest2f_Singularnoun_Verb2_ProgressiveN, Ctest22c_Noun1_Pluralnoun, Ctest22f_Pluralnoun_Verb2_ProgressiveY, Ctest3c_ProgressiveY_PluralVerb, Ctest3f_Pluralnoun_1syllOFverb1, Ctest33c_ProgressiveN_SingularVerb, Ctest33f_SingularNoun_1syllOFverb0, Ctest4c_Noun2_SingularNoun,Ctest4f_ProgressiveN_SingularVerb, Ctest44c_Noun2_PluralNoun, Ctest44f_ProgressiveY_PluralVerb))


Ctestnamelist=("Ctest1c_Verb0_ProgressiveY_Pluralverb","Ctest1f_Pluralnoun_Verb0_ProgressiveY","Ctest11c_Verb3_ProgressiveN_Singularverb","Ctest11f_Pluralnoun_Verb3_ProgressiveN", "Ctest2c_Noun0_Singularnoun", "Ctest2f_Singularnoun_Verb2_ProgressiveN", "Ctest22c_Noun1_Pluralnoun", "Ctest22f_Pluralnoun_Verb2_ProgressiveY", "Ctest3c_ProgressiveY_PluralVerb", "Ctest3f_Pluralnoun_1syllOFverb1", "Ctest33c_ProgressiveN_SingularVerb", "Ctest33f_SingularNoun_1syllOFverb0", "Ctest4c_Noun2_SingularNoun","Ctest4f_ProgressiveN_SingularVerb", "Ctest44c_Noun2_PluralNoun", "Ctest44f_ProgressiveY_PluralVerb")

Dtest1c_Verb0_ProgressiveY_Pluralverb = DVerb[0] + DProgressiveY + DPluralVerb
Dtest1f_Pluralnoun_Verb0_ProgressiveY = DPluralNoun + DVerb[0] + DProgressiveY

Dtest11c_Verb3_ProgressiveN_Singularverb = DVerb[2] + DProgressiveN + DSingularVerb
Dtest11f_Pluralnoun_Verb3_ProgressiveN = DPluralNoun + DVerb[2] + DProgressiveN

#noun vs non-word
Dtest2c_Noun0_Singularnoun = DNoun[0] + DSingularNoun
Dtest2f_Singularnoun_Verb2_ProgressiveN = DSingularNoun+ DVerb[2] + DProgressiveN

Dtest22c_Noun1_Pluralnoun = DNoun[1] + DPluralNoun
Dtest22f_Pluralnoun_Verb2_ProgressiveY = DPluralNoun + DVerb[2] + DProgressiveY

#morpheme vs non-word
Dtest3c_ProgressiveY_PluralVerb=DProgressiveY + DPluralVerb
Dtest3f_Pluralnoun_1syllOFverb1=DPluralNoun +  str(DVerb[1])[0:2]  #first syllable of 2 syllable  verb DOESNT WORK

Dtest33c_ProgressiveN_SingularVerb= DProgressiveN + DSingularVerb
Dtest33f_SingularNoun_1syllOFverb0= DSingularNoun + str(DVerb[0])[0:2] #first syllable of 2 syllable  verb DOESNT WORK

#noun vs morpheme
Dtest4c_Noun2_SingularNoun=DNoun[2]  + DSingularNoun
Dtest4f_ProgressiveN_SingularVerb=DProgressiveN + DSingularVerb  

Dtest44c_Noun2_PluralNoun=DNoun[2] + DPluralNoun
Dtest44f_ProgressiveY_PluralVerb=DProgressiveY + DPluralVerb

Dtest.extend((Dtest1c_Verb0_ProgressiveY_Pluralverb,Dtest1f_Pluralnoun_Verb0_ProgressiveY,Dtest11c_Verb3_ProgressiveN_Singularverb,Dtest11f_Pluralnoun_Verb3_ProgressiveN, Dtest2c_Noun0_Singularnoun, Dtest2f_Singularnoun_Verb2_ProgressiveN, Dtest22c_Noun1_Pluralnoun, Dtest22f_Pluralnoun_Verb2_ProgressiveY, Dtest3c_ProgressiveY_PluralVerb, Dtest3f_Pluralnoun_1syllOFverb1, Dtest33c_ProgressiveN_SingularVerb, Dtest33f_SingularNoun_1syllOFverb0, Dtest4c_Noun2_SingularNoun,Dtest4f_ProgressiveN_SingularVerb, Dtest44c_Noun2_PluralNoun, Dtest44f_ProgressiveY_PluralVerb))


Dtestnamelist=("Dtest1c_Verb0_ProgressiveY_Pluralverb","Dtest1f_Pluralnoun_Verb0_ProgressiveY","Dtest11c_Verb3_ProgressiveN_Singularverb","Dtest11f_Pluralnoun_Verb3_ProgressiveN", "Dtest2c_Noun0_Singularnoun", "Dtest2f_Singularnoun_Verb2_ProgressiveN", "Dtest22c_Noun1_Pluralnoun", "Dtest22f_Pluralnoun_Verb2_ProgressiveY", "Dtest3c_ProgressiveY_PluralVerb", "Dtest3f_Pluralnoun_1syllOFverb1", "Dtest33c_ProgressiveN_SingularVerb", "Dtest33f_SingularNoun_1syllOFverb0", "Dtest4c_Noun2_SingularNoun","Dtest4f_ProgressiveN_SingularVerb", "Dtest44c_Noun2_PluralNoun", "Dtest44f_ProgressiveY_PluralVerb")
"""
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
