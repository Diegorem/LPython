def suma(*args):
    return sum(args)


def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg ** 2
    return total


def suma_absolutos(*args):
    total = 0
    for arg in args:
        total += abs(arg)
    return total


def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus números es {sum(args)}"


print(suma(4,5,7,5))
print(suma_cuadrados(4,5,7,5))
print(suma_absolutos(4,5,-7,-5))
print(numeros_persona("Juan",4,6,8,5,4))