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
print(datos2[:10])
print(datos3[:10])
print(datos5[:10])


#Conviertiendo los valores
x = [float(valor) for valor in datos2]
#x = x1[:130]
y1 = [float(valor) for valor in datos3]
#y1_130 = y1[:130]
y2 = [float(valor) for valor in datos4]
#y2_130 = y2[:130]
y3 = [float(valor) for valor in datos5]
#y3_130 = y3[:130]

#Transformada de Fourir de los datos anteriores

#Frecuencia
fs = 1/ (x[1]-x[0])
frecuencia = np.fft.fftfreq(len(y1),d=1/fs)
frecuencia2 = np.fft.fftfreq(len(y2),d=1/fs)
frecuencia3 = np.fft.fftfreq(len(y3),d=1/fs)

mask = frecuencia >= 0
mask1 = frecuencia2 >= 0 
mask3 = frecuencia3 >= 0 

Positivas = frecuencia[mask]
Positivas2 = frecuencia2[mask]
Positivas3 = frecuencia3[mask]

print(Positivas)

#Fourier
Fourier = np.fft.fft(y1) 
Fourier2 = np.fft.fft(y2) 
Fourier3 = np.fft.fft(y3) 
Magnitud1 = np.abs(Fourier)
Magnitud2 = np.abs(Fourier2)
Magnitud3 = np.abs(Fourier3) 

#Graficando
fig = plt.figure()
ax = fig.subplots(3,2)
ax[0,0].plot(x,y1)
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')
ax[0,0].set_title('Canal 1 HN')

ax[0,1].plot(x,y2,'y')
ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('y')
ax[0,1].set_title('Canal 2 HeW')

ax[1,0].plot(x,y3, 'g')
ax[1,0].set_xlabel('x')
ax[1,0].set_ylabel('y')
ax[1,0].set_title('Canal 3 Ez')

ax[1,1].plot(Positivas,Magnitud1[:650])
ax[1,1].set_xlabel('x')
ax[1,1].set_ylabel('y')
ax[1,1].set_title('Transformada de Fourier de Canal 1')
ax[1,1].grid()

ax[2,0].plot(Positivas2,Magnitud2[:650],'y')
ax[2,0].set_xlabel('x')
ax[2,0].set_ylabel('y')
ax[2,0].set_title('Transformada de Fourier de Canal 2')

ax[2,1].plot(Positivas3,Magnitud3[:650], 'g')
ax[2,1].set_xlabel('x')
ax[2,1].set_ylabel('y')
ax[2,1].set_title('Transformada de Fourier de Canal 3')
plt.show()
