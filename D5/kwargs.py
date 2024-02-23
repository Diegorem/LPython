# Clase **kwargs

def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")


    for key, valor in kwargs.items():
        print(f'{key} = {valor}')

args = [5,43,23,13,65,44]
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

prueba(12, 34, *args, **kwargs)
