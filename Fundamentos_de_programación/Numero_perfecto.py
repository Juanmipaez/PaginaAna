# Cantidad_de_numeros = int(input())
# Numeros_a_evaluar = []

# def numeroPerfecto(x):
#     Divisores = []
#     for divisor in range(1,x):
#         if (x%divisor == 0):
#             Divisores.append(divisor)
#     if x == sum(Divisores):
#         return True
#     else:
#         return False

# for numeros in range(Cantidad_de_numeros):
#     numero_a_evaluar = int(input())
#     Numeros_a_evaluar.append(numero_a_evaluar)

# for numero in Numeros_a_evaluar:
#     if numeroPerfecto(numero) == True:
#         print("El numero1",numero,"es perfecto")
#     elif numero <= 0:
#         print("El numero ingresado debe ser positivo")
#     else:
#         print("El numero",numero,"no es perfecto")


memo = []

def ackerman(m, n):
    # Verificamos si ya hemos calculado este valor previamente
    for pair in memo:
        if pair[0] == m and pair[1] == n:
            return pair[2]
    
    # Casos base
    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ackerman(m - 1, 1)
    elif m > 0 and n > 0:
        result = ackerman(m - 1, ackerman(m, n - 1))
    
    # Almacenamos el resultado en el diccionario
    memo.append((m, n, result))
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

print(memo)

