import matplotlib.pyplot as plt
import numpy as np

# Parametros hidraulicos do solo 
theta_sat = 0.4 #g H20/g solo
Psi_sat = -0.001 #MPa
b = 7 #sem unidade

# Conteudo volumétrico de água no solo (i.e. g H20/g solo)  ARRUMAR
theta = np.arange(0.1, theta_sat, 0.001)

# Calculo potencial hidrico do solo (Psi_solo MPa - equação de Clapp & Hornberger 1978 - Empirical Equations for Some Soil Hydraulic Properties)
#ACRESCENTAR CAMADAS?
Psi_solo = Psi_sat * (theta / theta_sat) ** (-b)

# Gráfico Psi_solo vs W(theta/theta_sat)   ARRUMAR   #acrescentei theta_sat
fig, ax = plt.subplots()
ax.plot(theta , Psi_solo)   #esse gráfico na verdade teria que ser theta/theta_s vs Psi_solo

ax.grid(False, linestyle='-')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

plt.show()


#CONTINUAR O CÓDIDO


# Parametros hidráulicos das plantas 
P50 = -2 #MPa     #VIRAR UM RANGE
a = 4 #sem unidade

# Calculo de V (equação de Manzoni et al 2013 - Biological constraints on water transport in the soil-plant-atmosphere system)
V = 1 / (1 + (Psi_solo / P50) ** a)


#CRIAR GRÁFICOS V vs Psi_solo   e    V vs W(theta/theta_sat)

#plot(V~Psi_solo,type="l", ylim=c(0,1))
#plot(V~I(theta/theta_sat),type="l", ylim=c(0,1))





# se existir altura no modelo o efeito da gravidade no transporte de água pode incluido tbm
#rho<-997 #kg/m3
#g<-9.8#m/s2
#alt<-20#m
#conv<-1e-6 # Pa to MPa
#Psi_g<-rho*g*alt*conv

#V=1/(1+((Psi_solo-Psi_g)/P50)^a)
#plot(V~Psi_solo,type="l", ylim=c(0,1))
#plot(V~I(theta/theta_sat),type="l", ylim=c(0,1))