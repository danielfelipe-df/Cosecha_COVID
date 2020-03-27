import network as net
import SIRODE as SIR
import networkx as nx
import numpy as np
import random as ran

#Defino las variables de las personas en la red
S0 = 59999970
E0 = 0
I0 = 30
R0 = 0
beta0 = 1.95
gamma0 = 0.8
sigma0 = 0.22

#Defino las variables de la red
N = 30
param = 30

#Creo el grafo
G = nx.watts_strogatz_graph(N,param,0,876)

#Genero la matriz de adjacencia como una matriz de numpy para editar
matrix = nx.to_numpy_matrix(G)
#Hago que sea una matriz pesada
ran.seed(636748)
for i in range(N*N):
    if(matrix.item(i) != 0):
        matrix.itemset(i, ran.randint(1,10))
        
#Defino el diccionario que me va a dar la propiedad de Susceptibles, Expuesto, Infectado y Recuperado
sus = {}
exp = {}
inf = {}
rec = {}
for i in range(N):
    sus[i] = 0
    exp[i] = 0
    inf[i] = 0
    rec[i] = 0
#Defino la semilla para el número aleatorio de susceptibles
ran.seed(7645)
#Guardo cada Susceptible en algún nodo
for i in range(S0):
    #sus[ran.randint(0,N-1)] += 1
    sus[int(N*ran.gauss(0.5,0.17))%N] += 1
print("Susceptibles: ", sus)
#Hago lo mismo para los Infectados
#ran.seed(6738)
for i in range(I0):
    inf[i] += 1
print("Infectados: ", inf)

#Guardo los Susceptibles, Expuestos, Infectados y Recuperados como atributos del nodo
nx.set_node_attributes(G, sus, 'Susceptibles')
nx.set_node_attributes(G, exp, 'Expuestos')
nx.set_node_attributes(G, inf, 'Infectados')
nx.set_node_attributes(G, rec, 'Recuperados')    

#Le doy una forma circular para poderlo ver mejor
pos = nx.circular_layout(G)

#Hacer el ciclo sobre T pasos de tiempo
T = 100
dt = 1
ti = 0
tf = ti + dt
for i in range(T):
    #Obtengo los diccionarios de cada tipo de persona
    sus = nx.get_node_attributes(G, 'Susceptibles')
    exp = nx.get_node_attributes(G, 'Expuestos')
    inf = nx.get_node_attributes(G, 'Infectados')
    rec = nx.get_node_attributes(G, 'Recuperados')
    #print("Primero: ", sum(sus.values())+sum(exp.values())+sum(inf.values())+sum(rec.values()))
    
    #Hago el ciclo sobre cada nodo haciendo el SIR
    for j in range(N):
        NS,NE,NI,NR = np.array(SIR.resolviendo(ti,tf,sus[j],exp[j],inf[j],rec[j],beta0,gamma0,sigma0))
        #Le asigno los nuevos valores de cada variable al diccionario
        sus[j] = NS[len(NS)-1]
        exp[j] = NE[len(NE)-1]
        inf[j] = NI[len(NI)-1]
        rec[j] = NR[len(NR)-1]
        
        #Imprimo los datos
        net.print_data(j,NS,NE,NI,NR,param)
        
    #Le asigno nuevamente los atributos
    nx.set_node_attributes(G, sus, 'Susceptibles')
    nx.set_node_attributes(G, exp, 'Expuestos')
    nx.set_node_attributes(G, inf, 'Infectados')
    nx.set_node_attributes(G, rec, 'Recuperados')

    #Hago el intercambio entre los nodos
    G = net.swap(G, matrix, 500)

    #print("Tercero: ", sum(sus.values())+sum(exp.values())+sum(inf.values())+sum(rec.values()))

    #Dibujo la red con la propiedad de expuestos
    #net.net_drawing(G,pos,exp,'Expuestos')
