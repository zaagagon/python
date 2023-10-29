# Función para ver arreglos desde un archivo
def ver_arreglos():
    try:
        with open("arreglos.txt", "r") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No se encontraron arreglos en el archivo.")
                return

            print("Arreglos encontrados en el archivo:")
            for linea in lineas:
                print(linea.strip())  # Elimina caracteres de nueva línea

    except FileNotFoundError:
        print("El archivo 'arreglos.txt' no existe.")

# Función para agregar elementos a un arreglo en el archivo
def agregar_elementos():
    nombre_arreglo = input("Ingrese el nombre del arreglo al que desea agregar elementos: ")
    elemento = input("Ingrese el elemento que desea agregar: ")

    try:
        with open("arreglos.txt", "r") as archivo:
            lineas = archivo.readlines()
            nuevo_contenido = []

            encontrado = False

            for linea in lineas:
                if nombre_arreglo in linea:
                    nuevo_contenido.append(linea.strip() + ", " + elemento)
                    encontrado = True
                else:
                    nuevo_contenido.append(linea)

            if not encontrado:
                nuevo_contenido.append(f"{nombre_arreglo}: {elemento}")

        with open("arreglos.txt", "w") as archivo:
            archivo.writelines(nuevo_contenido)

        print(f"'{elemento}' ha sido agregado al arreglo '{nombre_arreglo}'.")

    except FileNotFoundError:
        print("El archivo 'arreglos.txt' no existe.")

# Menú principal
while True:
    print("\nMenú:")
    print("1. Ver arreglos en archivo")
    print("2. Agregar elementos a un arreglo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_arreglos()
    elif opcion == "2":
        agregar_elementos()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
