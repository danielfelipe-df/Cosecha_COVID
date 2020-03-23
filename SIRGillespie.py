import math
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
# Input parameters ####################
# int; total population
N = 100
# float; maximum elapsed time
T = 20.0
# float; start time
t = 0.0
# float; rate of infection after contact
beta = 1.95
# float; rate of leaving and entering
gamma=0.8
I0=1
S0=N-I0
R0=0
I = I0
#########################################
# Compute susceptible population, set recovered to zero
S = S0
R=R0
# Initialize results list
SIR_data = []
SIR_data.append((t, S, I, R))
tiempo=[]
Ii=[]
# Main loop
lentime=[]
def Gilles1(beta,gamma,S,I,R):
	T = 20.0
	# float; start time
	t = 0.0
	time=[]
	NI=[]
	NS=[]
	NR=[]
	# Main loop
	while t < T:
		if I==0:
			t=t+0.1
			time.append(t)
			NI.append(I)
			NS.append(S)
			NR.append(R)
		else:
			ran1=np.random.rand()
			ran2=np.random.rand()
			a1=beta*S*I/N
			a2=gamma*I
			A=a1+a2
			dt=(1.0/A)*np.log(float(1.0/ran1))
			t=t+dt
			if ran2<a1/A:
				S=S-1
				I=I+1
			else:
				I=I-1
				R=R+1
			time.append(t)
			NI.append(I)
			NS.append(S)
			NR.append(R)
	lentime.append(len(time))
	return time,NS,NI,NR
nsim=1000
times=[]
Nss=[]
for i in range(nsim):	
	timee,Ns,Ni,Nr=Gilles1(beta,gamma,S,I,R)
	times.append(timee)
	Nss.append(Ni)
	if i%100==0:
		print("se han hecho",i, "iteraciones")
	plt.plot(timee, Ni,'k-', lw=0.3, alpha=0.01,color='blue')
tii=np.linspace(0.,T,500)
def modelo_sir(y,t, beta,gamma):
	S,I,R=y
	dS_dt = -beta*S*I/N
	dI_dt = beta*S*I/N - gamma*I
	dR_dt = gamma*I 
	return([dS_dt, dI_dt,dR_dt])
def resolviendo(t,beta,gamma):
	solucion = scipy.integrate.odeint(modelo_sir, [S0, I0,R0], t, args=(beta,gamma))
	#solucion = numpy.array(solucion)
	return(solucion[:,1])
plt.plot(tii, resolviendo(tii,beta,gamma),linewidth=4, label="I real(t)\n beta={}".format(beta))
plt.grid()
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("I(t)")
plt.title("SIR-DG")
plt.show()
