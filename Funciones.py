#En esta linea, se define la funcion
def saludar():
    print('Hola Desde Una Funcion')

#En esta linea, se define la funcion
def mis_datos(nombre):
    print(f'Hola, {nombre} desde la funcion mis_datos')

#En esta linea, se define la funcion
def mi_operacion(num1, num2):
    return num1 + num2

#Paso de parametros
a = int(input(' ¿Numero Uno? '))
b = int(input(' ¿Numero Dos? '))
#Casting de datos

suma = mi_operacion(a,b)
print(suma)