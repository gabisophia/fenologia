############################################
#TESTE COM VALORES REAIS E FIXOS FUNCIONANDO 
############################################

# In[1]: teste LLS 6 anos (sequencia de idades)
import matplotlib.pyplot as plt
import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

print("TESTE LLS 6 ANOS")
print("\n")

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
a = 2            #year
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
print ("folhas morreram")

#gráfico
age = [0.5, 1, 1.5, 2, 3, 4, 4.5, 5, 5.5, 6]
fa = [0.24659696394160643, 0.301194211912202, 0.36787944117144233, 0.4317105234290797, 1, 1, 0.7408182206817179, 0.5488116360940264, 0.40656965974059917, 0.30119421191220214]
plt.plot(age, fa)
plt.title('fa vs age com LLS de 6 anos')
plt.xlabel('leaf age')
plt.ylabel('fa')
plt.show()

print("\n")
print("\n")

# In[2]: teste LLS 3 anos (sequência de idades)
import matplotlib.pyplot as plt
import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

print("TESTE LLS 3 ANOS")
print("\n")
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
a = 1            #year
print (fa(u,acrit,a))
print("\n")

print("folhas maduras")
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

#gráfico
age = [0.3, 0.5, 0.7, 1, 1.5, 2, 2.3, 2.5, 2.7, 3]
fa = [0.5066169923655895, 0.5488116360940264, 0.5945205479701944, 0.6440364210831413, 1, 1, 0.8352702114112721, 0.7408182206817179, 0.6570468198150567, 0.5488116360940264]
plt.plot(age, fa)
plt.title('fa vs age com LLS de 3 anos')
plt.xlabel('leaf age')
plt.ylabel('fa')
plt.show()

print("\n")
print("\n")

# In[3]: teste com LLS 6 (com médias de 'a')
import matplotlib.pyplot as plt
import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

print("TESTE LLS 6 ANOS")

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
print ("folhas morreram")

#gráfico
age = [1, 3, 5]
fa = [0.301194211912202, 1, 0.5488116360940264]
plt.plot(age, fa)
plt.title('fa vs age com LLS de 6 anos')
plt.xlabel('leaf age')
plt.ylabel('fa')
plt.show()

print("\n")

# In[4]: teste com LLS 3 (com médias de 'a')
import matplotlib.pyplot as plt
import math
def fa(u, acrit, a):
    #return min(1,math.exp(u*(acrit-a)))
    return min(1,math.exp(u*(acrit-a)))

print("TESTE LLS 3 ANOS")

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
print ("folhas morreram")

age = [0.5, 1.5, 2.5]
fa = [0.5488116360940264, 1, 0.7408182206817179]
plt.plot(age, fa)
plt.title('fa vs age com LLS de 3 anos')
plt.xlabel('leaf age')
plt.ylabel('fa')
plt.show()


    


#a_crit = np.linspace(start = 0.1, stop = 8.3, num = 100)