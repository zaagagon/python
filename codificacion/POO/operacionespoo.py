class Calculadora:
    def __init__(self):
        self.numero1 = float(input("Ingrese el primer número: "))
        self.numero2 = float(input("Ingrese el segundo número: "))

    def suma(self):
        return self.numero1 + self.numero2

    def resta(self):
        return self.numero1 - self.numero2

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "No se puede dividir por cero."

# Ejemplo de uso
calculadora = Calculadora()

print("Suma:", calculadora.suma())
print("Resta:", calculadora.resta())
print("Multiplicación:", calculadora.multiplicacion())
print("División:", calculadora.division())
