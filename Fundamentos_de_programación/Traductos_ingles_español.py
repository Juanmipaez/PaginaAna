Cantidad_de_palabras = int(input())
Traducciones = {}

for productos in range(Cantidad_de_palabras):
    Traducciones_individuales = str(input())
    Traducciones_individuales_lista = Traducciones_individuales.split(":")
    Traducciones[Traducciones_individuales_lista[0]]= Traducciones_individuales_lista[1]

Cantidad_de_palabras_a_traducir = int(input())

Traduccion_por_fila = []
for No_traducciones in range(Cantidad_de_palabras_a_traducir):
    Frase = str(input())
    Traduccion_por_fila.append(Frase.split(" "))

for frases in Traduccion_por_fila:
    for index in range(len(frases)-1):
        print(Traducciones[frases[index]],end=" ")
    print(Traducciones[frases[-1]])

