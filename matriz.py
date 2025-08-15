import clase2

tamano=int(input("ingrese el tamaño de la matriz: "))
matriz=clase2.Matriz(tamano)
matriz2=matriz.crear_matriz()

for x in matriz2:
    print(x)

matriz2=matriz.sumar_matrices()
print(f"la suma de la matriz es: {matriz2}")