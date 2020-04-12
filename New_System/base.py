import network as net
import SIRODE as SIR
import ZipfDistance as ZD
import networkx as nx
import numpy as np
import random as ran
import matplotlib.pyplot as plt

types = 3

pop0 = 4.9e7

pop = [0]*types
pop[0] = 0.3*pop0
pop[1] = 0.3*pop0
pop[2] = 0.4*pop0

aux = [0]*types
beta0 =[aux]*types
beta0[0][0] = 1.95
beta0[1][1] = 0.75*1.95
beta0[2][2] = 0.5*1.95
beta0[0][1] = beta0[1][0] = 0.875
beta0[0][2] = beta0[2][0] = 0.75
beta0[2][1] = beta0[1][2] = 0.625
gamma0 = 0.627
sigma0 = 0.22

sus = [0]*types
inf = [0]*types
exp = [0]*types
rec = [0]*types

for i in range(types):
    sus[i] = pop[i]

inf[0] += 1
sus[0] -= 1

ti = 0

deltat = 300

S1,S2,S3,E1,E2,E3,I1,I2,I3,R1,R2,R3 = np.array(SIR.resolviendo(ti,deltat,sus,exp,inf,rec,beta0,gamma0,sigma0,pop,dt=int(deltat*100)))

t = np.linspace(ti,deltat,deltat*100)

#plt.xlim(0,10)
#plt.ylim(-1,5)
plt.plot(t,I1)
plt.plot(t,I2)
plt.plot(t,I3)
plt.show()
