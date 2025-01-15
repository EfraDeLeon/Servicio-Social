from vpython import *

canvas(width=1200, height=800)

arrow(pos=vec(0,0,0), axis=vec(5,0,0), color=color.orange, shaftwidth=0.03)
arrow(pos=vec(0,0,0), axis=vec(-5,0,0), color=color.orange, shaftwidth=0.03)
arrow(pos=vec(0,0,0), axis=vec(0,5,0), color=color.green, shaftwidth=0.03)

#Ecuación de movimiento rectiline uniformemente acelrado para lanzamiento vertical
#y=y0+v0(t)+1/2(a)(t**2)


print('Simulación de lanzamiento vertical, ingresa los datos que se solicitan.')

y0=float(input('Ingresa la altura inicial del lanzamiento (entre 0 y 3): '))
v0=float(input('Ingresa la velocidad inicial del lanzamiento: '))
delta_t=float(input('Ingresa el incremento de tiempo del movimiento: '))


vel=0
tiempo=0
a=-9.8
pelota=sphere(color=color.red, radius=0.2, pos=vec(0,y0,0));
#considerar el radio de la esfera
while True :    
    y = y0+v0*tiempo+(1/2)*(a)*tiempo**2
    if y<=0:
        break
    vel=v0+a*tiempo
    pelota.pos=vec(0,y,0)
    print('(0,%f,0)' % y)
    print('tiempo=%f' % tiempo)
    print('velocidad=%f ' % vel)
    print()
    tiempo=tiempo+delta_t
    sleep(0.1)
    pass
    
input("Presiona Enter para cerrar la ventana...")

