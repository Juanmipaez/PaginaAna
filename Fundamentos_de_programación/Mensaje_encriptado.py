file = open("C:/Users/Juanm/.vscode/Code/Fundamentos_de_programación/mensaje.txt","r")

def cambiar_lista(x):
    lista_cambiada = []
    for index in range(-1,-len(x)-1,-1):
        palabra_al_reves = x[index]
        palabra_al_reves=palabra_al_reves[::-1]
        lista_cambiada.append(palabra_al_reves)
    print(*lista_cambiada)

for linea in file:
    linea_en_lista = linea.split()
    cambiar_lista(linea_en_lista)