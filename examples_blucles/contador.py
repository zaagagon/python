def mostrar(lista):
    for elemento in lista:
        print(elemento)

def hola(nombre):
    print(f"hola {nombre}")

lista = [2, 8, 4, 7, 2]
contador = 0
#insertar elemento 
lista.insert(1, 2)
hola("marcos")
mostrar(lista)

  #muestra las iteraciones de la lista
for lista in lista:
   if lista == 2:
       contador += 1

print("Cantidad de 2:", contador)

