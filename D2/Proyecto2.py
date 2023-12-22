nombre = input("¿Cuál es tu nombre? ")
venta = float(input("¿Cuánto vendiste? "))
gano = round(venta * 13 / 100, 2)
print(f"Ganaste ${gano} en total {nombre}")