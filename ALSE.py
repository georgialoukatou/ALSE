from os import system
import random

trainoutput=open("/Users/lscpuser/Documents/ALSE/output.txt", 'w')

Syllables=[]
Use=[]
Noun=[]
Verb=[]
Disrupter1=[]
Disrupter2=[]
Sentence=[]
test=[]


vowels=["a", "e", "i", "o", "u"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

def stringtoPhon(string):
  phon=str(string).replace("[","").replace("]","").replace("'","").replace(" - ","").replace(", ", "")
  return phon



#######LANGUAGE
for cons in consonants:
  consonant_list=[]
  for vowel in vowels: 
     consonant_list.append(str(cons)+str(vowel))
  Syllables.append(consonant_list)


for syllableGroup in Syllables:
   Use.append(random.sample(syllableGroup, k=1))
random.shuffle(Use)
random.shuffle(Use)


Noun.append(str(Use[0]+ Use[1]))
Noun.append(str(Use[2]+ Use[3]))
Noun.append(str(Use[4]))


Verb.append(str(Use[5]+ Use[6]))
Verb.append(str(Use[7]+ Use[8]))
Verb.append(str(Use[9]))


Disrupter1.append(str(Use[10]))
Disrupter1.append("  ")
Disrupter2.append(str(Use[11]))
Disrupter2.append(" ")


SingularNoun= str(Use[12])
SingularVerb= str(Use[13])
PluralNoun= str(Use[14])
PluralVerb=  str(Use[15])
ProgressiveY= str(Use[16])
ProgressiveN= str(Use[17])



##########TRAINING

for N in Noun:
  for V in Verb:
     Sentence.append(random.choice(Disrupter1)+ " - " + N + SingularNoun + " - " +  V + ProgressiveY + SingularVerb + " - " + random.choice(Disrupter2))
     Sentence.append(random.choice(Disrupter1)+ " - " + N + PluralNoun + " - " + V + ProgressiveY + PluralVerb + " - " + random.choice(Disrupter2))
     Sentence.append(random.choice(Disrupter1)+ " - " + N + SingularNoun + " - " + V + ProgressiveN + SingularVerb + " - " + random.choice(Disrupter2))
     Sentence.append(random.choice(Disrupter1)+ " - " + N + PluralNoun + " - " + V + ProgressiveN + PluralVerb + " - " + random.choice(Disrupter2))
#print(Noun1, Noun2, Noun3, Verb1, Verb2, Verb3, Disrupter1, Disrupter2, SingularNoun, SingularVerb, PluralNoun, PluralVerb, ProgressiveY, ProgressiveN)


print(len(Sentence))

count=0
for element in Sentence:
 count=count+1
 name="train" + str(count)
 print(element)
 trainoutput.write(element + str("\n"))
 element=stringtoPhon(element)
 print(element)
 system('say -o  ~/Documents/ALSE/pilot2alex/{}.aiff -v  "Paulina" {}'.format(name, stringtoPhon(element))) 


#############TEST
#verb vs non-word
test1c=Verb[0] + ProgressiveY + PluralVerb
test1f=PluralNoun + Verb[0] + ProgressiveY

test11c=Verb[2] + ProgressiveN + SingularVerb
test11f=PluralNoun + Verb[2] + ProgressiveN

#noun vs non-word
test2c=Noun[0] + SingularNoun
test2f=SingularNoun+ Verb[2] + ProgressiveN

test22c=Noun[1] + PluralNoun
test22f=PluralNoun + Verb[2] + ProgressiveY

#morpheme vs non-word
test3c=ProgressiveY + PluralVerb
test3f=PluralNoun +  str(Verb[1]).split(",")[0]  #first syllable of 2 syllable  verb

test33c= ProgressiveN + SingularVerb
test33f= SingularNoun + str(Verb[0]).split(",")[0] #first syllable of 2 syllable  verb

#noun vs morpheme
test4c=Noun[2]  + SingularNoun
test4f=ProgressiveN + SingularVerb  

test44c=Noun[2] + PluralNoun
test44f=ProgressiveY + PluralVerb

test.extend((test1c, test1f,  test11c, test11f, test2c, test2f, test22c, test22f, test3c, test3f, test33c, test33f, test4c, test4f, test44c, test44f))

count=0
namecount=0
namelist=("test1c", "test1f",  "test11c", "test11f", "test2c", "test2f", "test22c", "test22f", "test3c", "test3f", "test33c", "test33f", "test4c", "test4f", "test44c", "test44f")
for example in test:
 count=count+1
 if count>=2:
   namecount=namecount+1
 example=stringtoPhon(example)
 system('say -o  ~/Documents/ALSE/pilot2alex/{}.aiff -v  "Paulina" {}'.format(namelist[namecount], example))

