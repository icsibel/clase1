class Ventas:
    matriz=[]
    dimension=0
    tipo_comida=""
    cantidad=0
    tamano=0
    precio=0

    def __init__(self,dimension):
        self.dimension=dimension
        

    def crear(self):
        for i in range(self.dimension):
            filas=[]
            for j in range(self.dimension):

                self.tipo_comida=input("ingrese el tipo de comida: \n 1. hamburguesita \n 2.perro \n 3.papas \n")
                match self.tipo_comida:
                    case "1":
                        tipo_comida="hamburgesita"
                    case "2":
                        tipo_comida="perro"
                    case "3":
                        tipo_comida="papas"
                    case _:
                        print("no hay ese tipo de comida")
                
                self.tamano=input("ingrese el tamaño: \n 1. grande \n 2.mediano \n 3.pequeña \n ")
                match self.tamano:
                    case "1":
                        tamano="grande"
                    case "2":
                        tamano="mediano"
                    case "3":
                        tamano="pequeño"
                    case _:
                        print("no hay ese tamano")

                self.cantidad=int(input("ingrese la cantidad: "))
                self.precio = int(input("ingrese el precio: "))
                filas.append({"tipo_comida":tipo_comida, "tamano":tamano, "cantidad": self.cantidad, "precio":self.precio} ) 

            self.matriz.append(filas)

    
    def total_ventas(self):
        totales={}
        for i in self.matriz:
            for venta in i:
                if venta:
                    tipo= venta["tipo_comida"]
                    total= venta["cantidad"] * venta["precio"]
                    totales[tipo]=totales.get(tipo, 0) + total
        
        print(" TOTAL VENTAS")
        for tipo, total in totales.items():
            print(f"{tipo} :{total}")


dimension=int(input("ingrese el tamaño de la matriz: "))
ventas=Ventas(dimension)
ventas.crear()
ventas.total_ventas()


        
        
    




