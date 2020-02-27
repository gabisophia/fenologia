# %% teste LLS 6 anos
import matplotlib.pyplot as plt
import numpy as np
import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

acrit = 4 
leaf_age = [acrit / 2, acrit / 2 * 2, acrit / 2 * 3]  #years
print(leaf_age)
print("\n")

print("folhas jovens")
u = -0.4              #umol CO2 m2 S-1  
acrit = 4            #year
a = 0.5             #year
print (fa(u,acrit,a))

u = -0.4           #umol CO2 m2 S-1  
acrit = 4         #year
a = 1            #year
print (fa(u,acrit,a))

u = -0.4            #umol CO2 m2 S-1  
acrit = 4         #year
a = 1.5          #year
print (fa(u,acrit,a))

u = -0.4           #umol CO2 m2 S-1  
acrit = 4         #year
a = 1.9            #year
print (fa(u,acrit,a))
print("\n")

print("folhas maduras")
u = 1              #umol CO2 m2 S-1  
acrit = 4         #year
a = 3            #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 4         #year
a = 4            #year
print (fa(u,acrit,a))
print("\n")

print("folhas velhas")
u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 4.5            #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 5            #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 5.5          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 6            #year
print (fa(u,acrit,a))
print("\n")

print ("folhas morreram")


# %% teste LLS 3 anos

import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

acrit = 2
leaf_age = [acrit / 2, acrit / 2 * 2, acrit / 2 * 3]  #years
print(leaf_age)

print("\n")

print("folhas jovens")
u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.3           #year
print (fa(u,acrit,a))

u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.5           #year
print (fa(u,acrit,a))

u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.7           #year
print (fa(u,acrit,a))

u = -0.4           #umol CO2 m2 S-1  
acrit = 2         #year
a = 0.9            #year
print (fa(u,acrit,a))
print("\n")

u = 1              #umol CO2 m2 S-1  
acrit = 2         #year
a = 1.5          #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 2         #year
a = 2            #year
print (fa(u,acrit,a))
print("\n")

print("folhas velhas")
u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.3          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.5          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.7          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 3            #year
print (fa(u,acrit,a))

print ("folhas morreram")


# %% LLS 6 acrit 4

import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))
    
u = -0.4           #umol CO2 m2 S-1  
acrit = 4         #year
a = 1            #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 4         #year
a = 3            #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 4         #year
a = 5            #year
print (fa(u,acrit,a))

# %% LLS 3 acrit 2

u = -0.4            #umol CO2 m2 S-1  
acrit = 2          #year
a = 0.5           #year
print (fa(u,acrit,a))

u = 1              #umol CO2 m2 S-1  
acrit = 2         #year
a = 1.5          #year
print (fa(u,acrit,a))

u = 0.6            #umol CO2 m2 S-1  
acrit = 2         #year
a = 2.5          #year
print (fa(u,acrit,a))

# %%
