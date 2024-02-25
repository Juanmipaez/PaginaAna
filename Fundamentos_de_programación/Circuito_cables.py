Numero_de_casos = int(input())
Lista_combinaciones = []

def circuito(x):
    lista_abierta = x.split(" ")
    M_iniciales = 0
    M_finales = 0
    F_iniciales = 0
    F_finales = 0

    for parejas in lista_abierta:
        if parejas[0]=="M":
            M_iniciales += 1
        elif parejas[0] == "F":
            F_iniciales+=1

        if parejas[1] == "M":
            M_finales+=1
        elif parejas[1] == "F":
            F_finales+=1
    
    if (M_iniciales==F_finales) and (F_iniciales == M_finales):
        Lista_combinaciones.append("Circulo de cables")
    elif (M_iniciales!=F_finales) and (F_iniciales != M_finales):
        Lista_combinaciones.append("Circulo imposible")


for casos in range(Numero_de_casos):
    Combinacion_cables = input()
    circuito(Combinacion_cables)

for resultado in Lista_combinaciones:
    print(resultado)
