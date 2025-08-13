import random 

tamano= int(input("ingrese dimension de la matriz: "))

def crear_matriz():
    matriz=[]
    

    for i in range(tamano):
        filas=[]
        for j in range(tamano):
            filas.append(random.randint(1,20))
        matriz.append(filas)
    return matriz

def sumar_matrices(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i + j) % 2 ==0:
                suma+=matriz[i][j]
    return suma

def promedio_matriz(matriz, tamano):
    total_matriz= tamano * tamano
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma+=matriz[i][j]
    promedio=suma/total_matriz
    return promedio

def num_divisiblesx2(matriz):
    contador= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j % 2 ==0:
                contador+=1
    return contador

def diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j==i: 
                print (matriz[i][j], end=" ")
            else:
                print (" ", end= " ")


matriz2=crear_matriz()
for x in matriz2:
    print (x)

print(f"la suma de las posiciones pares es: {sumar_matrices(matriz2)}")
print(f"el promedio de la matriz es: {promedio_matriz(matriz2, tamano)}")
print(f"la cantidad de numeros divisibles por 2 es : {num_divisiblesx2(matriz2)}")
diagonal(matriz2)

     