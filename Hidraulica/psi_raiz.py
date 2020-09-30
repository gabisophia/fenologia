#### Cálculo para representar o W atualizado ####

import matplotlib.pyplot as plt
import numpy as np

# Parametros hidraulicos do solo 
theta_sat = 0.4 #g H20/g solo
Psi_sat = -0.001 #MPa
b = 7 #sem unidade

# Conteudo volumétrico de água no solo (i.e. g H20/g solo)  ARRUMAR
theta = np.arange(0.1, theta_sat, 0.001)

# Umidade do solo
W = theta / theta_sat 

# Calculo potencial hidrico do solo (Psi_solo MPa - equação de Clapp & Hornberger 1978 - Empirical Equations for Some Soil Hydraulic Properties)
Psi_solo = Psi_sat * W ** (-b)

# Gráfico Psi_solo vs W(theta/theta_sat)   ARRUMAR  
fig, ax = plt.subplots()
ax.plot(W , Psi_solo)   #conferir se está saindo theta/theta_s vs Psi_solo pois antes era somente o theta e ainda está dando erro

ax.grid(False, linestyle='-')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

plt.show()


# Calculo condutância solo-raiz expressa com base na área foliar (ksr; mol m-2 leaf s-1):
Ksr = W ^ ((2*b)+3)


#Parametros faltantes para calcular o psi da raiz
E = 0.35 #transpiration mol m-2 leaf s-1

# Calculo potencial hídrico da raíz (Eller et al. 2018)
Psi_raiz = Psi_solo - (E / Ksr)

# Gráfico Psi_raiz vs W
fig, ax = plt.subplots()
ax.plot(W , Psi_raiz)   #conferir se está saindo theta/theta_s vs Psi_solo pois antes era somente o theta e ainda está dando erro

ax.grid(False, linestyle='-')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

plt.show()









#Ψr como uma função da condutância solo-raiz expressa com base na área foliar (ksr; mol m-2 leaf s-1):

#pot raiz = pot solo - (transpiração / ksr)

#mudanças de ksr são dominadas por mudanças de condutância hidráulica do solo, baseado em Clapp & Hornberger

#ksr = ksrmax (theta/thetas)^(2b+3)