class Almacen:
    matriz=[]
    nombre=""
    precio=0
    categoria=""
    
    def __init__(self, dimension): 
        self.dimension=dimension
        
        
    def crear(self):
        for i in range(self.dimension):
            fila=[]
            for j in range(self.dimension):
                self.nombre=input("ingrese nombre del producto: ")
                self.precio=int(input("ingrese precio del producto: "))
                self.categoria=input("ingrse categoria del producto: \n 1.carnicos \n 2.lacteos \n 3.grano \n")
                match self.categoria:
                    case "1":
                        categoria= "producto agregado a la categoria carnicos"
                    case "2":
                        categoria= "producto agregado a la categoria lacteos"
                    case "3":
                        categoria= "producto agregado a la categoria grano"
                    case _:
                        categoria="invalido"
                        print("categoria invalida")
                
                while self.categoria=="invalido":
                    if self.categoria=="invalido":
                        self.categoria=categoria.replace()
                        self.categoria=input("ingrse categoria del producto: \n 1.carnicos \n 2.lacteos \n 3.grano \n")
                
                fila.append({"nombre":self.nombre, "precio":self.precio, "categoria": categoria} )
            self.matriz.append(fila)
        return self.matriz
    

print(" INVENTARIO")
dimension=int(input("ingrese el tamaño de la matriz: "))
matriz=Almacen(dimension)
matriz2=matriz.crear()

for x in matriz2:
    print(x)

                    