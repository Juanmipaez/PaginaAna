Tamaño_de_matriz = int(input())
Matriz_en_tablas = []

for filas in range(Tamaño_de_matriz):
    Lista_por_fila = []
    elemento_por_fila = input()
    lista = elemento_por_fila.split()
    Matriz_en_tablas.append(lista)

contador_diferentes_diagonal = 0
contador_de_diagonal = 0
for fila in range(Tamaño_de_matriz):
    for columna in range(Tamaño_de_matriz):
        if fila==columna:
            if Matriz_en_tablas[fila][columna] == "0":
                contador_de_diagonal+=1

for fila in range(-1,-(Tamaño_de_matriz+1),-1):
    for columna in range(-1,-(Tamaño_de_matriz+1),-1):
        if fila==columna:
            if Matriz_en_tablas[fila][columna] == "0":
                contador_de_diagonal+=1

for fila in range(Tamaño_de_matriz):
    for columna in range(Tamaño_de_matriz):
        if fila!=columna:
            if Matriz_en_tablas[fila][columna] == "*":
                contador_diferentes_diagonal+=1
contador_de_diagonal -= 1

if (contador_diferentes_diagonal + contador_de_diagonal) == Tamaño_de_matriz**2:
    print("Si es la bandera de Escocia")
else:
    print("No es la bandera de Escocia")

