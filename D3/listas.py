# Clase Listas en Python

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

# Acceder a un elemento de la lista
print(lista[0])

# Acceder a un elemento de la lista de forma inversa
print(lista[-1])

# Acceder a un rango de elementos
print(lista[0:3]) # Sin incluir el 3

# Acceder a un rango de elementos sin indicar el inicio
print(lista[:3]) # Sin incluir el 3

# Acceder a un rango de elementos sin indicar el final
print(lista[3:]) # Incluye el 3

# Cambiar el valor de un elemento de la lista
lista[0] = 10
print(lista)

# Recorrer elementos de una lista
for elemento in lista:
    print(elemento)
