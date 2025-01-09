# Programas realizados en enero

## Convertir la lista a valores enteros
valores_y_int = [int(valor) for valor in valores_y]  

## Eje x (puedes usar valores enteros o generados automáticamente)
valores_x = range(len(valores_y_int))

## Transforamda de Fourier
- 1-‘np.fft.fft()‘: Calcula la Transformada de Fourier discreta de una secuencia unidimensional.

- 2-‘np.fft.ifft()’: Calcula las Transformada Inversa de Fourier discreta de una secuencia unidimensional.

- 3-‘np.fft.fft2()’: Calcula la Transformada de Fourier bidimensional de una matriz.

- 4-‘np.fft.ifft2()’: Calcula la Transformada Inversa de Fourier bidimensional de una matriz.

- 5-‘np.fft.fftfreq()’: Genera las frecuencias correspondientes a las salidas de ‘fft‘.

- 6-‘np.fft.shift()’: Cambia el dominio de frecuencia de salida para centrarlo alrededor de cero.

- 7-‘np.fft.ishift()’: Deshacer el cambio generados por la función ‘shift()‘.

- 8-‘np.fft.rfft()’: Calcula la Transformada de Fourier discreta de valores reales.

- 9-‘np.fft.irfft()’: Calcula la Transformada Inversa de Fourier discreta para valores reales


## Para seleccionar una cantidad exacta de una lista se usa lo siguiente

x = x1[:130]

o direcctamente

x1 = [float(valor) for valor in datos2][:130]


## Cambios a graficas con axies

fig = plt.figure()
ax = fig.subplots(3,2)
ax[0,0].plot(x,y1_130)
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')
ax[0,0].set_title('Canal 1 HN')



## Para los archivos y seleccionar

datos = [line.rstrip('\n').split('\t') for line in archivo]