import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Defino la función para dibujar la red
def net_drawing(G,pos,labels,title):
    nx.draw_networkx_labels(G, pos=pos, labels=labels)
    nx.draw(G, pos=pos, node_size=10, width=0.5)
    plt.title(title)
    plt.show()
    plt.clf()

#Defino la función para hacer el intercambio de agentes
def swap(G, matrix):
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
    for i in range(len(matrix)):
        total = sus[i] + exp[i] + inf[i] + rec[i]
        value = suma[i]
        asus[i] = (sus[i]/total)*value
        sus[i] -= asus[i]
        aexp[i] = (exp[i]/total)*value
        exp[i] -= aexp[i]
        ainf[i] = (inf[i]/total)*value
        inf[i] -= ainf[i]
        arec[i] = (rec[i]/total)*value
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

#Esta función me imprime los datos de las características de los nodos
def print_data(i,NS,NE,NI,NR):
    with open("Data_1/node_" + str(i) + ".csv", "a") as myfile:
        for j in range(len(NS)):
            myfile.write(str(NS[j]) + '\t' + str(NE[j]) + '\t' + str(NI[j]) + '\t' + str(NR[j]) + '\n')
