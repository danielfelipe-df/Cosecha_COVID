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
        suma.append(np.sum(matrix[i])/maxi)

    '''
    Obtengo los diccionarios con los Susceptibles, Expuestos, Infectados y
    Recuperados de cada nodo
    '''
    not_aux = [{}]*4
    not_aux[0] = nx.get_node_attributes(G,'Susceptibles')
    not_aux[1] = nx.get_node_attributes(G,'Expuestos')
    not_aux[2] = nx.get_node_attributes(G,'Infectados')
    not_aux[3] = nx.get_node_attributes(G,'Recuperados')

    '''
    Defino unos diccionarios donde pondré los nuevos Susceptibles, Expuestos,
    Infectados y Recuperados de cada nodo
    '''
    aux = []
    
    #Le quito las personas que se van a pasar a los nodos
    for i in range(4):
        aaux = {}
        #Defino la proporción de personas de cada tipo que se van y las resto
        for j in range(len(matrix)):
            aaux[j] = suma[j]*not_aux[i][j]
            not_aux[i][j] -= aaux[j]
        aux.append(aaux)

    #Hago la asignación de esas personas a los nuevos nodos
    for i in range(len(matrix)):
        #Hago el ciclo sobre los tipos de agentes
        for j in range(4):
            #Hago el ciclo sobre los vecinos del nodo
            for k in range(len(matrix)):
                not_aux[j][k] += (matrix.item((i,k))/500)*aux[j][i]

    #Le asigno los nuevos valores de las personas a los nodos
    nx.set_node_attributes(G, not_aux[0], 'Susceptibles')
    nx.set_node_attributes(G, not_aux[1], 'Expuestos')
    nx.set_node_attributes(G, not_aux[2], 'Infectados')
    nx.set_node_attributes(G, not_aux[3], 'Recuperados')

    return G


#Número de nodos
N = 15

#Creo el grafo que va a estar en la mitad
G = nx.watts_strogatz_graph(N,5,0.1,876)

#Genero la matriz de adjacencia como una matriz de numpy para editar.
matrix = nx.to_numpy_matrix(G)
print(matrix[0])

#Genero la matriz pesada
ran.seed(68798)
for i in range(N*N):
    if(matrix.item(i) != 0):
        matrix.itemset(i,ran.randint(1,11))

#Creo el nuevo grafo pesado
G = nx.from_numpy_matrix(matrix)
print(matrix)

#Defino la población en los nodos
S = 4990
I = 10

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
ran.seed(7678)
#Guardo cada Susceptible en algún nodo
for i in range(S):
    sus[ran.randint(0,N-1)] += 1
print("Susceptibles: ", sus)
#Hago lo mismo para los Infectados
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

