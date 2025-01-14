#Calcular Pi
import numpy as np

pi=4
for i in range(1,10000):
    if(i==1):
        pi=pi
    elif(i%2==0):
        aux1=i*2-1
        pi=pi-4/aux1
    elif(i%2!=0):
        aux2=i*2-1
        pi=pi+4/aux2
print(pi)    
print(np.pi)
