# Parametros hidraulicos do solo 
theta_sat=0.4 #g H20/g solo
Psi_sat=-0.001 #MPa
b=7 #sem unidade

# Conteudo volum�trico de �gua no solo (i.e. g H20/g solo)
theta=seq(0.1,theta_sat,len=1000)

# Calculo potencial hidrico do solo (Psi_solo MPa - equa��o de Clapp & Hornberger 1978 - Empirical Equations for Some Soil Hydraulic Properties)
Psi_solo=Psi_sat*(theta/theta_sat)^(-b)
plot(Psi_solo~I(theta/theta_sat),type="l")

# Parametros hidr�ulicos da plantas 
P50=-2 #MPa
a=4 #sem unidade  

# Calculo de V (equa��o de Manzoni et al 2013 - Biological constraints on water transport in the soil-plant-atmosphere system)
# se existir altura no modelo o efeito da gravidade no transporte de �gua pode incluido tbm
rho<-997 #kg/m3
g<-9.8#m/s2
alt<-20#m
conv<-1e-6 # Pa to MPa
Psi_g<-rho*g*alt*conv

V=1/(1+((Psi_solo-Psi_g)/P50)^a)
plot(V~Psi_solo,type="l", ylim=c(0,1))
plot(V~I(theta/theta_sat),type="l", ylim=c(0,1))

#Analytical solution to calculate P88 from P50
P50 = -3.5
a = 4
  #  P88fun<-function(P50,a) {
    P88=7.33^(1/a)*P50
  #}
  
  print(P88)