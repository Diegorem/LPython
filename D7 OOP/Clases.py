# Clases en python

class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def volar(self,metros):
        print(f"El pájaro voló {metros} metros")
    def piar(self):
        print(f"El pájaro {self.especie} esta piando")

    def pintar_negro(self):
        self.color = "Negro"
        print(f"El {self.especie} ahora es {self.color}")

    @classmethod # Los métodos de clase no necesitan una instancia para ejecutarse
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pájaro mira")



tucan = Pajaro("Amarillo", "Tucan")
tucan.volar(20)
print(tucan.color)
tucan.piar()
tucan.pintar_negro()
print(tucan.color)
Pajaro.poner_huevos(4)
Pajaro.mirar()


