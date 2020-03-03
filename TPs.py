from __future__ import division


Syllables=["glu","sin",  "ga",  "kli",  "ten",  "ko",  "blu", "tun",  "man",  "blo", "ti", "gle" ,"da", "pun",  "go", "kan", "fen", "bi"]

######################PREP PHASE
#######Group  A

ANoun=[]
AVerb=[]
ASentence=[]
ADisrupter1=[]
ADisrupter2=[]
Atest=[]



ANoun.append(str(Syllables[0]+ Syllables[1]))
ANoun.append(str(Syllables[2]+ Syllables[3]))
ANoun.append(str(Syllables[4]))


AVerb.append(str(Syllables[5]+ Syllables[6]))
AVerb.append(str(Syllables[7]+ Syllables[8]))
AVerb.append(str(Syllables[9]))

ADisrupter1.append("/")
ADisrupter1.append(str(Syllables[10]))
ADisrupter2.append("/")
ADisrupter2.append(str(Syllables[11]))


ASingularNoun= str(Syllables[12])
ASingularVerb= str(Syllables[13])
APluralNoun= str(Syllables[14])
APluralVerb=  str(Syllables[15])
AProgressiveY= str(Syllables[16])
AProgressiveN= str(Syllables[17])

#noun0=dog 
#verb0=flip, verb1=jump, verb2=walk 

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



i=0
fverb2=0
fverb2progry=0
fprogry=0
fprogrypluralv=0
fpluraln=0
fpluralnverb2=0
fprogrysingularv=0
fsingularn=0
fsingularnverb2=0
ffirstsyllverb0=0
fsecondsyllverb0=0
fverb0=0
fsecondsyllverb0progrn=0
fprogrn=0
fprogrnsingularv=0
fsingularv=0
ffirstsyllnoun1=0
fsecondsyllnoun1=0
fsecondsyllnoun1pluraln=0
fnoun1=0
fverb1=0
ffirstsyllverb1=0
fsecondsyllverb1progry=0
fsecondsyllverb1=0
fprogrypluralv=0
fpluralv=0
fnoun0=0
ffirstsyllnoun0=0
fsecondsyllnoun0singularn=0
fsecondsyllnoun0=0
fsingularn=0
fprogrnpluralv=0
fverb2progrn=0
fnoun2singularn=0
fnoun2=0
fnoun2pluraln=0
fsyll1=0
fnoun1pluraln=0
fsecondsyllnoun0pluraln=0



FAtest1c=0
FAtest1f=0
FAtest11c=0
FAtest11f=0
FAtest111c=0
FAtest111f=0
FAtest1111c=0
FAtest1111f=0
FAtest11111c=0
FAtest11111f=0
FAtest111111c=0
FAtest111111f=0
FAtest2c=0
FAtest2f=0
FAtest22c=0
FAtest22f=0
FAtest222c=0
FAtest222f=0
FAtest2222c=0
FAtest2222f=0
FAtest3c=0
FAtest3f=0
FAtest33c=0
FAtest33f=0
FAtest333c=0
FAtest333f=0
FAtest3333c=0
FAtest3333f=0
FAtest4c=0
FAtest4f=0
FAtest44c=0
FAtest44f=0
FAtest444c=0
FAtest444f=0
FAtest4444c=0
FAtest4444f=0
FAtest22222c=0
FAtest22222f=0
FAtest222222c=0
FAtest222222f=0
FAtest1111111c=0
FAtest1111111f=0
FAtest11111111c=0
FAtest11111111f=0
FAtest33333c=0
FAtest33333f=0
FAtest333333c=0
FAtest333333f=0
FAtest3333333c=0
FAtest3333333f=0
FAtest33333333c=0
FAtest33333333f=0
FAtest44444c=0
FAtest44444f=0
FAtest444444c=0
FAtest444444f=0
FAtest4444444c=0
FAtest4444444f=0
FAtest44444444c=0
FAtest44444444f=0



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
Atest222f_2ndofVerb0_ProgressiveN  = AVerb[0] + AProgressiveN  #smallPROBLEM
Atest2222c_Noun0_Singularnoun = ANoun[0] + ASingularNoun
Atest2222f_2ndofVerb1_ProgressiveY  = AVerb[1] + AProgressiveY  #smallPROBLEM


#verbstem vs non-verbstem

Atest3c_Verb0  = AVerb[0]
Atest3f_2ndofVerb1_ProgressiveY = AVerb[1][3:6]+ AProgressiveY

Atest33c_Verb1  = AVerb[1]
Atest33f_2ndofVerb0_ProgressiveN = AVerb[0][2:5] + AProgressiveN

Atest333c_Verb0  = AVerb[0]
Atest333f_2ndofNoun0_Singularnoun  =  ANoun[0][3:6]+ ASingularNoun 

Atest333333c_Verb1  = AVerb[1]
Atest333333f_2ndofNoun1_Pluralnoun  = ANoun[1][2:5]+ APluralNoun 



#nounstem vs non-nounstem

Atest4c_Noun1 = ANoun[1]
Atest4f_2ndofNoun1_Pluralnoun  =  ANoun[1][2:5]+ APluralNoun
Atest44c_Noun0 = ANoun[0]
Atest44f_2ndofNoun0_Singularnoun  =  ANoun[0][3:6]+ ASingularNoun 
Atest444c_Noun1 =  ANoun[1]
Atest444f_2ndofVerb1_ProgressiveY =  AVerb[1][3:6]+ AProgressiveY
Atest4444c_Noun0 =  ANoun[0]
Atest4444f_2ndofVerb0_ProgressiveN = AVerb[0][2:5] + AProgressiveN



for item in ASentence:
 if AVerb[2] in item: 
    fverb2=fverb2+1
 if AVerb[2] + AProgressiveY in item:
    fverb2progry=fverb2progry + 1
 if AVerb[2] + AProgressiveN in item:
    fverb2progrn=fverb2progrn + 1
 if AVerb[2] + AProgressiveY + APluralVerb in item:
 	FAtest1c=FAtest1c + 1
 if AVerb[2] + AProgressiveY + ASingularVerb in item:
 	FAtest11c=FAtest11c + 1 
 if AVerb[2] + AProgressiveN + APluralVerb in item:
 	FAtest11111c=FAtest11111c + 1  
 if AVerb[2] + AProgressiveN + ASingularVerb in item:
 	FAtest111111c=FAtest111111c + 1  

 if AVerb[0][0:2] in item:
 	ffirstsyllverb0=ffirstsyllverb0 + 1
 if AVerb[0][2:5] in item:
 	fsecondsyllverb0=fsecondsyllverb0 + 1
 if AVerb[0] in item:
 	fverb0=fverb0 +1
 	FAtest3c=FAtest3c + 1 
 	FAtest333c=FAtest333c + 1 
 	FAtest33333c=FAtest33333c +1
 	FAtest3333333c=FAtest3333333c+1
 if AVerb[0][2:5] + AProgressiveN in item:
 	fsecondsyllverb0progrn=fsecondsyllverb0progrn +1
 	FAtest33f=FAtest33f+1
 	FAtest4444f=FAtest4444f + 1
 	FAtest3333333f=FAtest3333333f+1
 	FAtest44444f=FAtest44444f+1
 if AVerb[0] + AProgressiveN + ASingularVerb  in item:
 	FAtest111c= FAtest111c + 1
 	FAtest1111111c= FAtest1111111c + 1
 if AVerb[0] + AProgressiveN in item:
 	FAtest222f= FAtest222f + 1 
 	FAtest222222f=FAtest222222f +1
 
 if AVerb[1] in item:
 	fverb1=fverb1+1	
 	FAtest33c=FAtest33c + 1 
 	FAtest3333c=FAtest3333c + 1 
 	FAtest333333c=FAtest333333c+1
 	FAtest33333333c=FAtest33333333c +1
 if AVerb[1][0:3] in item:
 	ffirstsyllverb1=ffirstsyllverb1+1
 if AVerb[1][3:6] in item:
 	fsecondsyllverb1=fsecondsyllverb1+1
 if AVerb[1][3:6] + AProgressiveY in item:
 	fsecondsyllverb1progry=fsecondsyllverb1progry+1
 	FAtest444f=FAtest444f + 1
 	FAtest444444f=FAtest444444f+1
 	FAtest3f=FAtest3f+1
 	FAtest333333f=FAtest333333f+1
 if AVerb[1] + AProgressiveY + APluralVerb  in item:
 	FAtest1111c=FAtest1111c +1 	
 	FAtest11111111c=FAtest11111111c +1 	
 if AVerb[1] + AProgressiveY in item:
 	FAtest2222f= FAtest2222f + 1 
 	FAtest22222f=FAtest22222f + 1

 if ANoun[0] in item:
 	fnoun0=fnoun0+1	
 	FAtest44c=FAtest44c + 1
 	FAtest4444c=FAtest4444c + 1
 	FAtest444444c=FAtest444444c+1
 	FAtest44444444c=FAtest44444444c+1
 if  ANoun[0][0:3] in item:
 	ffirstsyllnoun0=ffirstsyllnoun0+1 	
 if ANoun[0][3:6] + ASingularNoun in item:
 	fsecondsyllnoun0singularn=fsecondsyllnoun0singularn+1
 	FAtest333f=FAtest333f+1
 	FAtest4f=FAtest4f + 1  
 	FAtest33333333f=FAtest33333333f+1
 	FAtest44444444f=FAtest44444444f+1
 if ANoun[0][3:6] in item:
 	fsecondsyllnoun0=fsecondsyllnoun0+1	 
 if ANoun[0] + ASingularNoun +  " - " + AVerb[2]  in item:
 	FAtest1111f=FAtest1111f + 1  	
 	FAtest1111111f=FAtest1111111f+1
 if ANoun[0] + ASingularNoun in item:
 	FAtest2222c=FAtest2222c +1 
 	FAtest222222c=FAtest222222c +1
 
 if ANoun[1][0:2] in item:
 	ffirstsyllnoun1=ffirstsyllnoun1+1
 if ANoun[1][2:5] in item:
 	fsecondsyllnoun1=fsecondsyllnoun1+1
 if ANoun[1][2:5] + APluralNoun in item:
 	fsecondsyllnoun1pluraln = fsecondsyllnoun1pluraln + 1
 	FAtest44f=FAtest44f + 1
 	FAtest4444444f=FAtest4444444f+1
 	FAtest3333f=FAtest3333f+1
 	FAtest33333f=FAtest33333f +1
 if ANoun[1] + APluralNoun in item:
 	fnoun1pluraln= fnoun1pluraln + 1  	
 	FAtest222c=FAtest222c + 1
 	FAtest22222c=FAtest22222c +1
 if ANoun[1] in item:
 	fnoun1=fnoun1+1
 	FAtest4c=FAtest4c + 1
 	FAtest444c=FAtest444c + 1
 	FAtest44444c=FAtest44444c+1
 	FAtest4444444c=FAtest4444444c+1
 if ANoun[1] + APluralNoun + " - " + AVerb[2] in item:
    FAtest111f=FAtest111f +1 
    FAtest11111111f=FAtest11111111f + 1 
 if ANoun[2] + ASingularNoun in item:
 	fnoun2singularn= fnoun2singularn + 1 
 	FAtest2c=FAtest2c +1 
 if ANoun[2]in item:
 	fnoun2= fnoun2 + 1
 if ANoun[2] + APluralNoun in item:
 	fnoun2pluraln= fnoun2pluraln + 1 
 	FAtest22c=FAtest22c +1  


 
	
 if AProgressiveY in item: 
 	fprogry=fprogry+1
 if AProgressiveY + APluralVerb in item:
 	fprogrypluralv=fprogrypluralv+1
 if AProgressiveN + APluralVerb in item:
 	fprogrnpluralv=fprogrnpluralv + 1 	
 if AProgressiveN in item:
 	fprogrn=fprogrn+1
 if AProgressiveN + ASingularVerb in item:
 	fprogrnsingularv=fprogrnsingularv + 1	
 if AProgressiveY + ASingularVerb in item:
 	fprogrysingularv=fprogrysingularv + 1
	
 	
 if APluralNoun + " - "+ AVerb[2] in item:
    fpluralnverb2=fpluralnverb2+1
    FAtest2f=FAtest2f +1  
 if APluralNoun in item:
 	fpluraln=fpluraln + 1
 if APluralNoun + " - " +  AVerb[2] + AProgressiveN in item:
 	FAtest11111f=FAtest11111f +1 
 if ASingularNoun in item:
 	fsingularn=fsingularn + 1
 if ASingularNoun + " - "+ AVerb[2] in item:
    fsingularnverb2=fsingularnverb2+1
    FAtest22f=FAtest22f + 1
 if APluralNoun + " - " + AVerb[2] + AProgressiveY in item:
 	FAtest1f=FAtest1f + 1
 if ASingularNoun + " - " +  AVerb[2] + AProgressiveY in item:
    FAtest11f=FAtest11f + 1 
 if ASingularNoun + " - " + AVerb[2] + AProgressiveN in item:
 	FAtest111111f=FAtest111111f + 1 

# 	
 #	FAtest33f=FAtest33f+1
 
 if ASingularVerb in item:
 	fsingularv=fsingularv + 1
 if APluralVerb in item:
 	fpluralv=fpluralv + 1










 	
TPAtest1c= (fverb2progry/fverb2) + (fprogrypluralv/fprogry)
TPAtest1f= (fpluralnverb2/fpluraln) + (fverb2progry/fverb2)
TPAtest11c= (fverb2progry/fverb2) +  (fprogrysingularv/fprogry)
TPAtest11f= (fsingularnverb2/fsingularn) + (fverb2progry/fverb2)
TPAtest111c= (fverb0/ffirstsyllverb0) +  (fsecondsyllverb0progrn/fsecondsyllverb0) + (fprogrnsingularv/fprogrn)
TPAtest111f= (fnoun1/ffirstsyllnoun1) + (fsecondsyllnoun1pluraln/fsecondsyllnoun1) + (fpluralnverb2/fpluraln)  #is  this normal it is verb2 and not berb0?
TPAtest1111c= (fverb1/ffirstsyllverb1) +  (fsecondsyllverb1progry/fsecondsyllverb1) + (fprogrypluralv/fprogry)
TPAtest1111f= (fnoun0/ffirstsyllnoun0) + (fsecondsyllnoun0singularn/fsecondsyllnoun0) + (fsingularnverb2/fverb2)
TPAtest11111c=(fverb2progrn/fverb2) + (fprogrnpluralv/fprogrn)
TPAtest11111f= (fpluralnverb2/fpluraln) + (fverb2progrn/fverb2)
TPAtest111111c= (fverb2progrn/fverb2) + (fprogrnsingularv/fprogrn)
TPAtest111111f= (fsingularnverb2/fsingularn) + (fverb2progrn/fverb2)
TPAtest1111111c= (fverb0/ffirstsyllverb0) +  (fsecondsyllverb0progrn/fsecondsyllverb0) + (fprogrnsingularv/fprogrn)
TPAtest1111111f= (fnoun0/ffirstsyllnoun0) + (fsecondsyllnoun0singularn/fsecondsyllnoun0) + (fsingularnverb2/fverb2)
TPAtest11111111c= (fverb1/ffirstsyllverb1) +  (fsecondsyllverb1progry/fsecondsyllverb1) + (fprogrypluralv/fprogry)
TPAtest11111111f= (fnoun1/ffirstsyllnoun1) + (fsecondsyllnoun1pluraln/fsecondsyllnoun1) + (fpluralnverb2/fpluraln)


TPAtest2c= (fnoun2singularn/fnoun2)
TPAtest2f= (fpluralnverb2/fpluraln)
TPAtest22c= (fnoun2pluraln/fnoun2)
TPAtest22f= (fsingularnverb2/fsingularn)
TPAtest222c=(fnoun1/ffirstsyllnoun1) + (fsecondsyllnoun1pluraln/fsecondsyllnoun1)  #normally +  1  
TPAtest222f= (fverb0/ffirstsyllverb0) + (fsecondsyllverb0progrn/fsecondsyllverb0) #idem
TPAtest2222c=(fnoun0/ffirstsyllnoun0) + (fsecondsyllnoun0singularn/fsecondsyllnoun0)  #idem
TPAtest2222f= (fverb1/ffirstsyllverb1) + (fsecondsyllverb1progry/fsecondsyllverb1) # idem
TPAtest22222c=(fnoun1/ffirstsyllnoun1) +  (fsecondsyllnoun1pluraln/fsecondsyllnoun1) 
TPAtest22222f=(fverb1/ffirstsyllverb1) + (fsecondsyllverb1progry/fsecondsyllverb1)
TPAtest222222c=(fnoun0/ffirstsyllnoun0) + (fsecondsyllnoun0singularn/fsecondsyllnoun0)
TPAtest222222f=(fverb0/ffirstsyllverb0) + (fsecondsyllverb0progrn/fsecondsyllverb0)


TPAtest3c=(fverb0/ffirstsyllverb0)
TPAtest3f=(fsecondsyllverb1progry/fsecondsyllverb1)
TPAtest33c=(fverb1/ffirstsyllverb1)
TPAtest33f=(fsecondsyllverb0progrn/fsecondsyllverb0)
TPAtest333c=(fverb0/ffirstsyllverb0)
TPAtest333f=(fsecondsyllnoun0singularn/fsecondsyllnoun0)
TPAtest3333c=(fverb1/ffirstsyllverb1)
TPAtest3333f=(fsecondsyllnoun1pluraln/fsecondsyllnoun1) 
TPAtest33333c=(fverb0/ffirstsyllverb0)
TPAtest33333f=(fsecondsyllnoun1pluraln/fsecondsyllnoun1) 
TPAtest333333c=(fverb1/ffirstsyllverb1)
TPAtest333333f=(fsecondsyllverb1progry/fsecondsyllverb1)
TPAtest3333333c=(fverb0/ffirstsyllverb0)
TPAtest3333333f=(fsecondsyllverb0progrn/fsecondsyllverb0)
TPAtest33333333c=(fverb1/ffirstsyllverb1)
TPAtest33333333f=(fsecondsyllnoun0singularn/fsecondsyllnoun0)


TPAtest4c=(fnoun1/ffirstsyllnoun1)
TPAtest4f=(fsecondsyllnoun0singularn/fsecondsyllnoun0)
TPAtest44c=(fnoun0/ffirstsyllnoun0)
TPAtest44f=(fsecondsyllnoun1pluraln/fsecondsyllnoun1)
TPAtest444c= (fnoun1/ffirstsyllnoun1)
TPAtest444f= (fsecondsyllverb1progry/fsecondsyllverb1)
TPAtest4444c= (fnoun0/ffirstsyllnoun0)
TPAtest4444f=(fsecondsyllverb0progrn/fsecondsyllverb0)
TPAtest44444c= (fnoun1/ffirstsyllnoun1)
TPAtest44444f= (fsecondsyllverb0progrn/fsecondsyllverb0)
TPAtest444444c= (fnoun0/ffirstsyllnoun0)
TPAtest444444f= (fsecondsyllverb1progry/fsecondsyllverb1)
TPAtest4444444c=(fnoun1/ffirstsyllnoun1)
TPAtest4444444f=(fsecondsyllnoun1pluraln/fsecondsyllnoun1)
TPAtest44444444c=(fnoun0/ffirstsyllnoun0)
TPAtest44444444f=(fsecondsyllnoun0singularn/fsecondsyllnoun0)


print("test1",TPAtest1c,FAtest1c,  "+", TPAtest1f,FAtest1f)
print("test11",TPAtest11c,FAtest11c,"+", TPAtest11f,FAtest11f)
print("test111",TPAtest111c,FAtest111c,TPAtest111f,FAtest111f)
print("test1111",TPAtest1111c,FAtest1111c,TPAtest1111f,FAtest1111f)
print("test11111",TPAtest11111c,FAtest11111c,TPAtest11111f,FAtest11111f)
print("test111111",TPAtest111111c,FAtest111111c,TPAtest111111f,FAtest111111f)
print("test1111111",TPAtest1111111c,FAtest1111111c,TPAtest1111111f,FAtest1111111f)
print("test11111111",TPAtest11111111c,FAtest11111111c,TPAtest11111111f,FAtest11111111f)


print("test2", TPAtest2c, FAtest2c,TPAtest2f, FAtest2f)
print("test22", TPAtest22c, FAtest22c,TPAtest22f, FAtest22f)
print("test222", TPAtest222c, FAtest222c,TPAtest222f, FAtest222f)
print("test2222", TPAtest2222c, FAtest2222c,TPAtest2222f, FAtest2222f)
print("test22222", TPAtest22222c, FAtest22222c,TPAtest22222f, FAtest22222f)
print("test222222", TPAtest222222c, FAtest222222c,TPAtest222222f, FAtest222222f)


print("test3", TPAtest3c, FAtest3c, TPAtest3f, FAtest3f)
print("test33", TPAtest33c, FAtest33c, TPAtest33f, FAtest33f)
print("test333", TPAtest333c, FAtest333c, TPAtest333f, FAtest333f)
print("test3333", TPAtest3333c, FAtest3333c, TPAtest3333f, FAtest3333f)
print("test33333", TPAtest33333c, FAtest33333c, TPAtest33333f, FAtest33333f)
print("test333333",TPAtest333333c, FAtest333333c,  TPAtest333333f,FAtest333333f)
print("test3333333",TPAtest3333333c, FAtest3333333c,  TPAtest3333333f,FAtest3333333f)
print("test3333333",TPAtest33333333c, FAtest33333333c,  TPAtest33333333f,FAtest33333333f)



print("test4", TPAtest4c, FAtest4c, TPAtest4f, FAtest4f)
print("test44", TPAtest44c, FAtest44c, TPAtest44f, FAtest44f)
print("test444", TPAtest444c, FAtest444c, TPAtest444f, FAtest444f)
print("test4444", TPAtest4444c, FAtest4444c, TPAtest4444f, FAtest4444f)
print("test44444", TPAtest44444c, FAtest44444c, TPAtest44444f, FAtest44444f)
print("test444444", TPAtest444444c, FAtest444444c, TPAtest444444f, FAtest444444f)
print("test4444444", TPAtest4444444c, FAtest4444444c, TPAtest4444444f, FAtest4444444f)
print("test44444444", TPAtest44444444c, FAtest44444444c, TPAtest44444444f, FAtest44444444f)
