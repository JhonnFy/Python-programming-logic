#Definir Lista
colores = ['Rojo', 'Verde', 'Gris']

#Modificando un elemento
colores[2] = 'Blanco'
print(colores[1])

#Agregando elementos a un arreglo
colores.append('Azul')
colores.append('Amarillo')

#Eliminar el ultimo elemento
colores.pop()

#Eliminar un elemento
colores.remove('Rojo')

#Invertir
colores.reverse()

#Convertimos a tuplas(), no se puede modificar un elemento
colores=tuple(colores)

print(colores[0])
print(len(colores))





