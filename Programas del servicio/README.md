# Programas

## Conceptos básicos

La interpretacion para las palabras reservadas como algunas:

- if
- While
- for
- cast
- print

## Números primos
Son los números que solamente pueden ser divididos entre 1 y si mismos
El 1 no es número primo

## Fibonnaci
Para la sucesion de fibonnaci es la siguiente 
Cada número se calcula sumando los dos anteriores a él.
Es decir:

Entonces podemos escribir la regla:

- La regla es xn = xn−1 + xn−2

donde:

- xn es el término en posición "n"
- xn−1 es el término anterior (n−1)
- xn−2 es el anterior a ese (n−2)

## Leer textos

- Implementar un codigo que permita leer archivos txt, cvs y CSV

Python posee lo siguiente para leer archivos

- open => Abrir
- read => Leer
- readLine => Leer linea
- readLines => Leer lineas
- close => cerrar
- with => Con

## Graficar en Python
Es necesario las siguientes librerias
- import matplotlib.pyplot as plt
- import numpy as np

Para poder instalarlos en python se hace el siguiente comando en terminal

-   pip install matplotlib

Tiene lo siguiente
- plt.plot(x,y) : Valores de x y y para la grafica
- plt.xlabel('x') :la etiqueta de x sobre el eje x
- plt.ylabel('y') : la etiqueta de y sobre el eje y
- plt.title('Lab DLS') : El titulo de la grafica
- plt.show() : Como mostrar la grafica

Se muestra como tabla los comandos extras

|Grosor de línea| Color de línea |El color utilizando (R,G,B) en el intervalo [0 1] | Agregando rejilla |
| --------- | --------- | --------- | --------- |
|plt.plot(x,y,linewidth=4)| plt.plot(x,y,color='r') | plt.plot(x,y,color=(0.8,0.9,0)) | plt.grid()|
