Numero_de_casos = int(input())
Palabras = []

def transformar_palabra(x):
    lista_x = x.split("_")
    Palabra_cambiada = lista_x[0]
    for index in range(1,len(lista_x)):
        lista_x[index] = lista_x[index].capitalize()
        Palabra_cambiada += lista_x[index]
    return Palabra_cambiada

for caso in range(Numero_de_casos):
    palabra = str(input())
    Palabras.append(palabra)

for palabra_2 in Palabras:
    print(transformar_palabra(palabra_2))