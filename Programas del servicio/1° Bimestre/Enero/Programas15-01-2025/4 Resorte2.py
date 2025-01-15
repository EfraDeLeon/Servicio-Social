from vpython import *

ventana0=canvas( align='left', background=color.white) #usando vpython

ventana=graph( align='right')
ventana2=graph( align='left')
puntos=gcurve(graph=ventana, color=color.red)
puntos2=gcurve(graph=ventana, color=color.blue)
puntos3=gcurve(graph=ventana2, color=color.green, dot=True)

k = 0.3
m = 1.0
t = 0.0
Delta_t = 0.1
fric = 0.00 #Coeficiente de fricción, con fric>0 es movimiento amortiguado con fric=0 es perpetuo hasta que termine el for

x = 10.0

v = 0.0

masa = sphere(color=color.red, radius=0.5, pos=vec(x,0,0))#usando vpython
resorte=helix(pos=vec(-13,0,0), axis=vec(x+13,0,0), coils=15, radius=0.3)

#print(x, v, t)
puntos.plot(pos=(t,x))
puntos2.plot(pos=(t,v))
puntos3.plot(pos=(x,v))
for t in range(1000):          #La distancia con respecto al tiempo se comporta como coseno
    rate(50)
    v = v + (-k/m*x-fric/m*v)*Delta_t    #La velocidad con respecto al tiempo se comparta como -seno
    x = x + v*Delta_t
    t = t + Delta_t
    #print(x, v, t)
    puntos.plot(pos=(t,x))
    puntos2.plot(pos=(t,v))
    puntos3.plot(pos=(x,v)) #Obtendremos el espacio fase
    masa.pos = vec(x,0,0) # o puede ser masa.pos.x=x Usando vpython para mover la esfera
    resorte.axis=vec(x+13,0,0)

input("Presiona Enter para cerrar la ventana...")
