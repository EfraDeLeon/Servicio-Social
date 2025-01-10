import matplotlib.pyplot as plt
import numpy as np

# Listas para los datos
datos2, datos3, datos4, datos5 = [], [], [], []
i = 24  # Inicio del índice para datos

# Leer datos desde el archivo
with open("Programas del servicio/1° Bimestre/Enero/data_utc_24-04-08_1303.lvm") as archivo:
    datos = [line.rstrip('\n').split('\t') for line in archivo]
    datos2.append(datos[23][0])
    datos3.append(datos[23][1])
    datos4.append(datos[23][2])
    datos5.append(datos[23][3])
    while len(datos[24]) >= len(datos[i]) or len(datos[23]) == len(datos[i]):
        datos2.append(datos[i][0])
        datos3.append(datos[i][1])
        datos4.append(datos[i][2])
        datos5.append(datos[i][3])
        i += 1  
        if i == 76723:
            break

# Convertir los valores a flotantes
x = [float(valor) for valor in datos2][:5000]
y1 = [float(valor) for valor in datos3][:5000]
y2 = [float(valor) for valor in datos4][:5000]
y3 = [float(valor) for valor in datos5][:5000]

# Función para calcular la Transformada de Fourier Discreta (DFT)
def dft_manual(signal):
    """
    Calcula la Transformada de Fourier Discreta (DFT) de manera manual.
    :param signal: Señal en el dominio del tiempo (lista o array).
    :return: Transformada de Fourier (valores complejos).
    """
    N = len(signal)
    X = []  # Aquí se almacenarán los valores de la DFT
    for k in range(N):
        X_k = 0
        for n in range(N):
            X_k += signal[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(X_k)
    return np.array(X)

# Calcular la frecuencia de muestreo
if len(x) > 1:
    fs = 1 / (x[1] - x[0])  # Intervalo de tiempo entre muestras
else:
    raise ValueError("La lista 'x' no tiene suficientes datos para calcular fs.")

# Calcular las frecuencias correspondientes
frecuencia = np.fft.fftfreq(len(y1), d=1/fs)

# Transformada de Fourier Discreta (DFT) manual
Fourier1 = dft_manual(y1)
Fourier2 = dft_manual(y2)
Fourier3 = dft_manual(y3)

# Magnitudes
Magnitud1 = np.abs(Fourier1)
Magnitud2 = np.abs(Fourier2)
Magnitud3 = np.abs(Fourier3)

# Filtrar frecuencias positivas
mask = frecuencia >= 0
frecuencia = frecuencia[mask]
Magnitud1 = Magnitud1[mask]
Magnitud2 = Magnitud2[mask]
Magnitud3 = Magnitud3[mask]

# Graficar las señales originales y sus transformadas
fig, ax = plt.subplots(3, 2, figsize=(12, 10))

# Señales originales
ax[0, 0].plot(x, y1)
ax[0, 0].set_title("Canal 1 (HN)")
ax[0, 1].plot(x, y2, 'y')
ax[0, 1].set_title("Canal 2 (HeW)")
ax[1, 0].plot(x, y3, 'g')
ax[1, 0].set_title("Canal 3 (Ez)")

# Transformadas de Fourier
ax[1, 1].plot(frecuencia, Magnitud1)
ax[1, 1].set_title("Transformada de Fourier Discreta - Canal 1")
ax[2, 0].plot(frecuencia, Magnitud2, 'y')
ax[2, 0].set_title("Transformada de Fourier Discreta - Canal 2")
ax[2, 1].plot(frecuencia, Magnitud3, 'g')
ax[2, 1].set_title("Transformada de Fourier Discreta - Canal 3")

# Ajustes generales
for a in ax.flatten():
    a.set_xlabel("Frecuencia (Hz)" if "Transformada" in a.get_title() else "Tiempo (s)")
    a.set_ylabel("Magnitud" if "Transformada" in a.get_title() else "Amplitud")
    a.grid()

plt.tight_layout()
plt.show()
