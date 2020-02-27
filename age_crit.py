# In[1]: descrevendo as variáveis com valores "normais"

import math
import numpy as np
import matplotlib.pyplot as plt

def fa(mu, age_crit, leaf_age):
    return min(1, math.exp(mu * (age_crit - leaf_age)))

mu = [-0.4, 1, 0.6]   #original 12/30/20    umol CO2 m2 s-1
print("young leaf:", mu[0])
print("mature leaf:", mu[1])
print("old leaf:", mu[2])

print("\n")

age_crit = 4    #anos   #range
#a_crit = np.linspace(start = 0.1, stop = 8.3, num = 100)
#print(acrit)

leaf_age = [age_crit/2, age_crit/2 *2, age_crit/2 *3]   #original 1/2/3       #meses ou anos
print("young leaf:", leaf_age[0])
print("mature leaf:", leaf_age[1])
print("old leaf:", leaf_age[2])

#contabilizando o tempo em escala anual

for leaf_age in range (0, age_crit/2 *3):
    if(age_crit > leaf_age[0]):
        # Penalizar a fotossíntese para folhas que tem até 2 anos.
        print (fa(mu[0],age_crit,leaf_age[0]))
        pass
    elif(age_crit >= leaf_age[0] and age_crit < leaf_age[2]):
        # Penalizar a fotossíntese para folhas que tem de 2 até 4 anos.
        print (fa(mu[1],age_crit,leaf_age[1]))
        pass
    elif(age_crit >= leaf_age[1] and age_crit <= leaf_age[2]):
        # Penalizar a fcotossíntese para folhas que tem de 4 até 6 anos.
        print (fa(mu[2],age_crit,leaf_age[2]))
        pass
    else:
        print (f"A folha está morta {leaf_age}")

# %% usando os valores definidos de 0 a 1

import math
import numpy as np
import matplotlib.pyplot as plt

def fa(mu, age_crit, leaf_age):
    return min(1, math.exp(mu * (age_crit - leaf_age)))