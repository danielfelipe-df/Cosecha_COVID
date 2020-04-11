import scipy.integrate as sciin
import numpy as np

#Esta función plantea las ecuaciones del modelo SEIR
def modelo_seir(y,t,beta,gamma,sigma,pop):
    S,E,I,R = y
    dS_dt = -beta*S*I/pop
    dE_dt = beta*S*I/pop - sigma*E
    dI_dt = sigma*E - gamma*I
    dR_dt = gamma*I
    return ([dS_dt,dE_dt,dI_dt,dR_dt])

#Defino la función que me resuelve el sistema de ecuaciones
def resolviendo(ti,tf,S0,E0,I0,R0,beta,gamma,sigma,dt=100):
    t = np.linspace(ti,tf,dt)
    pop = S0+E0+I0+R0
    solucion = sciin.odeint(modelo_seir, [S0,E0,I0,R0], t, args=(beta,gamma,sigma,pop))
    return (solucion[:,0],solucion[:,1],solucion[:,2],solucion[:,3])
