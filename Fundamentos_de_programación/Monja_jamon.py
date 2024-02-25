file = open("Fundamentos_de_programación/trifelios.txt","r")

def clasificarTrifelios(lineaEnLista):
    if len(lineaEnLista[0]) == 2:
        if (lineaEnLista[0])[::-1] == lineaEnLista[1]:
            print("Es trifelio")
        else:
            print("No es trifelio")
    else:
        Terminacion1 = (lineaEnLista[0])[-(len(lineaEnLista[0])-1):] + (lineaEnLista[0])[0:-(len(lineaEnLista[0])-1)]
        Terminacion2 = (lineaEnLista[0])[-2:] + (lineaEnLista[0])[0:-2]
        Terminacion3 = (lineaEnLista[0])[-(len(lineaEnLista[0])-2):] + (lineaEnLista[0])[0:-(len(lineaEnLista[0])-2)]
        if Terminacion1 == lineaEnLista[1] or Terminacion2 == lineaEnLista[1] or Terminacion3 == lineaEnLista[1]:
            print("Es trifelio")
        else:
            print("No es trifelio")

for linea in file:
    linea = linea.rstrip()
    lineaEnLista = linea.split("-")
    clasificarTrifelios(lineaEnLista)


