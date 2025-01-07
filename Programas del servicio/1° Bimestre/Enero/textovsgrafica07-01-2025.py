# Sacar los valores del txt y colocarlos en columna y graficarlos

import matplotlib.pyplot as plt
import numpy as np
#Listas a llenar y un contador
datos = []
datos2 = []
datos3 = []
datos4 = []
datos5 = []
i=24

with open("Programas del servicio/1° Bimestre/Enero\data_utc_24-04-08_1303.lvm") as archivo:
    datos = [line.rstrip('\n').split('\t') for line in archivo]
    datos2.append(datos[23][0])
    datos3.append(datos[23][1])
    datos4.append(datos[23][2])
    datos5.append(datos[23][3])
    while len(datos[24]) == len(datos[i]):
        datos2.append(datos[i][0])
        datos3.append(datos[i][1])
        datos4.append(datos[i][2])
        datos5.append(datos[i][3])
        i += 1  

print(datos[23])
print(datos2[0])
print(datos3)

#Graficando
x1 = datos2
y1 = datos3

x2 = datos2
y2 = datos4

x3 = datos2
y3 = datos5

fig = plt.figure()
ax = fig.subplots(2,2)
ax[0,0].plot(x1,y1)
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')
ax[0,0].set_title('Valores Grafica 1')
"""
ax[0,1].plot(x2,y2)
ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('y')
ax[0,1].set_title('Valores Grafica 2')

ax[1,1].plot(x3,y3)
ax[1,1].set_xlabel('x')
ax[1,1].set_ylabel('y')
ax[1,1].set_title('Valores Grafica 3')
"""
plt.show()
