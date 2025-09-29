import pandas as pd

def mensaje():
    print("hola ++ ")
    
mensaje()


lista=[3,4,5,6,3,2]

promedio= pd.Series(lista)
print(promedio)
#promedio con pandas
promedio2= pd.Series(lista).mean()
print(promedio2)