# Función para ver los arreglos creados y sus elementos
def ver_arreglos(arreglos):
    if not arreglos:
        print("No se han creado arreglos.")
    else:
        print("Arreglos creados:")
        for nombre, arreglo in arreglos.items():
            print(f"Nombre: {nombre}, Arreglo: {arreglo}")

# Función para crear un nuevo arreglo
def crear_arreglo(arreglos):
    nombre = input("Ingrese el nombre del arreglo: ")
    nuevo_arreglo = []
    arreglos[nombre] = nuevo_arreglo
    print(f"Se ha creado un nuevo arreglo con el nombre '{nombre}'.")

# Función para agregar un elemento al arreglo
def agregar_elemento(arreglo):
    elemento = input("Ingrese un elemento para agregar al arreglo: ")
    arreglo.append(elemento)
    print(f"'{elemento}' ha sido agregado al arreglo.")

# Función para eliminar un elemento del arreglo
def eliminar_elemento(arreglo):
    if len(arreglo) == 0:
        print("El arreglo está vacío. No hay elementos para eliminar.")
        return

    print("Elementos en el arreglo:")
    for i, elemento in enumerate(arreglo):
        print(f"{i + 1}. {elemento}")

    indice = int(input("Ingrese el número del elemento que desea eliminar: "))
    if indice >= 1 and indice <= len(arreglo):
        elemento_eliminado = arreglo.pop(indice - 1)
        print(f"'{elemento_eliminado}' ha sido eliminado del arreglo.")
    else:
        print("Número de elemento no válido.")

# Función para cambiar un elemento del arreglo
def cambiar_elemento(arreglo):
    if len(arreglo) == 0:
        print("El arreglo está vacío. No hay elementos para cambiar.")
        return

    print("Elementos en el arreglo:")
    for i, elemento in enumerate(arreglo):
        print(f"{i + 1}. {elemento}")

    indice = int(input("Ingrese el número del elemento que desea cambiar: "))
    if indice >= 1 and indice <= len(arreglo):
        nuevo_elemento = input(f"Ingrese el nuevo valor para el elemento {indice}: ")
        arreglo[indice - 1] = nuevo_elemento
        print(f"Elemento {indice} ha sido cambiado a '{nuevo_elemento}'.")
    else:
        print("Número de elemento no válido.")

# Función para guardar los arreglos en un archivo
def guardar_arreglos(arreglos):
    with open("arreglos.txt", "w") as archivo:
        for nombre, arreglo in arreglos.items():
            archivo.write(f"{nombre}: {arreglo}\n")
    print("Arreglos guardados en 'arreglos.txt'.")

# Diccionario para almacenar los arreglos con sus nombres
arreglos = {}

while True:
    print("\nMenú:")
    print("1. Crear un nuevo arreglo")
    print("2. Agregar elemento")
    print("3. Eliminar elemento")
    print("4. Cambiar elemento")
    print("5. Ver arreglos creados y sus elementos")
    print("6. Guardar arreglos en archivo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_arreglo(arreglos)
    elif opcion == "2":
        nombre_arreglo = input("Ingrese el nombre del arreglo: ")
        if nombre_arreglo in arreglos:
            agregar_elemento(arreglos[nombre_arreglo])
        else:
            print(f"No se encontró un arreglo con el nombre '{nombre_arreglo}'.")
    elif opcion == "3":
        nombre_arreglo = input("Ingrese el nombre del arreglo: ")
        if nombre_arreglo in arreglos:
            eliminar_elemento(arreglos[nombre_arreglo])
        else:
            print(f"No se encontró un arreglo con el nombre '{nombre_arreglo}'.")
    elif opcion == "4":
        nombre_arreglo = input("Ingrese el nombre del arreglo: ")
        if nombre_arreglo in arreglos:
            cambiar_elemento(arreglos[nombre_arreglo])
        else:
            print(f"No se encontró un arreglo con el nombre '{nombre_arreglo}'.")
    elif opcion == "5":
        ver_arreglos(arreglos)
    elif opcion == "6":
        guardar_arreglos(arreglos)
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
