# Clase sets en Python
set1 = set([1,2,3,4,5])
set2 = {1,2,3,4,5}
print(set1)
print(set2)

# Agregar elementos a un set
set1.add(6)
print(set1)

# Eliminar elementos de un set
set1.remove(6)
print(set1)

# Operaciones con sets
set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8}
print(set3 | set4) # Union
print(set3 & set4) # Interseccion
print(set3 - set4) # Diferencia
print(set3 ^ set4) # Diferencia simetrica

