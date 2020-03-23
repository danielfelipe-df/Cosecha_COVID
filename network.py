import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Número de nodos
N = 1000

#Creo el grafo que va a estar en la mitad
G = nx.watts_strogatz_graph(N,5,0.1,876)

#Le doy una forma circular para poderlo ver mejor.
pos = nx.circular_layout(G)

#Dibujo la red
nx.draw(G, pos=pos, node_size=10, width=0.5)
plt.show()

#Genero la matriz de adjacencia como una matriz de numpy para editar.
matrix = nx.to_numpy_matrix(G)

#La imprimo para verla
print(matrix)

#Genero el primer nodo externo
row = [1]*N
column = [1]*N
column.append(0)

#Lo agrego a la matriz
matrix = np.vstack((matrix, row))
matrix = np.column_stack((matrix, column))

#Lo imprimo para ver el cambio
print(matrix)

#Genero el segundo nodo externo
row.append(0)
column.append(0)

#Lo agrego a la matriz
matrix = np.vstack((matrix, row))
matrix = np.column_stack((matrix, column))

#Lo imprimo para ver el cambio
print(matrix)

#Genero la nueva red
G = nx.from_numpy_matrix(matrix)

#Imprimo las posiciones de la vieja red
print(pos)

#Le agrego las posiciones de los nuevos nodos
pos[N] = np.array([2.0,2.0])
pos[N+1] = np.array([-2.0,-2.0])

#Imprimo las posiciones de la nueva red
print(pos)

#Dibujo la nueva red
nx.draw(G, pos=pos, node_size=10, width=0.5)
plt.show()
