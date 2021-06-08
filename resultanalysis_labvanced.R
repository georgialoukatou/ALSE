library(tidyverse)
#library(dplyr) 
#library(ggplot2)
#library(ggpubr)
#library(plyr)
#library(beanplot)
#library(tidyr)
library(lme4)

pilot_long<-read_csv("data_pilotC_4subjects.csv")

names(pilot_long)[names(pilot_long) == 'Final'] <- 'thisResp'
names(pilot_long)[names(pilot_long) == 'Trial_Nr'] <- 'numberoftrial'
names(pilot_long)[names(pilot_long) == 'exp_subject_id'] <- 'uniqueid'
names(pilot_long)[names(pilot_long) == 'group_name'] <- 'group'

verb_word <- seq(1,8)
noun_word <- seq(9,14)
verb_stem <- seq(15, 22)
noun_stem <- seq(23, 30)

pilot_long$question <- NA
pilot_long$Nsyll <- NA

pilot_long <- pilot_long %>%
  mutate(question = ifelse(pilot_long$Trial_Id %in% verb_word,"verb_word",NA )) %>%
  mutate(question = ifelse(pilot_long$Trial_Id %in% noun_word,"noun_word",question )) %>%
  mutate(question = ifelse(pilot_long$Trial_Id %in% verb_stem,"verb_stem",question)) %>%
  mutate(question = ifelse(pilot_long$Trial_Id %in% noun_stem,"noun_stem",question))


pilot_long_log<-subset(pilot_long, select=c(thisResp, numberoftrial, question, uniqueid, group)) 

pilot_long_log<-pilot_long_log %>%
  filter(!thisResp == "")

pilot_long_log$numberoftrial<- as.numeric(pilot_long_log$numberoftrial)
pilot_long_log$thisResp<- factor(pilot_long_log$thisResp)

pilot_long_log$thisresplog <- NA
pilot_long_log$thisresplog[pilot_long_log$thisResp=='TRUE'] <- "1"
pilot_long_log$thisresplog[pilot_long_log$thisResp=='FALSE'] <- "0"


############################# Logistic regression 
pilot_long_log$level <- NA
pilot_long_log$level[pilot_long_log$question=='verb_word'] <- "word"
pilot_long_log$level[pilot_long_log$question=='verb_stem'] <- "stem"
pilot_long_log$level[pilot_long_log$question=='noun_stem'] <- "stem"
pilot_long_log$level[pilot_long_log$question=='noun_word'] <- "word"
pilot_long_log$type <- NA
pilot_long_log$type[pilot_long_log$question=='verb_word'] <- "verb"
pilot_long_log$type[pilot_long_log$question=='verb_stem'] <- "verb"
pilot_long_log$type[pilot_long_log$question=='noun_stem'] <- "noun"
pilot_long_log$type[pilot_long_log$question=='noun_word'] <- "noun"

pilot_long_log$thisresplog<- as.factor(pilot_long_log$thisresplog)

model<-glmer(formula= thisresplog ~ level + numberoftrial +(1 + level + numberoftrial|uniqueid),  control = glmerControl(optimizer = "bobyqa"), family = binomial(link = "logit"),  data = pilot_long_log)

##add percentage correct column
pilot_short<-subset(pilot_long_log, select=c(uniqueid, thisResp, level ))
pilot_short1<-subset(pilot_long_log, select=c(uniqueid, level ))
pilot_group<-subset(pilot_long_log, select=c(uniqueid, group ))

pilot_count1 <- pilot_short1 %>%  
  group_by(uniqueid, level) %>%  
  count() 
colnames(pilot_count1)[3] <- "total"
pilot_count <- pilot_short %>%  
  group_by(uniqueid, level, thisResp) %>%  
  count() 

df<-merge(x=pilot_count1,y=pilot_count,by=c("uniqueid", "level"),all=TRUE)
pilot_<- df %>%
  filter(thisResp == "TRUE") %>%
  mutate(proportion = n / total)
pilot<-unique(merge(x=pilot_,y=pilot_group,by=c("uniqueid"),all=TRUE))

ggplot(pilot, aes(x=level, y=proportion, group=factor(level)))+ geom_point()+ ylab("Proportion correct")# to add


######################## Number of trials
df2_ <- pilot_long_log %>%  
  group_by(numberoftrial, thisResp) %>%  
  tally()  %>%
  filter(thisResp=="TRUE")

df2_$numberoftrial<- factor(df2_$numberoftrial)

ggplot(df2_, aes(numberoftrial, n)) + geom_bar(stat = "identity")  + ylab("Number correct")



###Number of syllables
#df3 <- pilot_long_log %>%   group_by(Nsyll, thisResp) %>%  tally() 
#p<-ggplot(df3, aes(Nsyll, n, fill=factor(thisResp))) + geom_bar(stat = "identity")# to add
#p<-p + scale_fill_discrete(name = "Response", labels = c("correct", "wrong")) +scale_fill_manual(values = c("#00AFBB", "#E7B800"))
#p

########## T-tests 
pilot_words<-subset(pilot, level == 'word', select=c(level, proportion, group, uniqueid)) 
pilot_stems<-subset(pilot, level == 'stem', select=c(level, proportion, group, uniqueid)) 

#pilot_stems<-subset(pilot, question == ' verb_stem'| question == ' noun_stem', select=c(question, percentage, group, uniqueid)) 

summary(pilot_words)
shapiro.test(pilot_words$proportion) 
resw <- t.test(pilot_words$proportion, mu=0.50,  alternative = "greater")
resw

shapiro.test(pilot_stems$proportion) 
ress <- t.test(pilot_stems$proportion, mu=0.50,  alternative = "greater")
ress

res_f <- t.test(pilot_words$proportion, pilot_stems$proportion, paired = TRUE)
res_f

########################
####################### T-tests Nouns vs Verbs

pilot_count_nv <- pilot_long_log %>%  
  group_by(uniqueid, question) %>%  
  count() 
colnames(pilot_count_nv)[3] <- "total"
pilot_count1_nv <- pilot_long_log %>%  
  group_by(uniqueid, question, thisResp) %>%  
  count() 

df_nv<-merge(x=pilot_count_nv,y=pilot_count1_nv,by=c("uniqueid", "question"),all=TRUE)
pilot_nv<- df_nv %>%
  filter(thisResp == "TRUE") %>%
  mutate(proportion = n / total)
pilot_nv<-unique(merge(x=pilot_nv,y=pilot_group,by=c("uniqueid"),all=TRUE))

pilot_nouns<-subset(pilot_nv, question == 'noun_stem'| question == 'noun_word', select=c(question, proportion, group, uniqueid)) 
pilot_verbs<-subset(pilot_nv, question == 'verb_stem'| question == 'verb_word', select=c(question, proportion, group, uniqueid)) 
#group_by(pilot_nouns, question) %>%summarise(count = n(),mean = mean(percentage, na.rm = TRUE),sd = sd(percentage, na.rm = TRUE))


dn <- with(pilot_nouns, proportion[question == "noun_word"] - proportion[question == "noun_stem"])
dv <- with(pilot_verbs, proportion[question == "verb_word"] - proportion[question == "verb_stem"])
shapiro.test(dn) 
shapiro.test(dv) 


resn <- t.test(proportion ~ question, data = pilot_nouns, paired = TRUE)
resv <- t.test(proportion ~ question, data = pilot_verbs, paired = TRUE)
resn
resv

res_fc <- t.test(pilot_nouns$proportion, pilot_verbs$proportion, paired = TRUE)
res_fc

##### exclusion criteria
#4 or more wrong answers in test questions (Attention_1_animal_type vs attention1_test) OR less than 1 sd below group mean
trial_att<- c(5, 19, 34, 48, 64, 77, 92, 107)


pilot_log_atte <- pilot_long %>%
  select(contains("Attention"), uniqueid, numberoftrial )%>%
  select(-(contains("Time"))) %>%
  filter(numberoftrial %in% trial_att)

new<- pilot_log_atte %>%
  pivot_longer(
    cols = contains("Animal"),
    names_to = "AttentionQ",
    values_to = "answer" ) %>%
  pivot_longer(
    cols = contains("test"),
    names_to = "AttentionA",
    values_to = "question" ) %>%
  na.omit

new$answer <- new$answer %>%
  str_replace( "un ", "") 

new$question <- new$question %>%
  str_replace( " Is Correct", "") 

new<- new %>%
  mutate(eval = ifelse(answer == question, "TRUE", "FALSE"))

attention <- new %>% 
  group_by(eval, uniqueid) %>%
  summarise(n=n(),
  m=n/8) %>%
  filter(eval=="TRUE") %>%
  mutate(pass = ifelse(m < 0.5, "EXCLUDE", "INCLUDE") )

attention1 <- attention %>%
  summarise(mean_=mean(m),
            sd_=sd(m)) %>%
  mutate(threshold = mean_ - sd_) %>%
  left_join(attention) %>%
  mutate(pass = ifelse(m < threshold, "EXCLUDE", pass) )
  
  
#next video command for train
# decision time for test

Attention questions: those who answer incorrectly half of the times or less than  one sd below the group mean

For decision time: trials that are over 2 sd over the participant mean 
