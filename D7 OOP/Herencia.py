# Clase Herencia en Python
class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Naciendo")

    def hablar(self):
        print("Hablando")


class Pajaro(Animal):
    def __init__(self,edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio pio")
    def volar(self,metros):
        print(f"Volando {metros} metros")


piolin = Pajaro(2,"amarillo", 60)
mi_animal = Animal(5,"verde")
piolin.hablar()
piolin.volar(10)