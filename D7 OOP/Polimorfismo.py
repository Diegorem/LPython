# Clase polimorfismo en python

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice Muuu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice Beee')


vaca1 = Vaca('Juana')
oveja1 = Oveja('Dolly')


def animal_hablar(animal):
    animal.hablar()


animal_hablar(vaca1)
animal_hablar(oveja1)