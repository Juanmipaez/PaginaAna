Tamaño_de_matriz = int(input())
Matriz_en_tablas = []

for filas in range(Tamaño_de_matriz):
    Lista_por_fila = []
    for fila in range(Tamaño_de_matriz):
        elemento_por_fila = int(input())
        Lista_por_fila.append(elemento_por_fila)
    Matriz_en_tablas.append(Lista_por_fila)



def matriz_t_inf(matriz):
    contador_de_ceros = 0
    contador_diferente_de_cero = 0
    index = 1
    for fila in range(Tamaño_de_matriz):
        for columna in range(index,Tamaño_de_matriz):
            if matriz[fila][columna] == 0:
                contador_de_ceros+=1
        for columna in range(0,index):
            if matriz[fila][columna]!=0:
                contador_diferente_de_cero+=1
        index+=1
        
    if (contador_de_ceros + contador_diferente_de_cero) == Tamaño_de_matriz**2:
        print("Triangular inferior")
    elif (contador_de_ceros + contador_diferente_de_cero) != Tamaño_de_matriz**2:
        return False

def matriz_t_sup(matriz):
    contador_de_ceros = 0
    contador_diferente_de_cero = 0
    index = 0
    for fila in range(Tamaño_de_matriz):
        for columna in range(index,Tamaño_de_matriz):
            if matriz[fila][columna] != 0:
                contador_diferente_de_cero+=1
        for columna in range(0,index):
            if matriz[fila][columna]==0:
                contador_de_ceros+=1
        index+=1
    if (contador_de_ceros + contador_diferente_de_cero) == Tamaño_de_matriz**2:
        print("Triangular superior")
    elif (contador_de_ceros + contador_diferente_de_cero) != Tamaño_de_matriz**2:
        return False

Opcion1 = matriz_t_inf(Matriz_en_tablas)
Opcion2 = matriz_t_sup(Matriz_en_tablas)

if Opcion1 == False and Opcion2==False:
    print("No es triangular superior ni inferior")