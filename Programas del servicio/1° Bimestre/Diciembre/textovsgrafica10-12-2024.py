# Sacar los valores del txt y colocarlos en columna y graficarlos

import matplotlib.pyplot as plt
import numpy as np
#Listas a llenar y un contador
datos = []
datos2 = []
datos3 = []
i=0
with open("Programas del servicio/1° Bimestre/Diciembre\Texto.csv") as archivo:
    datos = [line.rstrip('\n').split('/') for line in archivo]
    print(datos) 
    while len(datos2) != len(datos):
        if i < 1:
            datos2.append(datos[i][0])
            datos3.append(datos[i][1])
            i += 1
            """
            Comprobacion de las listas llenandoce
            print(datos2)
            print(datos3)
            """
        else:
            datos2.append(datos[i][0])
            datos3.append(datos[i][1])
            """
            Comprobacion de las listas llenandoce
            print(datos2)
            print(datos3)
            """
            i += 1  

print(datos2)
print(datos3)

#Graficando
x = [int(valor) for valor in datos2]
y = [int(valor) for valor in datos3]

plt.plot(x,y)
plt.xlabel('x | Indice')
plt.ylabel('y | Cantidad')
plt.title('Texto vs Grafica')
plt.show()
        
        

