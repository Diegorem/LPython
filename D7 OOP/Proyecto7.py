class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Empleado(Persona):
    def __init__(self, nombre, apellido, numero_empleado, balance):
        super().__init__(nombre, apellido)
        self.numero_empleado = numero_empleado
        self.balance = balance

    def __str__(self):
        return f'{self.nombre} {self.apellido} tiene un balance de {self.balance}'

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance -= cantidad


print("Bienvenido al sistema de empleados")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
numero_empleado = input("Ingrese su numero de empleado: ")
balance = float(input("Ingrese su balance: "))
empleado = Empleado(nombre, apellido, numero_empleado, balance)

# menu
band = 1
while band == 1:
    print("\nMenu")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar balance")
    print("4. Salir")
    # Un try en caso de que el usuario ingrese un string
    try:
        opcion = int(input('Ingrese una opción: '))
    except:
        opcion = 0
    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        empleado.depositar(cantidad)
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > empleado.balance:
            print("No puede retirar más de lo que tiene")
        else:
            empleado.retirar(cantidad)
    elif opcion == 3:
        print(empleado)
    elif opcion == 4:
        band = 0
    else:
        print("Opción incorrecta")

print("Gracias por usar el sistema")