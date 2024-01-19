#Definir Clase

class Galleta:
    #Constructor
    def __init__(self, nombre, sabor, color) -> None:
        self.nombre = nombre
        self.sabor = sabor
        self.color = color
    #Metodo
    def imprimir(self):
        datos = f"""
        Nombre: {self.nombre}
        Sabor: {self.sabor}
        Color: {self.color}
        """
        print(datos)
    
    def __str__(self) -> str:
        return f'Galleta({self.nombre}, {self.sabor}, {self.color})'

#Objetos
galleta1 = Galleta('Oreo', 'Dulce', 'Negro')
galleta2 = Galleta('Ritz', 'Salado', 'Dorado')

#Modificar un atributo de objeto
galleta2.color = 'Naranjado'

print(galleta1.nombre)
galleta1.imprimir()
galleta2.imprimir()

#Herencia
class Gaseosa(Galleta):
    def __str__(self) -> str:
         return f'Gaseosa({self.nombre}, {self.sabor}, {self.color})'
#Objeto
gaseosa1 = Gaseosa('Coca Cola', 'Cero', 'Negro')
#Datos 
gaseosa1.imprimir()
#
print(gaseosa1)