n1<-31
n2<-31
 
m1<-67
m2<-61.1

se1<-4.32
se2<-5.11
  
sd1<-se1*sqrt(n1)
sd2<-se2*sqrt(n2)

sdpooled<-sqrt(((sd1*sd1) + (sd2*sd2))/2)

d<-(m1-m2)/sdpooled
d