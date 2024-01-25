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

resultado = chec_3_cifras(625)
print(resultado)

res = chec_3_cifras_lis([55,54,522])
print(res)

ress = reg_3_cif([545,5,633])
print(ress)

