#Los primeros 7 números primos
#Ahora los 1000
listaNum = []
for i in range(2,1000):
    es_primo = True
    for num in listaNum:
        if i%num == 0:
            es_primo = False
            break
    if es_primo:
        listaNum.append(i)
        #Comprobe que hacia los cambios uno por uno con el siguiente print
        #print(listaNum)

print(listaNum)