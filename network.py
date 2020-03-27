import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as ran

#Defino la función para dibujar la red
def net_drawing(G,pos,labels,title):
    nx.draw_networkx_labels(G, pos=pos, labels=labels)
    nx.draw(G, pos=pos, node_size=10, width=0.5)
    plt.title(title)
    plt.show()
    plt.clf()

#Defino la función para hacer el intercambio de agentes
def swap(G, matrix, maxi):
    #Hallo la suma de los pesos alrededor de cada nodo
    suma = []
    for i in range(len(matrix)):
        suma.append(np.sum(matrix[i]))

    '''
    Obtengo los diccionarios con los Susceptibles, Expuestos, Infectados y
    Recuperados de cada nodo
    '''
    sus = nx.get_node_attributes(G,'Susceptibles')
    exp = nx.get_node_attributes(G,'Expuestos')
    inf = nx.get_node_attributes(G,'Infectados')
    rec = nx.get_node_attributes(G,'Recuperados')

    '''
    Defino unos diccionarios donde pondré los nuevos Susceptibles, Expuestos,
    Infectados y Recuperados de cada nodo
    '''
    asus = {}
    aexp = {}
    ainf = {}
    arec = {}
    
    #Defino la proporción de personas de cada tipo que se van y las resto
    value = 0
    for i in range(len(matrix)):
        value = suma[i]/maxi
        asus[i] = value*sus[i]
        sus[i] -= asus[i]
        aexp[i] = value*exp[i]
        exp[i] -= aexp[i]
        ainf[i] = value*inf[i]
        inf[i] -= ainf[i]
        arec[i] = value*rec[i]
        rec[i] -= arec[i]

    #Hago la asignación de esas personas a los nuevos nodos
    for i in range(len(matrix)):
        #Hago el ciclo sobre los vecinos del nodo
        for j in range(len(matrix)):
            value = matrix.item((i,j))/suma[i]
            sus[j] += value*asus[i]
            exp[j] += value*aexp[i]
            inf[j] += value*ainf[i]
            rec[j] += value*arec[i]

    #Le asigno los nuevos valores de las personas a los nodos
    nx.set_node_attributes(G, sus, 'Susceptibles')
    nx.set_node_attributes(G, exp, 'Expuestos')
    nx.set_node_attributes(G, inf, 'Infectados')
    nx.set_node_attributes(G, rec, 'Recuperados')

    return G

def print_data(i,NS,NE,NI,NR,k):
    with open("Data_" + str(k) + "/node_" + str(i) + ".csv", "a") as myfile:
        for j in range(len(NS)):
            myfile.write(str(NS[j]) + '\t' + str(NE[j]) + '\t' + str(NI[j]) + '\t' + str(NR[j]) + '\n')

'''
Número de nodos
N = 15

Creo el grafo que va a estar en la mitad
G = nx.watts_strogatz_graph(N,5,0.1,876)

Genero la matriz de adjacencia como una matriz de numpy para editar.
matrix = nx.to_numpy_matrix(G)
print(matrix[0])

Genero la matriz pesada
ran.seed(68798)
for i in range(N*N):
    if(matrix.item(i) != 0):
        matrix.itemset(i,ran.randint(1,11))

Creo el nuevo grafo pesado
G = nx.from_numpy_matrix(matrix)
print(matrix)

Defino la población en los nodos
S = 4990
I = 10

Defino el diccionario que me va a dar la propiedad de Susceptibles, Expuesto, Infectado y Recuperado
sus = {}
exp = {}
inf = {}
rec = {}
for i in range(N):
    sus[i] = 0
    exp[i] = 0
    inf[i] = 0
    rec[i] = 0
Defino la semilla para el número aleatorio de susceptibles
ran.seed(7678)
Guardo cada Susceptible en algún nodo
for i in range(S):
    sus[ran.randint(0,N-1)] += 1
print("Susceptibles: ", sus)
Hago lo mismo para los Infectados
ran.seed(673828)

for i in range(I):
    inf[ran.randint(0,N-1)] += 1
print("Infectados: ", inf)
    
#Guardo los Susceptibles, Expuestos, Infectados y Recuperados como atributos del nodo
nx.set_node_attributes(G, sus, 'Susceptibles')
nx.set_node_attributes(G, exp, 'Expuestos')
nx.set_node_attributes(G, inf, 'Infectados')
nx.set_node_attributes(G, rec, 'Recuperados')    

#Le doy una forma circular para poderlo ver mejor.
pos = nx.circular_layout(G)

net_drawing(G,pos,sus,'Susceptibles')

#Hago el intercambio de personas
G = swap(G, matrix, 500)
sus = nx.get_node_attributes(G,'Susceptibles')
exp = nx.get_node_attributes(G,'Expuestos')
inf = nx.get_node_attributes(G,'Infectados')
rec = nx.get_node_attributes(G,'Recuperados')


#Dibujo la red
net_drawing(G,pos,sus,'Susceptibles')
#net_drawing(G,pos,exp,'Expuestos')
#net_drawing(G,pos,inf,'Infectados')
#net_drawing(G,pos,rec,'Recuperados')
'''
