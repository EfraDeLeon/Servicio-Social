from vpython import *
from random import choice

A=[color.red, color.blue, color.green, color.cyan, color.yellow]

def cambiaColor(k):
    global c
    c=c+1
    E.color=A[c%5]

def Radio(x):
    E.radius=regla1.value

ventana = canvas(range=4)

c=0
E=sphere(color=A[c], radius=1.0)

boton1=button(text='Cambia', bind=cambiaColor )
regla1= slider(min=1.0, max=3.0, value=1.0, length=220, bind=Radio)

input("Presiona Enter para cerrar la ventana...")
