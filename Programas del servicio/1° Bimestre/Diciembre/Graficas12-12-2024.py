import matplotlib.pyplot as plt
import numpy as np

#Para los valores de rango de np.arange Inicial, Final, Crecimiento 
x = np.arange(0,20,0.1)
y = x*np.cos(x)


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
