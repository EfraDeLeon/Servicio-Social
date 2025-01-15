from math import *

while True:
    r = [float(input('Dame el radio r%d en m: ' % (i+1)))for i in range(3)]

    if r[0]*r[1]*r[2]==0:
        print('Alguno de los datos es inválido, ingresalo nuevamente')
    else:
        break

n=float(input('Dame el número de vueltas: '))

teta1=2*pi*n
teta2=r[0]/r[1]*teta1

L=teta2*r[2]

print('La bicicleta avanzará %f metros ' % L)


