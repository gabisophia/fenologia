# In[1]: Fórmula efeito da idade foliar com os valores reais definidos

import math
import numpy as np
import matplotlib.pyplot as plt

def fa (mu, age_crit, leaf_age):
    return min(1, math.exp(mu * (age_crit - leaf_age)))

#penalização da fotossíntese pra cada coorte
mu = [-0.4, 1, 0.6]     #original 12/30/20    umol CO2 m2 s-1
print("young leaf:", mu[0])
print("mature leaf:", mu[1])
print("old leaf:", mu[2])

print("\n")
 
#age_crit será derivado do tempo de residência do carbono (trait variante do modelo)
tresid = 6                       #anos   #variante 
age_crit = tresid / 3 * 2        #anos
print(age_crit)

print("\n")

#calculando a idade limite de cada coorte 
age_limit = [age_crit/2, age_crit, age_crit/2 *3]  #meses ou anos
print("young leaf limit:", age_limit[0])
print("mature leaf limit:", age_limit[1])
print("old leaf limit:", age_limit[2])

print("\n")

#preciso criar uma função pra pegar a idade do meio de cada range das coortes
#não consegui fazer isso
leaf_age = [1, 3, 5]
print("young leaf age:", leaf_age[0])
print("mature leaf age:", leaf_age[1])
print("old leaf age:", leaf_age[2])

print("\n")

#contabilizando o tempo em escala anual
for age in age_limit:
    if(age <= age_limit[0]):
        # Penalizar a fotossíntese para folhas que tem até 2 anos.
        print (fa(mu[0],age_crit,leaf_age[0]))
        pass
    elif(age > age_limit[0] and age <= age_limit[1]):
        # Penalizar a fotossíntese para folhas que tem de 2 até 4 anos.
        print (fa(mu[1],age_crit,leaf_age[1]))
        pass
    elif(age > age_limit[1] and age <= age_limit[2]):
        # Penalizar a fcotossíntese para folhas que tem de 4 até 6 anos.
        print (fa(mu[2],age_crit,leaf_age[2]))
        pass
    else:
        print (f"A folha está morta")

#tirando as médias dos 3 resultados de 'fa'

