from vpython import *

canvas(width=600, height=600)

x=arrow(pos=vec(0,0,0), axis=vec(10,0,0), color=color.orange, shaftwidth=0.2, round=True)
y=arrow(pos=vec(0,0,0), axis=vec(0,10,0), color=color.blue, shaftwidth=0.2, round=True)
z=arrow(pos=vec(0,0,0), axis=vec(0,0,10), color=color.green, shaftwidth=0.2, round=True)



E=sphere(texture=textures.earth)

E.rotate(axis=vec(0,1,0),origin=vec(0,0,0),angle=pi/2)

while True:
    rate(50)
    E.rotate(axis=vec(0,1,0),origin=vec(2,0,0),angle=0.05)

