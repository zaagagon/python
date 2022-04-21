#PROGRAMA QUE SUMA DOS NUMEROS EN PYTHON3

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

print(" ** Programa que suma dos numeros **" + '\n')

n1 = float(input("Digite número uno: "))
n2 = float(input("Digite numero dos: "))
suma = n1+n2
print("Resultado de la suma es: ", suma)

print(" ** fin del programa**" + '\n')


