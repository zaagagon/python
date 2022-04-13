frutas = {1.35:"platano", 0.8:'Manzana',0.85:'Pera', 0.7:'Naranja'}
precios = {8000:"bandeja paisa", 4500:"Desayuno paisa", 5500:"Ajiaco"}

accion = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if accion in frutas:
    print(kg, 'kilos de', accion, 'valen', frutas[accion]*kg, '$')
else: 
    print("Lo siento, la fruta",accion, "no está disponible.")