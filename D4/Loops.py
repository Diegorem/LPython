# Clase loops en python
# For
for i in range(10):
    print(i)

letras = ['a','b','c','d','e','f','g','h','i','j']
for i in letras:
    print(i)
lista = [[1,2,3],[4,5,6],[7,8,9]]
for i,j,k in lista:
    print(i,j,k)

# While
i = 0
while i < 10:
    print(i)
    i += 1

# Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# Continue
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

