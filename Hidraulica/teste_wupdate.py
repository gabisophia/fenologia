#### Cálculo para representar o W atualizado ####

import matplotlib.pyplot as plt
import numpy as np

# Parametros hidraulicos do solo 
theta_sat = 0.4 #g H20/g solo
psi_sat = -0.001 #MPa
b = 7 #sem unidade

# Conteudo volumétrico de água no solo (g H20/g solo)  
theta = np.arange(0.1, theta_sat, 0.001)
# Umidade do solo (gH2O/Gsolo ou m3 m-3) CONFERIR
w = theta / theta_sat 

#### Calculo potencial hidrico do solo (Psi_solo MPa - equação de Clapp & Hornberger)
psi_solo = psi_sat * w ** (-b)

# Gráfico Psi_solo vs W(theta/theta_sat) 
fig, ax = plt.subplots()
ax.plot(W , Psi_solo)   #conferir se está saindo theta/theta_s vs Psi_solo pois antes era somente o theta e ainda está dando erro
ax.grid(False, linestyle='-')
ax.set(xlabel='W (gH2O/gsolo)', ylabel='ψsolo (MPa)')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()


#### Calculo condutância solo-raiz expressa com base na área foliar (ksr; mol m-2 leaf s-1):
K = W ** ((2*b)+3)
Ksr = K * ksr_max
print("ksr")
print(Ksr)
print("\n")
#Ksr = 0.5

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