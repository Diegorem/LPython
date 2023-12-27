# Clase zip en python

nombres = ['Juan', 'Pedro', 'Maria', 'Luis']
edades = [18, 20, 19, 21]
ciudades = ['Monterrey', 'Guadalajara', 'CDMX', 'Puebla']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")