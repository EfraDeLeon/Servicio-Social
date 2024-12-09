#Fibonnaci iterativo
#los primeros 20
#Iterativo
print("Fibonnaci en iterativo")
listaNum = []
for i in range(0,21):
    if i < 2:
        listaNum.append(i)
    else :
        listaNum.append(listaNum[i-1] + listaNum[i-2])
print(listaNum)

#Recursivo
print("Fibonnaci en recursivo")

listaNum2 = []
def fi_recursivo(n):
    if n < 2:
        listaNum2.append(n)
        n += 1
        return fi_recursivo(n)
    elif n <= 20: #Limite de los componentes a evaluar
        listaNum2.append(listaNum2[n-1] + listaNum2[n-2])
        n += 1
        return fi_recursivo(n)

fi_recursivo(0)
print(listaNum2)