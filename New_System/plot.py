import matplotlib.pyplot as plt
import numpy as np

my_data = np.genfromtxt("normalizado.csv", delimiter='\t', dtype=None, encoding='utf-8-sig')

departamentos = []
peso = []

for i in range(len(my_data)):
    departamentos.append(my_data[i][0])
    peso.append(my_data[i][1])

#plt.xticks(rotation = 90)
plt.ylabel("Departamentos")
plt.xlabel("Pesos alrededor del nodo")
plt.barh(departamentos, peso)
plt.title("Suma de los pesos alrededor del nodo")   
#plt.savefig("Figure_Pesos.png")
plt.show()

