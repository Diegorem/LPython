texto = input("Inserte un texto: ")
texto = texto.lower()
letras = []
for i in range(0, 3):
    letras.append(input("inserte una letra: "))
    letras[i] = letras[i].lower()
print(f"La letra {letras[0]} se repite {texto.count(letras[0])} veces \nLa letra {letras[1]} se repite {texto.count(letras[1])} veces \nLa letra {letras[2]} se repite {texto.count(letras[2])} veces")

palabras = texto.split(" ")
print(f"El total de palabras en el texto es de {len(palabras)}")
print(f"La primera letra del texto es {texto[0]} y la ultima letra es {texto[-1]} ")
print(f"La oración con palabras en orden inverso es: ")
palabras.reverse()
texto_inverso = " ".join(palabras)
print(texto_inverso)
real = "python" in palabras
print(f"¿Aparece python en el texto? {real}")
