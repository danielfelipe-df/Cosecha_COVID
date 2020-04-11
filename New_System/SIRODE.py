import scipy.integrate as sciin
import numpy as np

#Esta función plantea las ecuaciones del modelo SEIR
def modelo_seir(y,t,beta,gamma,sigma,pop):
    #Obtengo los agentes
    S = []
    for i in range(3):
        S.append(y[i])
    E = []
    for i in range(3,6):
        E.append(y[i])
    I = []
    for i in range(6,9):
        I.append(y[i])
    R = []
    for i in range(9,12):
        R.append(y[i])

    #Hay que tener en cuenta que S e I tienen 3 tipos distintos. Son listas.
    dS_dt = [0]*len(S)
    dE_dt = [0]*len(E)
    dI_dt = [0]*len(I)
    dR_dt = [0]*len(R)

    #Tener en cuenta que beta es una matriz
    #Hago el ciclo para los susceptibles
    for i in range(len(S)):
        betaI = 0 
        for j in range(len(beta)):
            betaI += beta[i][j]*I[j]  
        dS_dt[i] = -betaI*S[i]/pop[i]
        
    #Hago el ciclo sobre los expuestos
    for i in range(len(S)):
        dE_dt[i] = -dS_dt[i] - sigma*E[i]

    #Hago el ciclo para los infectados
    for i in range(len(I)):
        dI_dt[i] = sigma*E[i] - gamma*I[i]

    #Hago el ciclo sobre los recuperados
    for i in range(len(I)):
        dR_dt[i] = gamma*I[i]

    result = []
    for i in dS_dt:
        result.append(i)
    for i in dE_dt:
        result.append(i)
    for i in dI_dt:
        result.append(i)
    for i in dR_dt:
        result.append(i)

    #Devuelvo los parámetros
    return result

#Defino la función que me resuelve el sistema de ecuaciones
def resolviendo(ti,tf,S0,E0,I0,R0,beta,gamma,sigma,pop,dt=100):
    t = np.linspace(ti,tf,dt)
    y = []
    for i in S0:
        y.append(i)
    for i in E0:
        y.append(i)
    for i in I0:
        y.append(i)
    for i in R0:
        y.append(i)
    
    solucion = sciin.odeint(modelo_seir, y, t, args=(beta,gamma,sigma,pop))
    
    return (solucion[:,0],solucion[:,1],solucion[:,2],solucion[:,3],solucion[:,4],solucion[:,5],solucion[:,6],solucion[:,7],solucion[:,8],solucion[:,9],solucion[:,10],solucion[:,11])
