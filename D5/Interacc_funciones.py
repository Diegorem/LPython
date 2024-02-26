from random import shuffle
# Lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

# Comprobar intento
def compr_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Perdiste :( ")
    else:
        print("Te salvaste")

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
compr_intento(palitos_mezclados, seleccion)

# 2do ejemplo

def reducir_lista(lista):
    lista = sorted(list(set(lista)))
    lista.pop()
    return lista

def promedio(lista):
    return sum(lista) / len(lista)

lista_numeros = [1,4,2,6,3,4,45]
print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))