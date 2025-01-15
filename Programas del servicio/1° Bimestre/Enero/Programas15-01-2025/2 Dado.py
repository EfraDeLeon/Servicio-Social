#Tener una lista de 12 ceros

ocurrencias=[0 for n in range(12)]
print(ocurrencias)

from random import randint

for i in range(1000):
    dado = randint(1,6)
    dado2 = randint(1,6)
    #print(dado, dado2)
    suma_dados = dado + dado2
    #print(suma_dados)
    ocurrencias[suma_dados-1]=ocurrencias[suma_dados-1]+1
print(ocurrencias)
print(sum(ocurrencias))

probabilidades = [j/1000 for j in ocurrencias]
print(probabilidades)
print(sum(probabilidades))
