from vpython import *

ventana=graph(width=800, fast=False)
puntos1=gcurve(color=color.blue, label='Coseno')
puntos2=gdots(color=color.red, label='Seno')

for t in range(1000):
    x= t/100*2*pi
    y=cos(x)
    y1=sin(x)
    puntos1.plot(x,y)
    puntos2.plot(x,y)

input("Presiona Enter para cerrar la ventana...")
