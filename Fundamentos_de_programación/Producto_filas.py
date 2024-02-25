Numero_filas = int(input())
Numero_columnas = int(input())
Matriz_tabla = []

for filas in range(Numero_filas):
    Fila_individual = []
    for fila in range(Numero_columnas):
        Valor = int(input())
        Fila_individual.append(Valor)
    Matriz_tabla.append(Fila_individual)

def multiplicacion_fila(x):
    resultado = 1
    for i in x:
        resultado *= i
    return resultado

filas_valores = {}

index=0
for fila in Matriz_tabla:
    filas_valores[index] = multiplicacion_fila(fila)
    index+=1


Multiplicaciones_por_fila = []
for keys in filas_valores:
    Multiplicaciones_por_fila.append(filas_valores[keys])
Mayor_valor = max(Multiplicaciones_por_fila)
Menor_valor = min(Multiplicaciones_por_fila)

for keys in filas_valores:
    if filas_valores[keys] == Mayor_valor:
        print(keys)
    if filas_valores[keys] == Menor_valor:
        print(keys)