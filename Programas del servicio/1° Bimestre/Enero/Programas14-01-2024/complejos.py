#complejos
z1=complex(input("Dame un numero complejo "))
z2=complex(input("Dame otro numero complejo "))
 
print("Parte real de z1", z1.real)
print("Parte imaginaria de z1", z1.imag)

print("Suma ", z1+z2)

print("Resta ", z1-z2)

print("Multi ", z1*z2)

print("Divi ", z1/z2)

print("Potencia ", z1**z2)


#resolviendo div de imaginarios a patita como un sistema de ec

import numpy as np
from scipy.linalg import solve
A=np.array([[z2.real]])
