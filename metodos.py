class Vehiculo:
    color= ""
    marca= ""
    cilindraje= 0
    
    def __init__(self,color,marca,cilindraje):
        self.color=color
        self.marca=marca
        self.cilindraje=cilindraje
    
    def mostrar_vehiculo(self):
        dicc={ "color": self.color, "marca": self.marca, "cilindraje": self.cilindraje}
        return dicc
    

matriz=[]
tamano=int(input("ingresa tamaño: "))
def llenar_matriz():
    
    for i in range(tamano):
        filas=[]
        for j in range(tamano):
            color=input("ingrese color: ")
            marca=input("ingrese marca: ")
            cilindraje=int(input("ingrese cilindraje: "))
            vehiculo=Vehiculo(color, marca, cilindraje)
            filas.append(vehiculo.mostrar_vehiculo())
        matriz.append(filas)
    return matriz
    
matriz2=llenar_matriz()
for x in matriz2:
    print (x)
    
    
        
    
    
        
    
    
  