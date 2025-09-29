import pandas as pd

def mensaje():
    print("hola ++ ")
    
mensaje()


lista=[3,4,5,6,3,2,7,8,6,7,7,7]

promedio= pd.Series(lista)
print(promedio)
#promedio con pandas
promedio2= pd.Series(lista).mean()
print("Valor promedio con pandas : ", promedio2)

print("tamaño lista ", len(lista))
serie=pd.Series(lista)

print("promedio con serie", serie.mean())
print("mediana con serie", serie.median())
print("moda con serie", serie.mode())