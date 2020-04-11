import network as net
import SIRODE as SIR
import ZipfDistance as ZD
import networkx as nx
import numpy as np
import random as ran

#Leo le archivo donde está la información de población y ubicación.
my_data = np.genfromtxt("BaseCol_Dep.csv", delimiter=';', dtype=None, encoding='utf-8-sig')

#Defino el número de nodos
N = len(my_data)

#Guardo los atributos de nombre y población, y la propiedad de posición
name = {}
pop = {}
lat = []
lon = []
for i in range(N):
    name[i] = my_data[i][0]
    pop[i] = my_data[i][1]
    lat.append(my_data[i][2])
    lon.append(my_data[i][3])

#Creo la red con el número de nodos adecuados
G = nx.empty_graph(N)

#Creo los archivos donde se van a imprimir los distancias y los Zipf
file1 = open("vinculos.csv", "w")
file2 = open("zipf.csv", "w")

#Imprimo la distancia, el Zipf y agrego el vínculo a la red
kk = 1.3345e-8
for i in range(N):
    for j in range(i+1,N):
        #Hallo la distancia
        dist = ZD.coordinatetodistance(lat[i],lon[i],lat[j],lon[j])
        #Hallo el zipf
        zipf = ZD.ZipfGravity(kk,pop[i],pop[j],dist)
        #Imprimo la distancia y el zipf en los archivos correspondientes
        file1.write(str(name[i]) + '\t' + str(name[j]) + '\t' + str(dist) + '\n')
        file2.write(str(name[i]) + '\t' + str(name[j]) + '\t' + str(zipf) + '\n')
        #Agrego el vínculo con su peso
        G.add_edge(i, j, weight=float(zipf))
file1.close()
file2.close()

#Obtener la matriz de pesos
matrix = nx.to_numpy_matrix(G)

#Hallo la suma de los pesos alrededor de un nodo
sumv = []
for i in range(N):
    sumv.append(np.sum(matrix[i]))
aux = sumv[:]
sumv.sort()

#Los imprimo
file1 = open("Suma_pesos.csv", "w")
for i in range(N):
    for j in range(N):
        if(sumv[i] == aux[j]):
            file1.write(name[j] + '\t' + str(sumv[i]) + '\n')
            break
file1.close()

#Defino las variables de las personas en la red
I0 = 1
beta0 = 1.95
gamma0 = 0.8
sigma0 = 0.22

#Agrego el nombre de cada nodo como un atributo de cada nodo
nx.set_node_attributes(G, name, 'Nombre')
        
#Defino el diccionario que me va a dar la propiedad de Susceptibles, Expuesto, Infectado y Recuperado
sus = {}
exp = {}
inf = {}
rec = {}
for i in range(N):
    sus[i] = pop[i]
    exp[i] = 0
    inf[i] = 0
    rec[i] = 0
    
#Cundinamarca es el nodo número 2, entonces le sumo un infectado
inf[2] += 1
sus[2] -= 1

#Guardo los Susceptibles, Expuestos, Infectados y Recuperados como atributos del nodo
nx.set_node_attributes(G, sus, 'Susceptibles')
nx.set_node_attributes(G, exp, 'Expuestos')
nx.set_node_attributes(G, inf, 'Infectados')
nx.set_node_attributes(G, rec, 'Recuperados')    

#Le doy una forma circular para poderlo ver mejor
pos = nx.circular_layout(G)

print(name)

#infected = np.genfromtxt("casos_importados.csv", delimiter='\t', dtype=None, encoding='utf-8-sig')

#Hacer el ciclo sobre T pasos de tiempo
T = 2
dt = 100
ti = 0
tf = ti + dt
for i in range(T):
    '''
    if(i<30):
        #Obtengo el atributo de infectados y lo modifico
        inf = nx.get_node_attributes(G, 'Infectados')
        for j in range(1,len(infected)):
            if(int(infected[j][0]) == i):
                inf[int(infected[j][2])] += int(infected[j][4])
                #Los vuelvo a añadir a la red
        nx.set_node_attributes(G, inf, 'Infectados')
    '''
            
    #Obtengo los diccionarios de cada tipo de persona
    sus = nx.get_node_attributes(G, 'Susceptibles')
    exp = nx.get_node_attributes(G, 'Expuestos')
    inf = nx.get_node_attributes(G, 'Infectados')
    rec = nx.get_node_attributes(G, 'Recuperados')

    #Hago el ciclo sobre cada nodo haciendo el SIR
    for j in range(N):
        NS,NE,NI,NR = np.array(SIR.resolviendo(ti,tf,sus[j],exp[j],inf[j],rec[j],beta0,gamma0,sigma0))
        #Imprimo los datos
        net.print_data(j,NS,NE,NI,NR)
        #Le asigno los nuevos valores de cada variable al diccionario
        sus[j] = NS[-1]
        exp[j] = NE[-1]
        inf[j] = NI[-1]
        rec[j] = NR[-1]
    
    #Le asigno nuevamente los atributos
    nx.set_node_attributes(G, sus, 'Susceptibles')
    nx.set_node_attributes(G, exp, 'Expuestos')
    nx.set_node_attributes(G, inf, 'Infectados')
    nx.set_node_attributes(G, rec, 'Recuperados')
    
    #Hago el intercambio entre los nodos
    G = net.swap(G, matrix)

    #Dibujo la red con la propiedad de expuestos
    #net.net_drawing(G,pos,inf,'Infectados')
