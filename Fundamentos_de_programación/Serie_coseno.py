import math
Terminos_a_generar = int(input())
Termino_a_evaluar = float(input())
Valores_evaluados = [1]

suma = 1
for num in range(1,Terminos_a_generar):
    valor = (((-1)**num)*(Termino_a_evaluar**(2*num)))/math.factorial(2*num)
    suma += valor
    valorRedondeado = round(valor,2)
    Valores_evaluados.append(valorRedondeado)

for index in range(len(Valores_evaluados)-1):
    print(Valores_evaluados[index],end=", ")
print(Valores_evaluados[-1])

print(round(suma,2))
