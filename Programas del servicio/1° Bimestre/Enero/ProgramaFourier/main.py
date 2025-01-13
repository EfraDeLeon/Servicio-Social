import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
#Variables
archivo_cargado = False
# Funciones
def leer_archivo():
    global archivo_cargado
    global colum1
    global colum2
    global colum3
    global colum4
    datos,colum1,colum2,colum3,colum4  = [],[],[],[],[]
    i=24
    archivo_seleccionado = filedialog.askopenfilename(
    title="Selecciona un archivo", 
    filetypes=[("Archivos de LabVIEW", "*.lvm"), ("Todos los archivos", "*.*")]
    )
    if archivo_seleccionado:
        archivo_cargado = True
        print(f"Procesando el archivo: {archivo_seleccionado}")
        boton_fourier.config(state="normal")
        boton_muestras.config(state="normal")
        with open(archivo_seleccionado) as lectura:
            datos = [line.rstrip('\n').split('\t') for line in lectura]
            colum1.append(datos[23][0])
            colum2.append(datos[23][1])
            colum3.append(datos[23][2])
            colum4.append(datos[23][3])
            while len(datos[24]) >= len(datos[i]) or len(datos[23]) == len(datos[i]):
                colum1.append(datos[i][0])
                colum2.append(datos[i][1])
                colum3.append(datos[i][2])
                colum4.append(datos[i][3])
                i += 1  
                if i == 76723:
                    return colum1, colum2, colum3, colum4
    else:
        archivo_cargado = False
        print("No se seleccionó ningún archivo.")

def seleccion_muestras():
    pantalla_principal.pack_forget()
    apartado_1.pack()
def seleccion_espectro_1():
    pantalla_principal.pack_forget()
    apartado_1_1.pack()
def seleccion_espectro_2():
    apartado_1_1.pack_forget()
    apartado_2.pack()

def espectro_de_muestras(opcion):
    if opcion == 1:
        x = [float(valor) for valor in colum1][:130]
        y1 = [float(valor) for valor in colum2][:130]
        y2 = [float(valor) for valor in colum3][:130]
        y3 = [float(valor) for valor in colum4][:130]
        grafica_de_muestras(x,y1,y2,y3)
    elif opcion == 2:
        x = [float(valor) for valor in colum1][:7800]
        y1 = [float(valor) for valor in colum2][:7800]
        y2 = [float(valor) for valor in colum3][:7800]
        y3 = [float(valor) for valor in colum4][:7800]
        grafica_de_muestras(x,y1,y2,y3)
    elif opcion == 3:
        x = [float(valor) for valor in colum1][:39000]
        y1 = [float(valor) for valor in colum2][:39000]
        y2 = [float(valor) for valor in colum3][:39000]
        y3 = [float(valor) for valor in colum4][:39000]
        grafica_de_muestras(x,y1,y2,y3)
    elif opcion == 4:
        x = [float(valor) for valor in colum1]
        y1 = [float(valor) for valor in colum2]
        y2 = [float(valor) for valor in colum3]
        y3 = [float(valor) for valor in colum4]
        grafica_de_muestras(x,y1,y2,y3)

def grafica_de_muestras(x,y1,y2,y3):
    fig, ax = plt.subplots(3, 1, figsize=(6, 10))
    ax[0].plot(x, y1)
    ax[0].set_title("Canal 1 (HN)")
    ax[1].plot(x, y2, 'y')
    ax[1].set_title("Canal 2 (HeW)")
    ax[2].plot(x, y3, 'g')
    ax[2].set_title("Canal 3 (Ez)")
    plt.tight_layout()
    plt.show()

def espectro_de_funcion(opcion):
    if opcion == 1:
        x = [float(valor) for valor in colum1][:130]
        y1 = [float(valor) for valor in colum2][:130]
        y2 = [float(valor) for valor in colum3][:130]
        y3 = [float(valor) for valor in colum4][:130]
        grafica_espectro_muestras(x,y1,y2,y3)
    elif opcion == 2:
        x = [float(valor) for valor in colum1][:7800]
        y1 = [float(valor) for valor in colum2][:7800]
        y2 = [float(valor) for valor in colum3][:7800]
        y3 = [float(valor) for valor in colum4][:7800]
        grafica_espectro_muestras(x,y1,y2,y3)
    elif opcion == 3:
        x = [float(valor) for valor in colum1][:39000]
        y1 = [float(valor) for valor in colum2][:39000]
        y2 = [float(valor) for valor in colum3][:39000]
        y3 = [float(valor) for valor in colum4][:39000]
        grafica_espectro_muestras(x,y1,y2,y3)
    elif opcion == 4:
        x = [float(valor) for valor in colum1]
        y1 = [float(valor) for valor in colum2]
        y2 = [float(valor) for valor in colum3]
        y3 = [float(valor) for valor in colum4]
        grafica_espectro_muestras(x,y1,y2,y3)

def grafica_espectro_muestras(x,y1,y2,y3):
    fs = 1/ (x[1]-x[0])
    frecuencia = np.fft.fftfreq(len(y1),d=1/fs)

    #Fourier
    Fourier1 = np.fft.fft(y1) 
    Fourier2 = np.fft.fft(y2) 
    Fourier3 = np.fft.fft(y3)

    Magnitud1 = np.abs(Fourier1)
    Magnitud2 = np.abs(Fourier2)
    Magnitud3 = np.abs(Fourier3) 

    mask = frecuencia >= 0
    frecuencia = frecuencia[mask]
    Magnitud1 = Magnitud1[mask]
    Magnitud2 = Magnitud2[mask]
    Magnitud3 = Magnitud3[mask]

    fig, ax = plt.subplots(3, 1, figsize=(6, 10))
    ax[0].plot(frecuencia, Magnitud1)
    ax[0].set_title("Canal 1 (HN)")
    ax[1].plot(frecuencia, Magnitud2, 'y')
    ax[1].set_title("Canal 2 (HeW)")
    ax[2].plot(frecuencia, Magnitud3, 'g')
    ax[2].set_title("Canal 3 (Ez)")
    plt.tight_layout()
    plt.show()

def dft_manual(signal):
    N = len(signal)
    X = []  # Aquí se almacenarán los valores de la DFT
    for k in range(N):
        X_k = 0
        for n in range(N):
            X_k += signal[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(X_k)
    return np.array(X)

def grafica_espectro_algoritmo():
    x = [float(valor) for valor in colum1][:3500]
    y1 = [float(valor) for valor in colum2][:3500]
    y2 = [float(valor) for valor in colum3][:3500]
    y3 = [float(valor) for valor in colum4][:3500]
    if len(x) > 1:
        fs = 1 / (x[1] - x[0])  # Intervalo de tiempo entre muestras
    else:
        raise ValueError("La lista 'x' no tiene suficientes datos para calcular fs.")
    frecuencia = np.fft.fftfreq(len(y1), d=1/fs)
    Fourier1 = dft_manual(y1)
    Fourier2 = dft_manual(y2)
    Fourier3 = dft_manual(y3)

    Magnitud1 = np.abs(Fourier1)
    Magnitud2 = np.abs(Fourier2)
    Magnitud3 = np.abs(Fourier3) 

    mask = frecuencia >= 0
    frecuencia = frecuencia[mask]
    Magnitud1 = Magnitud1[mask]
    Magnitud2 = Magnitud2[mask]
    Magnitud3 = Magnitud3[mask]

    fig, ax = plt.subplots(3, 1, figsize=(6, 10))
    ax[0].plot(frecuencia, Magnitud1)
    ax[0].set_title("Canal 1 (HN)")
    ax[1].plot(frecuencia, Magnitud2, 'y')
    ax[1].set_title("Canal 2 (HeW)")
    ax[2].plot(frecuencia, Magnitud3, 'g')
    ax[2].set_title("Canal 3 (Ez)")
    for a in ax.flatten():
        a.set_xlabel("Frecuencia (Hz)" if "Transformada" in a.get_title() else "Tiempo (s)")
        a.set_ylabel("Magnitud" if "Transformada" in a.get_title() else "Amplitud")
        a.grid()
    plt.tight_layout()
    plt.show()

def regresar_a_principal(apartado_1):
    apartado_1.pack_forget()
    pantalla_principal.pack()
def regresar_a_principal_1_1(apartado_1_1):
    apartado_1_1.pack_forget()
    pantalla_principal.pack()    
def regresar_a_principal_2(apartado_2):
    apartado_2.pack_forget()
    apartado_1_1.pack()

# Ventana principal
ventana = tk.Tk()
ventana.title("Programa para lvm")

ancho_ventana = 400
alto_ventana = 300

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

pantalla_principal = tk.Frame(ventana)

# Widgets
etiqueta = tk.Label(pantalla_principal, text="Bienvenido", font=("Arial", 16))
etiqueta.pack(pady=10)
etiqueta_2 = tk.Label(pantalla_principal, text="Por favor ingrese un archivo", font=("Arial", 12))
etiqueta_2.pack(pady=10)

boton_cargar = tk.Button(pantalla_principal, text="Cargar archivo .lvm", command=leer_archivo)
boton_cargar.pack(pady=5)

boton_muestras = tk.Button(pantalla_principal, text="Espectro de muestras",state="disabled",command=seleccion_muestras)
boton_muestras.pack(pady=5)

boton_fourier = tk.Button(pantalla_principal, text="Espectro de funcion",state="disabled" ,command=seleccion_espectro_1)
boton_fourier.pack(pady=5)

pantalla_principal.pack()

#Apartados

apartado_1 = tk.Frame(ventana)
etiqueta_1 = tk.Label(apartado_1, text="Opciones de muestras",)
etiqueta_1.pack(pady=10)
opcion_1 = tk.Button(apartado_1, text="1 seg -> 130 muestras",command= lambda: espectro_de_muestras(opcion=1))
opcion_1.pack(pady=5)
opcion_2 = tk.Button(apartado_1, text="1 min / 60 seg -> 7800 muestras",command= lambda :espectro_de_muestras(opcion=2))
opcion_2.pack(pady=5)
opcion_3 = tk.Button(apartado_1, text=" 5 min -> 39000 muestras",command= lambda: espectro_de_muestras(opcion=3))
opcion_3.pack(pady=5)
opcion_4 = tk.Button(apartado_1, text="todo el archivo -> 78000 muestras",command= lambda: espectro_de_muestras(opcion=4))
opcion_4.pack(pady=5)
boton_regresar_1 = tk.Button(apartado_1, text="Regresar", command=lambda: regresar_a_principal(apartado_1))
boton_regresar_1.pack(pady=10)

apartado_1_1 = tk.Frame(ventana)
etiqueta_1_1 = tk.Label(apartado_1_1, text="Opciones",)
etiqueta_1_1.pack(pady=10)
opcion_1_espectro_1 = tk.Button(apartado_1_1, text="Funcion python",command= lambda: seleccion_espectro_2())
opcion_1_espectro_1.pack(pady=5)
opcion_2_espectro_1 = tk.Button(apartado_1_1, text="Algoritmo implementado",command= lambda :grafica_espectro_algoritmo())
opcion_2_espectro_1.pack(pady=5)
boton_regresar_1_1 = tk.Button(apartado_1_1, text="Regresar", command=lambda: regresar_a_principal_1_1(apartado_1_1))
boton_regresar_1_1.pack(pady=10)

apartado_2 = tk.Frame(ventana)
etiqueta_2 = tk.Label(apartado_2, text="Opciones de funcion Fourier",)
etiqueta_2.pack(pady=10)
opcion_1_espectro = tk.Button(apartado_2, text="1 seg -> 130 muestras",command= lambda: espectro_de_funcion(opcion=1))
opcion_1_espectro.pack(pady=5)
opcion_2_espectro = tk.Button(apartado_2, text="1 min / 60 seg -> 7800 muestras",command= lambda :espectro_de_funcion(opcion=2))
opcion_2_espectro.pack(pady=5)
opcion_3_espectro = tk.Button(apartado_2, text=" 5 min -> 39000 muestras",command= lambda: espectro_de_funcion(opcion=3))
opcion_3_espectro.pack(pady=5)
opcion_4_espectro = tk.Button(apartado_2, text="todo el archivo -> 78000 muestras",command= lambda: espectro_de_funcion(opcion=4))
opcion_4_espectro.pack(pady=5)
boton_regresar_2 = tk.Button(apartado_2, text="Regresar", command=lambda: regresar_a_principal_2(apartado_2))
boton_regresar_2.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
