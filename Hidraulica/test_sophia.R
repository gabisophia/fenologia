#constants/produced by the model
b=7#unitless
ksr_max=0.0025#mol m-2 s-1 MPa-1
Psat=-0.01#Saturated soil water potential (Mpa)
E=10*0.001#Transpiration - mol m-2 s-1
W=seq(0.01,1,by=0.01)#normalized soil water content
#Pr calculation
  k=W^2*b+3# Normalized k - Clapp & Hornberger 1978
  print(k)
  ksr=k*ksr_max#mol m-2 s-1 MPa-1
  print(ksr)
  Ps=Psat*W^-b#Soil water potential - Clapp & Hornberger 1978
  Pr=Ps-(E/ksr)#Root water potential
#plot
plot(Pr~W, type="l",ylim=c(-15,0),
     ylab=expression(Psi~"("*MPa*")"),xlab="Soil water content (Normalized)")
lines(Ps~W,col=2)
legend("topleft",legend=c(expression(Soil~Psi),expression(Root~Psi)),
       col=c(2,1),lty=1,bty="n")
Pr-Ps
