import pandas as pd

def mensaje():
    print("hola ++ ")
    
mensaje()


lista=[3,4,5,6,3,2]

promedio= pd.Series(lista)
promedio2= pd.Series(lista).mean()
print(promedio)
promedio.serie.mean(lista)
print(promedio2)