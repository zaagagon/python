#
class Sumador:
    def __init__(self):
        # Inicializar los números en 0
        self.num1 = 0
        self.num2 = 0

    def ingresar_numeros(self):
        # Solicitar al usuario que ingrese dos números
        self.num1 = float(input("Ingresa el primer número: "))
        self.num2 = float(input("Ingresa el segundo número: "))

    def sumar(self):
        # Calcular la suma
        suma = self.num1 + self.num2
        return suma

# Crear una instancia de la clase Sumador
mi_sumador = Sumador()

# Llamar a los métodos para ingresar números y realizar la suma
mi_sumador.ingresar_numeros()
resultado_suma = mi_sumador.sumar()

# Imprimir el resultado
print("La suma de los dos números es:", resultado_suma)
