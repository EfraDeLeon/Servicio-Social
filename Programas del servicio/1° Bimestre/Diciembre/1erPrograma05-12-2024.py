#If
print(" **If")
a = 3 
b = 2
if b!= 0:
    print("b es diferente de 0")
if a>b:
    c=a+b
else:
    c =a*b
print(c)

#While
print(" **While")
x=0
while x<10:
    print(x)
    x += 1
    
print("Finalizo el ciclo")

lista = ['A','B','C','D','E','F','G','H',1]

#For
print(" **For")

for i in lista:
    print(i)
    if i == 'A':
        print(i*5)