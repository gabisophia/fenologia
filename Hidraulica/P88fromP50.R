#Analytical solution to calculate P88 from P50
P88fun<-function(P50,a) {
  P88=7.33^(1/a)*P50
}

#compare P88 found numerically with the P88 found analytically 
P50=-2
a=seq(2,10,by=0.1)

#analytical solution
P88anl=P88fun(P50,a)
P88anl
#numerical solution
P=seq(P50,10*P50,by=-0.01)
P88num<-NULL
for (i in 1:length(a)) {
  k=1/(1+(P/P50)^a[i])
  P88num[i]=P[which.min(abs(k-0.12))]}
P88num
#plot
plot(P88anl~P88num)
abline(0,1)

#Se a é constante a relação entre P50 e P88 é linear com a inclinação dependendo do valor de a
a=2
P50=seq(-1,-5,len=100)
y=P88fun(P50,a)
plot(y~P50,type="l")
a=4
y2=P88fun(P50,a)
lines(y2~P50,col=2)
a=8
y3=P88fun(P50,a)
lines(y3~P50,col=4)
