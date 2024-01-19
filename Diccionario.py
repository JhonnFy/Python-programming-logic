
#Crear diccionario
datos = {
    'uno':1,
    'dos':2,
    'colores':['Rojo','Negro','Verde']
}

#Agregar elementos
datos['estado'] = True

#Eliminar elemento
del(datos['estado'])

#Tuplas
print(datos.items())
#Imprimir los valores
print(datos.values())
#Imprimir Clabes
print(datos.keys())