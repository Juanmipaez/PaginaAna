Numero_de_palabras = int(input())
Vocales = ["a","e","i","o","u"]
Palabras = []

def clasificacion_palabra(x):
    contador = 0
    for vocal in Vocales:
        if vocal in x:
            contador+=1
    if contador == 5:
        return "Panvocalica"
    else:
        return "No panvocalica"

for casos in range(Numero_de_palabras):
    Palabra = str(input())
    Palabras.append(Palabra)

for palabra in Palabras:
    print(clasificacion_palabra(palabra))