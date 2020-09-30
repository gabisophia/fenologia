#### Cálculo para representar o W atualizado ####

import matplotlib.pyplot as plt
import numpy as np

# Parametros hidraulicos do solo 
theta_sat = 0.4 #g H20/g solo
Psi_sat = -0.001 #MPa
b = 7 #sem unidade

# Conteudo volumétrico de água no solo (i.e. g H20/g solo)  ARRUMAR
theta = np.arange(0.1, theta_sat, 0.001)
print("theta")
print(theta)
print("\n")

# Umidade do solo (gH2O/Gsolo ou m3 m-3) CONFERIR
W = theta / theta_sat 
print("W")
print(W)
print("\n")


#### Calculo potencial hidrico do solo (Psi_solo MPa - equação de Clapp & Hornberger 1978 - Empirical Equations for Some Soil Hydraulic Properties)
Psi_solo = Psi_sat * W ** (-b)
print("Psi_solo")
print(Psi_solo)
print("\n")

# Gráfico Psi_solo vs W(theta/theta_sat) 
fig, ax = plt.subplots()
ax.plot(W , Psi_solo)   #conferir se está saindo theta/theta_s vs Psi_solo pois antes era somente o theta e ainda está dando erro
ax.grid(False, linestyle='-')
ax.set(xlabel='W (gH2O/gsolo)', ylabel='ψsolo (MPa)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()


#### Calculo condutância solo-raiz expressa com base na área foliar (ksr; mol m-2 leaf s-1):
#Ksr = W ** ((2*b)+3)
#print("ksr")
#print(Ksr)
#print("\n")
Ksr = 0.5

#Parametros faltantes para calcular o psi da raiz
#ARRUMAR
E = 9e-5 #transpiration mol m-2 s-1 

#### Calculo potencial hídrico da raíz (Eller et al. 2018)
Psi_raiz = Psi_solo - (E / Ksr)
print("Psi_raiz")
print(Psi_raiz)
print("\n")

# Gráfico Psi_raiz vs W
fig, ax = plt.subplots()
ax.plot(W, Psi_raiz)   
ax.grid(False, linestyle='-')
ax.set(xlabel='W (gH2O/gsolo)', ylabel='Psi_raiz (MPa)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()


# Calculo diferença de pressão entre a raiz e a planta
Psi_dif = Psi_raiz - Psi_solo
print("Psi_dif")
print(Psi_dif)
print("\n")


#### Calculo de V (Manzoni et al 2013) com fator de altura
rho = 997 #kg/m3
g = 9.8 #m/s2
alt = 20 #m
conv = 1e-6 # Pa to MPa
Psi_g = rho * g * alt * conv

# Parametros hidráulicos das plantas 
P50 = -2 #MPa     
a = 4 #sem unidade
V = 1 / (1+((Psi_solo - Psi_g) / P50) ** a)
print("V")
print(V)
print("\n")

# Gráfico Psi_solo vs V
fig, ax = plt.subplots()
ax.plot(Psi_solo, V)   
ax.grid(False, linestyle='-')
plt.title('Teste P50 -2')
ax.set(xlabel='ψsolo (MPa)', ylabel='V (mol m2 s-1 MPa-1)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

# Gráfico Psi_raiz vs V
fig, ax = plt.subplots()
ax.plot(Psi_solo, V)   
ax.grid(False, linestyle='-')
ax.set(xlabel='Psi_raiz (MPa)', ylabel='V (mol m2 s-1 MPa-1)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

# Gráfico V vs W
fig, ax = plt.subplots()
ax.plot(W, V)   
ax.grid(False, linestyle='-')
plt.title('Teste P50 -2')
ax.set(xlabel='W (gH2O/gsolo)', ylabel='V (mol m2 s-1 MPa-1)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()


#### Calculo quantidade de água puxada pela planta (W_uso; mol m2 s) 
# ARRUMAR CÁLCULO 
W_uso = Psi_dif * V
print("W_uso")
print(W_uso)
print("\n")

# Gráfico W_uso vs W
fig, ax = plt.subplots()
ax.plot(W_uso, W)   
ax.grid(False, linestyle='-')
ax.set(xlabel='W_uso (ver unidade)', ylabel='W (gH2O/gsolo)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

#### Calculo W atualizado (W_update; VER UNIDADE)
W_update = W - W_uso
print("W_update")
print(W_update)