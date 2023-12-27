# Clase métodos especiales en Python

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"El CD {self.titulo} de {self.autor} tiene {self.canciones} canciones"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha borrado el CD")


mi_cd = CD("The Beatles", "Abbey Road", 17)
print(mi_cd)
print(len(mi_cd))
del mi_cd

