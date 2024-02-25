cantidad_numeros = int(input())
numeros = []
for iteraciones in range(cantidad_numeros):
    numero_a_evaluar = int(input())
    numeros.append(numero_a_evaluar)


def funcionTramos(x):
    if x >= 2:
        valor_evaluado = x + 3
        return(valor_evaluado)
    else:
        valor_evaluado = ((x**2)-(7*x) + 5)
        return(valor_evaluado)

for numero in numeros:
    print(funcionTramos(numero))

