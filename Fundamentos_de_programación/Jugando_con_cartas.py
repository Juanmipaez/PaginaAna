Casos_de_mazos = []
while True:
    Tamaño_del_mazo = int(input())
    if Tamaño_del_mazo == 0:
        break
    Casos_de_mazos.append(Tamaño_del_mazo)


def eliminar_mazo(x):
    posiciones = []
    Numeros_eliminados = []
    for numeros in range(1,x+1):
        posiciones.append(numeros)
    num_inicial = 0
    for casos in range(len(posiciones)):
        while len(posiciones) >=2:
            Numeros_eliminados.append(posiciones[num_inicial])
            posiciones.append(posiciones[num_inicial+1])
            del(posiciones[num_inicial])
            del(posiciones[num_inicial])
    for num in range(len(Numeros_eliminados)-1):
        print(Numeros_eliminados[num],end=", ")
    print(Numeros_eliminados[-1])
    print(*posiciones)

for num in Casos_de_mazos:
    eliminar_mazo(num)