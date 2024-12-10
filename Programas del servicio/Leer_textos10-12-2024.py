#Programa para leer archivos

#Funcion Open
archivo = open("Programas del servicio\Texto.txt")
#Funcion Read
print(archivo.read())

#Para archivos csv
print(archivo.readline(10))

archivo = open("Programas del servicio\Texto.csv")

print(archivo.read())

#Funcion with, open y readlines
with open("Programas del servicio\Texto.csv") as archivo2 :
    print(archivo2.readlines())