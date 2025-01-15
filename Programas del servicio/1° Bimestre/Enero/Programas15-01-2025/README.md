# Identificar que hacen los programas

## 1 volumenCilindro.py
### Librerías
- Math

### ¿Qué hace el código?
Se importa la Liberia math como m, de eso imprime en la consola Este programa "calcula el volumen de un cilindro" el cual a dos variables de tipo float pide que ingrese valores que uno es el radio de la base del cilindro y otro es la altura.

Siguiente de eso en una variable se le asigna la fórmula de como se calcula el volumen del cilindro, siguiente de eso imprime el radio y altura y volumen, después de eso en otra variable llamada volumen2 ocupa la función math para poner pi y calcular el respectivo volumen y por último imprime esto como lo anterior.

## 2 Dado.py
### Librerías
- Random

### ¿Qué hace el código?
Inicia una lista con 12 ceros y luego de eso imprime la lista, importando de random que es una biblioteca incluida en python importa la función randint que elige números aleatorios que uno coloque.

Siguiente de eso en un ciclo for en un rango de 1000 hace que dos dados ya con la función randint en 1 al 6 para que tengan valores diferentes, siguiente de eso en un print imprime los valores de los dados en el ciclo for, después hace en una variable la operación de dado uno más el dado dos e imprime esos valores y por ultimo del ciclo for en una lisa ocurrencias en la posición de la suma de los dados menos es igual a la lista ocurrencias en el apuntador de suma de dados menos uno y suma uno al final.

En eso imprime ocurrencias y la suma de la lista de ocurrencias, por último, en una variable llamada probabilidades es igual a j sobre 1000 en un para cada j en la lista ocurrencias, haciendo esta operación para calcular las probabilidades e imprime por último esa variable probabilidades e imprime la suma de la lista de probabilidades

## 3 vpython2.py
### Librerías
- Vpython

### ¿Qué hace el código?
Importa la librería vpython completa, de eso crea un canvas de altura y ancho de 600, asigna a cada variable x, y y z posiciones respecto a cada eje y colores (naranja, azul, verde) de eso crea una variable que sea esfera con texturas de la tierra y hace que con esa variable la esfera rote sobre y y vuelva al origen con un ángulo de pi sobre 2 y por último mientras que sea verdadero el ratio en 50 la esfera girara en y =1 y su origen en x = 2 con un ángulo de 0.05.

## 4 Resorte2.py
### Librerías
- Vpython

### ¿Qué hace el código?
Importa toda librería de vpython y crea tres ventanas la primera es una general donde se mostrará un fondo blanco, la segunda será sobre la misma del lado derecho y la 3ra hacia la izquierda, de eso crea 3 puntos el primero sobre la ventana 1 con el color rojo y el punto2 será de color azul sobre la ventana 1 y el 3re punto será sobre la ventana dos de color ver donde es verdadero.

Crea variables que son k = 0.3, m = 1 y t es igual a 0 una delta de 0.1 una fricción de 0 x de 10 y v de 0, de eso crea una esfera de color rojo con un radio de 0.5 donde se posiciona sobre el eje x, también un resorte sobre las posición -13 hasta x más 13 con un rastro de cola de 15 y un radio de 0.3, de eso imprime los 3 puntos con plot sobre el tiempo de t en x y en v.

Por último, entra a un for de t en un rango de 1000 donde el ratio es de 50 y hace las operaciones de velocidad respecto al -sin, multiplica para x en x más la multiplicación de v por delta_t y hace lo mismo pero en vez de x es t, imprime esos valores en plot donde se obtiene el espacio de fase de eso mueve la posición de la masa sobre el vector en x y para el resorte muestra el eje con el vector de x más 13.

## 5 bicicleta_mcu2.py
### Librerías
- Math

### ¿Qué hace el código?
Hace referencia a cuantos metros debe avanzar una bicicleta ingresando sus valores y las vueltas que debe dar.

Importa la librería math completa y entra a un ciclo mientras verdadero donde pide ingresar a una variable en lista de r, esto pide ser 3 diferentes r siendo r1, r2 y r3, donde hay un sí donde la multiplicación de esas 3 r es igual a 0 te indica que alguno de los datos ingresados es incorrecto sino rompe el ciclo.

De eso pide ingresar en flotante el número de vueltas a dar, de so en dos variables hace operaciones que son teta1 y teta2; donde 2 por pi por n (número de vueltas) y para el segundo hace operaciones con r1 y r2 donde r1 sobre la multiplicación de r2 por teta1, por último, en una variable multiplica teta2 por r3 donde este indica cuantos metros avanzara la bicicleta.

## 6 grafica_con_coor.py
### Librerías
- Vpython

### ¿Qué hace el código?
Importa toda la librería de vpython, donde crea una venta de tamaño 800 que su velocidad sea falta y crea dos puntos donde le primero genera una con curva de color azul con la etiqueta coseno y el segundo punto gdots de color rojo que indica Seno.

Indicando con un for de t para el rango de 1000 en x es igual a a t sobre la multiplicación de dos por 100 por pi, siguiente y es igual a coseno de x y y1 es igual a seno de x y grafica los puntos 1 y 2 con x y y como ejes.

## 7 funcionBotonSlider.py
### Librerías
- Vpython
- Random
### ¿Qué hace el código?
Importa toda la librería de vpython e importa de random la opción choice de eso asigna en una lista los colores rojo, azul, verde, cyan y amarillo de eso crea una función llamada cambiaColor que recibe como parámetro k donde indica una variable global c donde c es igual a c más uno y E color es igual a a con la dirección del módulo de c con 5.

Crea otra función llamada Radio que recibe como parámetro x con la regla de E radios donde es iguala regla1 valor, genera una ventana nueva con el rango de 0 inicia la variable de c es igual la 0 y coloca una esfera con el color de A con el apuntador de c con el radio de 1 y coloca un botón que indica cambia y activa la función cambiColor y relga1 es una barra que tiene sus menciones y activa la función radio.

## 8 Proyecto_DRO.py
### Librerías
- Vpython

### ¿Qué hace el código?
Es un simulador de lanzamiento vertical:

Importa toda la librería de vpyton donde en un canva con una altura de 800 por una anchura de 1200 crea 3 flechas una hacia 5 x, otra a hacia -5 x y la última hacia 5 y donde las x están de color naranja con una anchura de 0.03 y la de y es de color verde con una anchura de 0.03. 

De eso pide ingresar en variable tipo float donde es la altura inicial y la velocidad el lanzamiento y su incremento de tiempo con las variables y0, v0 y delta_t de eso crea 3 variables donde vel es igual a 0 tiempo es igual a 0, a es igual a -9.8 y una pelota que es una esfera de color rojo con un radio de 0.2 y su posición será y0.

Por último, entra en un ciclo mientras verdadero donde en la variable y hace la ecuación de movimiento rectilíneo uniforme y si y es menor o igual a 0 rompe el ciclo en caso contrario sigue calculando la velocidad y la pelota cambiara a la posición de y y va a imprimir y, tiempo y velocidad y cambia el tiempo más delta_t y duerme 0.1.

### Instalar las librerías

|Librerías | Comando para instalar | Documentación |
|---------|-----------------------|----------------|
| math | pip install math| https://docs.python.org/es/3.10/library/math.html |
| vpython | pip install vpython (este desde el cmd)| https://www.glowscript.org/docs/VPythonDocs/index.html |

Al final de cada archivo que tenia python les añadi:
````
input("Presiona Enter para cerrar la ventana...")
````
Para que no se cerrara solo el archivo.
