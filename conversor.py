menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos argentinos a Dolar Blue

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 200
    dolares = pesos / valor_dolar
    #dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 214
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares blue")
else:
    print('Ingresa una opcion correcta por favor')

