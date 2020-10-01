  # Parametros hidraulicos do solo 
  theta_sat = 0.4 #gH20/gsolo
  psi_sat = -0.001 #MPa 
  b = 7 #sem unidade
  
  # Conteudo volumetrico de agua no solo (gH20/g  solo)
  theta = seq (0.01, theta_sat, len=1000)
  # Conteúdo de água do solo 
  W = theta/theta_sat
  print(W)
  
  # Calculo potencial hidrico do solo (Clapp & Hornberger)
  psi_solo = psi_sat * W ^ (-b)
  # plot (psi_solo~I(W), type="l")
  
  # Calculo condutância solo raiz s/ considerar ksr_max
  # ksr dando valores errados. se eu uso um valor fixo de 0.5 por ex o psi da raiz fica com valores coerentes
  # Sperry & Love (2015) New phytologist  207:14-27 dao valores de condutancia hidraulica do solo bem maiores do que 50 kg h-1 MPa-1 m-2
  # O m-2 usado pelo Sperry ? de "?rea basal" (vamos considerar que isso seja area de sapwood) da planta, n?o de folhas. 
  # Ent?o vc tem que dividir esse valor pelo valor de huber (raz?o area sapwood/area foliar)
  k=100# kg h-1 MPa-1 m-2 sapwood 
  hv=0.001#m2 sapwood m-2 leaf
  kg_mol=55.5#convert kg water to mol
  h_s=3600#convert h to s
  ksr_max=(k*kg_mol/h_s)/hv#mol m-2 LEAF s-1
  print(ksr_max)
  ksr = ksr_max*(W ^ (2*b + 3))
  print(ksr)
  # ksr = 0.5
  
  # Calculo potencial h??drico da ra??z (Eller et al. 2018)
  E = 9e-5 #transpiration mol m-2 s-1 que sai do CAETE
  psi_raiz = psi_solo - (E / ksr)
  print(psi_raiz)
  #plot (psi_raiz~I(W), type="l")
  
  # pegando seu plot como exemplo
  # se eu rodo com valores de ksr entre 0 e 1 ainda assim o psi da raiz não está entre 1-2 MPa abaixo do potencial do solo
  par(mfrow=c(2,1))
  plot(psi_raiz~W, type="l",ylim=c(-15,0),xlim=c(0,1),
       ylab=expression(Psi~"("*MPa*")"),xlab="Soil water content (Normalized)")
  lines(psi_solo~W,col=2)
  legend("topleft",legend=c(expression(Soil~Psi),expression(Root~Psi)),
         col=c(2,1),lty=1,bty="n")
  plot(psi_raiz-psi_solo~W,type="l",
       ylim=c(0,-15))