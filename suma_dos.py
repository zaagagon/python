def sumar_dos_numeros():
    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Calcular la suma
    suma = num1 + num2

    # Devolver el resultado
    return suma

# Llamar a la función y almacenar el resultado en una variable
resultado_suma = sumar_dos_numeros()

# Imprimir el resultado
print("La suma de los dos números es:", resultado_suma)
