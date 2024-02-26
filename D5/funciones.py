def chec_3_cifras(numero):
    return numero in range(100,1000)

def chec_3_cifras_lis(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

def reg_3_cif(lista):
    lista_3_cif = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cif.append(n)
        else:
            pass
    return lista_3_cif

precios_cafe = [('capuccino', 1.5), ('Expresso', 3.2), ('Moka', 2.5)]

def cafe_mas_caro(lista):
    precio_may = 0
    cafe_mas_car = ""
    for cafe, precio in lista:
        if precio > precio_may:
            precio_may = precio
            cafe_mas_car = cafe
        else:
            pass
    return cafe_mas_car, precio_may

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es {cafe} cuyo precio {precio}")

resultado = chec_3_cifras(625)
print(resultado)

res = chec_3_cifras_lis([55,54,522])
print(res)

ress = reg_3_cif([545,5,633])
print(ress)

