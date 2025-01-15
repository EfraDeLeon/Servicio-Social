#Volumen de un cilindro
import math as m

print('Este programa calcula el volumen de un cilindro.')
radio=float(input('Ingresa el radio de la base del cilindro: '))
altura=float(input('Ingrasa la altura del cilindro: '))

volumen= 3.1416*(radio**2)*altura

print('El volumen del cilindro cuyo radio es %.2f y altura es %.2f, es: %.4f' % (radio,altura,volumen))

volumen2=m.pi*radio**2*altura
print('El volumen del cilindro usando pi de math, cuyo radio es %.2f y altura es %.2f, es: %.4f' % (radio,altura,volumen2))

