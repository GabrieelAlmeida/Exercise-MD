import matplotlib.pyplot as plt
import numpy as np

df = open('/home/gabriel/Downloads/e.txt','r')
listaItens = []
listaSteps = []
listaTemp = []
listaTotalEnergia = []

time = np.arange(0,100,0.01)

linha = df.readlines()
for i in linha:
    listaItens.append(i.strip())

for l in listaItens:
    listaSteps.append(l.split(" ")[0])
    listaTemp.append(l.split(" ")[6])
    listaTotalEnergia.append(l.split(" ")[22])

#Gráficos
#Temperatura/ Tempo
listaTemp.sort()
plt.plot(time,listaTemp)
plt.xlabel('Tempo')
plt.ylabel('Temperatura')
plt.grid()
plt.show()

#Energia total/ Tempo
listaTotalEnergia.sort()
plt.plot(time, listaTotalEnergia)
plt.xlabel('Tempo')
plt.ylabel('Energia Total')
plt.grid()
plt.show()





      









df.close()