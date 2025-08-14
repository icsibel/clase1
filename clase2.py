import random
class Matriz:
    matriz=[]
    tamano= 0

    def __init__(self, tamano):
        self.tamano=tamano

    def crear_matriz(self):
        
        for i in range(self.tamano):
            filas=[]
            for j in range(self.tamano):
                filas.append(random.randint(1,20))
            self.matriz.append(filas)
        return self.matriz
    
#    def funcion_util(self):
#       for i in range(len(self.matriz)):
#            for j in range(len(self.matriz[i])):
#                pass

    def sumar_matrices(self):
        suma=0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if (i + j) % 2 ==0:
                    suma+=self.matriz[i][j]
        return suma
    
    def promedio_matriz(self):
        total_matriz= self.tamano * self.tamano
        suma=0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                suma+=self.matriz[i][j]
        promedio=suma/total_matriz
        return promedio
    
    def num_divisiblesx2(self):
        contador= 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if j % 2 ==0:
                    contador+=1
        return contador

    def diagonal(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if j==i: 
                    print (self.matriz[i][j], end=" ")
                else:
                    print (" ", end= " ")

    



