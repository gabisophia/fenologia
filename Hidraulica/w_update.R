# Parametros hidraulicos do solo 
theta_sat = 0.4 #g H20/g solo
Psi_sat = -0.001 #MPa
b = 7 #sem unidade

# Conteudo volum�trico de �gua no solo (i.e. g H20/g solo)
theta = seq (0.1, theta_sat, len=1000)

# Umidade do solo
W = theta/theta_sat
print (W)
# Calculo potencial hidrico do solo (Psi_solo MPa - equa��o de Clapp & Hornberger 1978 - Empirical Equations for Some Soil Hydraulic Properties)
Psi_solo = Psi_sat * W ^ (-b)
plot (Psi_solo~I(W), type="l")


# Calculo condutância solo-raiz expressa com base na área foliar (ksr; mol m-2 leaf s-1):
#Ksr = W ^ (2*b + 3)
#print(Ksr)
Ksr = 0.5

# Parametros faltantes para calcular o psi da raiz
# ARRUMAR VALOR
E = 9e-5 #transpiration mol m-2 leaf s-1 

# Calculo potencial hídrico da raíz (Eller et al. 2018)
Psi_raiz = Psi_solo - (E / Ksr)
plot (Psi_raiz~I(W), type="l")


#plot
plot(psi_raiz~W, type="l",ylim=c(-15,0),
     ylab=expression(Psi~"("*MPa*")"),xlab="Soil water content (Normalized)")
lines(psi_solo~W,col=2)
legend("topleft",legend=c(expression(Soil~Psi),expression(Root~Psi)),
       col=c(2,1),lty=1,bty="n")
psi_raiz-psi_solo

# Calculo diferença de pressão entre a raiz e a planta MPa s
#Psi_dif = Psi_raiz - Psi_solo
Psi_dif = -2

# Calculo de V (Manzoni et al 2013) com fator de altura
rho <- 997 #kg/m3 
g <- 9.8#m/s2
alt <- 20#m
conv <- 1e-6 # Pa to MPa
Psi_g <- rho*g*alt*conv

V = 1 / (1+ ((Psi_solo - Psi_g) / P50)^a)
plot (V~Psi_solo, type="l", ylim=c(0,1))
plot (V~I(W), type="l", ylim=c(0,1))
print (V)

# Calculo quantidade de água puxada pela planta (W_uso; mol m2 s) 
# ARRUMAR CÁLCULO 
W_uso = Psi_dif * V
plot (W_uso~I(W), type="l", ylim=c(0,1))
print(W_uso)

# Calculo W atualizado (W_update; VER UNIDADE)
W_update = W - W_uso
print(W_update)

