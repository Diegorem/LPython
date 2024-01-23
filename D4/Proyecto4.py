from random import randint

nombre = input("Hola, inserta tu nombre: ")
print(f"Hola {nombre}, vamos a jugar")
numRandom = randint(1, 100)
print(numRandom)
n = 1
inten = 9
while n == 1 and inten > 1:
    try:
        elec = int(input(f"Elige un número del 1 al 100 para adivinar el número, te quedan {inten - 1} intentos\n"))
        if elec > 100 or elec < 1:
            print("No seleccionaste un número entres 1 y 100")
        elif elec == numRandom:
            print(f"¡Has ganado el juego! Te tomó {(inten - 10) * -1} intentos")
            n = 0
        elif elec < numRandom:
            print("No es el número pero el número seleccionado es menor al secreto")
            inten -= 1
        elif elec > numRandom:
            print("No es el número pero el número seleccionado es mayor al secreto")
            inten -= 1
    except:
        print("No has ingresado un número, intenta de nuevo")

print("Gracias por jugar")
