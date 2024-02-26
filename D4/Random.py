from random import *

# Entero aleatorio
randInt = randint(1,50)
print(randInt)
# Float aleatorio
randUniform = round(uniform(1,5),1)
print(randUniform)
# Random para un número entre 0 y 1
random = random()
print(random)
# Choice para elegir 1 en un array
colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)
# Shuffle para listas
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)