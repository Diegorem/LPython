# Clase control de flujo en python
num1 = 10
num2 = 20
if num1 > 0 and num2 > 0:
    print("Los dos numeros son positivos")
elif num1 > 0 or num2 > 0:
    print("Al menos uno de los numeros es positivo")
else:
    print("Los dos numeros son negativos")

if not(num1 > 0 and num2 > 0):
    print("Los dos numeros no son positivos")
