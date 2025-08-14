import random 
from Daniel import clase2

tamano= int(input("ingrese dimension de la matriz: "))

matriz= clase2.Matrix(tamano)
matriz2 = matriz.crear_matriz()

for x in matriz2:
    print (x)


     