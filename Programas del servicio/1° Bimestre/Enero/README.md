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
## Para convertir el valor de Fourier necesita

- np.abs(Fourier1)

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

## Fourier de manera manual

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


## En el apartado de Program de Foruier

Es una implemtancion de todo lo aprendido anteriormente, donde se implementa lo siguiente:

- Preguntar el nombre del archivo a procesar
- Preguntar sis e requiere el espectro de: 
|1 seg -> 130 muestras | 1 min / 60 seg -> 7800 muestras | 5 min -> 39000 muestras| todo el archivo -> 78000 muestras

- Hacer la obtencion del espectro con la funcion python o con el algoritmo implementado de Fourier

## Tkinter

|Widget|Descripción|
|-------|------|
|Label	|Muestra texto o imágenes estáticas.|
|Button	|Botón interactivo que ejecuta una acción al hacer clic.|
|Entry	|Campo de entrada de texto de una sola línea.|
|Text	|Cuadro de texto de varias líneas.|
|Frame	|Contenedor para agrupar otros widgets.|
|Canvas	|Área para gráficos, formas, líneas, imágenes, etc.|
|Checkbutton|	Casilla de verificación (checkbox).|
|Radiobutton|	Botones de opción (radio buttons) para seleccionar una sola opción.|
|Scale|	Barra deslizante para seleccionar un valor numérico.|
|Spinbox|	Campo de entrada con flechas para incrementar o decrementar un valor.|
|Scrollbar|	Barra de desplazamiento vertical u horizontal.|
|Menu|	Menú desplegable o de opciones.|
|Listbox|	Lista de opciones para seleccionar uno o varios elementos.|
|Combobox|	Menú desplegable (necesita el módulo ttk).|
|Progressbar|	Barra de progreso (necesita el módulo ttk).|
|Messagebox	|Ventana emergente de mensajes (necesita from tkinter import messagebox).|

Documentacion:
- https://docs.python.org/3/library/tkinter.html

## Para calcular la ventana

ventana = tk.Tk()
ventana.title("Programa para lvm")

ancho_ventana = 400
alto_ventana = 300

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

ventana.mainloop()
## Variables

Global sirve para mantener los datos en todo el programa

variables normales son mientras estan en la funcion