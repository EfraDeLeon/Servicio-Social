# Identificar que hacen los programas

## CalcularPi.py
### Librerías
- Numpy

### ¿Qué hace el código?
Inicia importando la librería numpy y le asigna para usarse np.

En el resto del código lo que hace es asignar a una variable llamada pi el valor de 4, luego de eso calcula con un for en el rango de 1 a 10000 el nuevo valor de pi con if donde si i es igual a 1 pi es igual a pi sino el módulo de i sobre 2 es igual a 0, guarda una variable auxiliar uno el valor de i por 2 menos 1 y luego asigna pi es igual a pi menos 4 sobre el auxiliar uno y sino el módulo de i sobre 2 es diferente de cero se asigna en una variable auxiliar dos es igual a i por dos menos 1 y asigna pi es igual a pi más 4 sobre auxiliar 2.

Al finalizar imprime el valor de la variable pi y vuelve a imprimir el valor de pi, pero ahora desde el comando de numpy como np.pi donde este mismo lo calcula y se imprime

## complejos.py
### Librerías
- Numpy
- Scipy

### ¿Qué hace el código?
Inicia con una variable z1 donde pide ingresar un número complejo desde la terminal, luego otra variable z2 donde pide ingresar otro número complejo.

Después imprime la parte real de z1, siguiente imprime la parte imaginaria de z1 luego al imprimir realiza una suma de z1 con z2 y luego imprime una resta de z1 y z2, al igual que una multiplicación, división y una potencia de los mismos.

de eso importa la librería numpy y le asigna para usarse np, y de scipy.linalg importa resolver que es solve de eso a una variable A le asigna el de np el arreglo de los reales de z2.

## integral.py
### Librerías
- Sympy
### ¿Qué hace el código?
Importa de la librería sympy símbolos, integral, seno y exponencial luego de una sub librería. plotting importa plot.

Siguiente asigna una variable x los símbolos con X, luego a una variable integ le asigna integrar el seno de x dx evaluado de -10 a 10 luego imprime el valor de integ.

Para finalizar grafica el sen de x desde -10 a 10.

## listas.py
### ¿Qué hace el código?
Asigna a una variable llamada ejemplo1; el valor de un arreglo del 1 al 5 luego imprime el contenido de ejemplo1 siguiente de eso asigna otra variable llamada ejemplo2 donde esta tiene cadenas, decimales y booleanos y siguiente lo imprime.

Por último, crea una variable a y le asigna un arreglo vacío y sigue un for que para x en un rango de 100 si el módulo de x sobre dos es igual a cero guarda ese valor en a y por finaliza imprimiendo a.
## MCD_Euclid.py
### ¿Qué hace el código?
Primero en una variable a pide que ingrese un valor entero y ace lo mismo, pero ahora con otra variable llamada b, siguiente de eso a una variable q asigna la división de a sobre b y otra variable r asigna a menos la multiplicación b de por q.

Entra a un ciclo donde r debe ser diferente de 0 donde a le asigna b y b se le asigna r imprime a y b, por siguiente vuelva a hacer las asignaciones de q y r y por último imprime que el máximo común divisor es el valor de b.

## Vectores.py
### Librerías
- Matplotlib

### ¿Qué hace el código?
Importa la librería matplotlib.pyplot y se asigna como plt, siguiente de eso crea una función llamada sumaComplejos donde debe recibir dos valores que son z1 y z2 y lo que hace esa función es regresar el valor de z1 en el apuntador 0 más z2 en el apuntador z2 y z1 en el apuntador 1 más z2 en el apuntador 1.

Crea otra función llamada multComplejos que se deben recibir dos valores que son z1 y z2 y devuelve el valor de z1 en el apuntador 0 por z2 en el apuntador 0 menos z1 en el apuntador 1 ´por z2 en el apuntador 1 y hace esto mismo, pero en vez de menos, es más.

Crea una última función llamada sumaVectores que debe recibir los valores de z1 y z2 donde devuelve lo mismo que la función sumacComplejos. 

Siguiente asigna una variable z1 donde este tiene dos valores que es 2 y 1 y para z2 le asigna 3 y 4 y para una nueva variable llamada suma se le asigna que llame a la función sumaComplejos dando los valores de z1 y z2

Por último crea una gráfica de la suma con plt.quiver que es asignación de vectores por los puntos 0 y 0, z1 en 0 y z1 en 1 de color verde con unidades xy a una escala de 1 para otro vector ahora de z1 en 0 en z1 en 1 a z2 en cero y z2 en uno de color azul con unidades en xy su escala es 1 y crea un último vector donde 0 y 0 a la suma en 0 a suma en 1 de color rojo en unidades de xy es escala de 1.

Para sus ejes esta escalada con sus límites x en 0 a 6 y para y de 0 a 6 y por último muestra la gráfica.

### Instalar las librerías

|Librerías | Comando para instalar |
|---------|-----------------------|
| numpy | pip install numpy|
| scipy | pip install scipy|
| sympy | pip install sympy|
| matplotlib | pip install matplotlib|


