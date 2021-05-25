#Tablas de multiplicar con for
#tabla del 8

#print("el mundo de zag en python")
print("hola, cual es tu nombre")
nombre=input()
print(f'Bienvenido  {nombre}')
#tambien podemos hacer lo siguiente
#tabla =8
print int(f'Que tabla de multiplicar  deseas {nombre}?')
tabla=input()

#usamos la variable 8 dentro del print
print(f'TABLA DEL {tabla} CON FOR Y RANGE')
for f in range(1,11):
	multiplicacion = tabla * f #operacion
	print(f'{tabla} x {f} = {multiplicacion}') #Resultado de operacion