import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import genfromtxt
import math as ma
from datetime import datetime, timedelta

"""numdays=200
base = datetime(2020,2,27)
date_list = [base - timedelta(days=x) for x in range(numdays)]
ax = plt.gca()
formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)
locator = mdates.DayLocator()
ax.xaxis.set_major_locator(locator)
"""

def modelo_seir(y,t, beta,gamma,sigma,pop):
                S,E,I,R=y
                dS_dt = -beta*S*I/(1*pop)
                dE_dt= beta*S*I/(1*pop) -(sigma)*E
                dI_dt = sigma*E-(gamma)*I
                dR_dt = gamma*I 
                return([dS_dt,dE_dt, dI_dt,dR_dt])

def resolviendo(t_i,t_f,S0,E0,I0,R0,beta,gamma,sigma):
	t=np.linspace(t_i,t_f,500)
	pop=S0+E0+I0+R0
	solucion = scipy.integrate.odeint(modelo_seir, [S0,E0,I0,R0], t, args=(beta,gamma,sigma,pop))
	return(solucion[:,0],solucion[:,1],solucion[:,2],solucion[:,3])
'''
S0=37999999
E0=0
I0=1
R0=0
bettaa=1.95
gammma=0.8
sigma=0.22
I0=10
## Intento 1, una población de tamaño 38.000.000
t_i=0
t_f=100
'''
#t=np.linspace(0,200, 500)
#solucionS,solucionE,solucionI,solucionR=np.array(resolviendo(t_i,t_f,S0,E0,I0,R0,bettaa,gammma,sigma))
##Intento 2, dos poblaciones de tamaño 19.000.000 sumadas
'''
N=20
##Is=np.array([int(2*np.random.rand()) for i in range(N)])
Is=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
print(Is)
pops=[pop/N for i in range(N)]
print(pops)
solItot=np.zeros(500)
solEtot=np.zeros(500)
for i in range(len(pops)): 
	solucions=np.array(resolviendo(t,Is[i],bettaa,gammma,sigma,pops[i]))
	solucionsS,solucionsE,solucionsR=np.array(resolviendoE(t,Is[i],bettaa,gammma,sigma,pops[i]))
	solItot=solItot+solucions
	solEtot=solEtot+solucionsE
'''
#t=np.linspace(t_i,t_f,500)
	

"""
pop2=190000
I02=1
solucion2=50*np.array(resolviendo(t,I02,bettaa,gammma,sigma,pop2))
solucionS2,solucionE2,solucionR2=50*np.array(resolviendoE(t,I02,bettaa,gammma,sigma,pop2))
"""
'''
plt.plot(t, solucionI,label="Poblacion completa con 50 infectados")
#plt.plot(t, solItot,label="Población separada en"+str(N)+" con 50 infectados")

#plt.plot(t, solucionE)
#plt.plot(t, solucionE2)


plt.legend()
plt.show()
'''
