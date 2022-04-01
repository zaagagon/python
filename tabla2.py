
print("cual es tu nombre")
nombre=input()
multiplicador = int(input(f'Cual tabla de multiplica deseas conocer {nombre}?'))
print ("\n esta es la tabla del",multiplicador,)
for j in range(1,6):
    print("%d * %d = %d" % (multiplicador,j,multiplicador*j))