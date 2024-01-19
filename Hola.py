#Este es un comntario
print('variables en Python')

#Capturar Datos Por Teclado
nombre = input('Ingrese Su Nombre ')
apellido = input('Ingrese Su Apellido ')
edad = input('Ingrese Su Edad ')

# print('nombre', nombre)
# print('apellidos', apellido)
# print('edad', edad)

# nombre_completo = nombre +' '+ apellido
# print('nombre completo:',nombre_completo)

nombre_completo = f'{nombre} {apellido}'

print(f'nombre_completo: {nombre_completo} \n Edad: {edad}')

