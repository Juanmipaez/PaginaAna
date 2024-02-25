lista_valores_ingresados = []

def ackerman(m, n):
    # Verificamos si ya hemos calculado este valor previamente
    for pair in lista_valores_ingresados:
        if pair[0] == m and pair[1] == n:
            return pair[2]

    # Casos base
    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ackerman(m - 1, 1)
    elif m > 0 and n > 0:
        result = ackerman(m - 1, ackerman(m, n - 1))
    
    lista_valores_ingresados.append((m, n, result))
    return result

Casos_a_probar = int(input())
Valores_a_evaluar = []

for i in range(Casos_a_probar):
    Valor_m = int(input())
    Valor_n = int(input())
    Valores_a_evaluar.append(Valor_m)
    Valores_a_evaluar.append(Valor_n)

for valor in range(0, len(Valores_a_evaluar), 2):
    print(ackerman(Valores_a_evaluar[valor], Valores_a_evaluar[valor + 1]))
