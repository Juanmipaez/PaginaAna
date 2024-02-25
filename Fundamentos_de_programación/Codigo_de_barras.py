Codigos_de_barra = []
while True:
    numero_del_codigo = int(input())
    if numero_del_codigo == -1:
        break
    Codigos_de_barra.append(numero_del_codigo)

for codigo in Codigos_de_barra:
    posiciones_pares = []
    posiciones_impares = []
    codigo_al_reves = str(codigo)[::-1]
    for index in range(1,len(codigo_al_reves)):
        if index % 2!=0:
            posiciones_impares.append(int(codigo_al_reves[index])*3)
        else:
            posiciones_pares.append(int(codigo_al_reves[index]))
    suma_total = sum(posiciones_pares) + sum(posiciones_impares)
    if (suma_total + int(codigo_al_reves[0])) % 10 == 0:
        print("CORRECTO")
    else:
        print("INCORRECTO")