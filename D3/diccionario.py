# Clase diccionario en Python
diccionario = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python','Django','JavaScript']}
print(type(diccionario))
print(diccionario)

# Acceder a los elementos de un diccionario
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])

# Modificar los valores de un diccionario
diccionario['nombre'] = 'Juan'
print(diccionario['nombre'])

# Recorrer los elementos de un diccionario
for key in diccionario:
    print(key, ":", diccionario[key])

letras = {'a1': ['a','b','c'], 'a2': ['d','e','f'], 'a3': ['g','h','i']}
mayus = letras['a2'][1].upper()
print(mayus)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#Actualizar un diccionario
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic 
