import matplotlib.pyplot as plt

def sumaComplejos(z1,z2):
    return (z1[0]+z2[0],z1[1]+z2[1])

def multComplejos(z1,z2):
    return (z1[0]*z2[0]-z1[1]*z2[1],z1[0]*z2[1]+z1[1]*z2[0])

def sumaVectores(z1,z2):
    return (z1[0]+z2[0],z1[1]+z2[1])

z1 = (2,1)
z2 = (3,4)
suma = sumaComplejos(z1,z2)

# Grafica la suma
plt.quiver(0, 0, z1[0], z1[1], color='g', units='xy',scale=1)
plt.quiver(z1[0], z1[1], z2[0], z2[1], color='b',
           units='xy', scale=1)
plt.quiver(0, 0, suma[0], suma[1], color='r',
           units='xy',scale=1)
plt.axis('scaled')
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.show()
