# Clase operadores lógicos

# Operador and
num1 = 10
num2 = 20

if num1 > 0 and num2 > 0:
    print("Los dos numeros son positivos")

# Operador or
if num1 > 0 or num2 > 0:
    print("Al menos uno de los numeros es positivo")

# Operador not
if not(num1 > 0 and num2 > 0):
    print("Los dos numeros no son positivos")

# Operador in
if "a" in "hola":
    print("La letra a esta en hola")