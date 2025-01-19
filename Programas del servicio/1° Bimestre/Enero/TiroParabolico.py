from vpython import *
import numpy as np

velocidad_inicial = float(input("Ingrese la velocidad inicial (m/s): "))
angulo_inicial = float(input("Ingrese el ángulo de lanzamiento (°): "))
canvas(width=1200, height=800)

arrow(pos=vec(0,0,0), axis=vec(10,0,0), color=color.orange, shaftwidth=0.03)
arrow(pos=vec(0,0,0), axis=vec(-10,0,0), color=color.orange, shaftwidth=0.03)
arrow(pos=vec(0,0,0), axis=vec(0,10,0), color=color.green, shaftwidth=0.03)

pelota=sphere(color=color.red, radius=0.2, pos=vec(0,0,0))

g=9.8
# Convertir el ángulo a radianes
theta = np.radians(angulo_inicial)

# Componentes iniciales de la velocidad
v_x0 = velocidad_inicial * np.cos(theta)
v_y0 = velocidad_inicial * np.sin(theta)

# Tiempo total de vuelo
t_vuelo = 2 * v_y0 / g

# Altura máxima
h_max = (v_y0 ** 2) / (2 * g)

# Alcance horizontal
alcance = v_x0 * t_vuelo

# Imprimir resultados
print(f"Tiempo de vuelo: {t_vuelo:.2f} s")
print(f"Altura máxima: {h_max:.2f} m")
print(f"Alcance horizontal: {alcance:.2f} m\n")

# Animación de la trayectoria
dt = 0.01  # Incremento de tiempo
t = 0

#tiro_parabolico(velocidad_inicial, angulo_inicial)
while t <= t_vuelo:
    rate(50)  # Controlar la velocidad de la animación (100 iteraciones por segundo)
    x = v_x0 * t
    y = v_y0 * t - 0.5 * g * t**2
    pelota.pos = vector(x, y, 0)
    if y < 0:
        break
    t += dt

input("Presiona Enter para cerrar la ventana...")
