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

#Dibujo la red
net_drawing(G,pos,sus,'Susceptibles')
net_drawing(G,pos,exp,'Expuestos')
net_drawing(G,pos,inf,'Infectados')
net_drawing(G,pos,rec,'Recuperados')
