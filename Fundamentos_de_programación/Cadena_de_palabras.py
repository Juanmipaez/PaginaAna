file = open("C:/Users/Juanm/.vscode/Code/Fundamentos_de_programación/palabras.txt","r")

Resultados_por_linea = []
def analizar_linea(x):
    contador = 0
    for index in range(len(x)-1):
        terminacion1= (x[index])[-3:] 
        terminacion2= (x[index])[-2:]
        if x[index+1].startswith(terminacion1) :
            contador+=1
        elif x[index+1].startswith(terminacion2):
            contador+=1
    if contador == len(x)-1:
        return "Cadena completa"
    else:
        return "Cadena rota"
    
for linea in file:
    lineaLista = linea.split(" ")
    print(analizar_linea(lineaLista))
