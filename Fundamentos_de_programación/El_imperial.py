Ventas = []
Ventas_por_semana = []
Organizacion_por_semana =[]

def dia_maximo ():
    if Ventas_por_semana.index(maximo) == 0:
        print("MARTES",end=" ")
    elif Ventas_por_semana.index(maximo) == 1:
        print("MIERCOLES",end=" ")
    elif Ventas_por_semana.index(maximo) == 2:
        print("JUEVES",end=" ")
    elif Ventas_por_semana.index(maximo) == 3:
        print("VIERNES",end=" ")
    elif Ventas_por_semana.index(maximo) == 4:
        print("SABADO",end=" ")
    elif Ventas_por_semana.index(maximo) == 5:
        print("DOMINGO",end=" ")

def dia_minimo ():
    if Ventas_por_semana.index(minimo) == 0:
        print("MARTES",end=" ")
    elif Ventas_por_semana.index(minimo) == 1:
        print("MIERCOLES",end=" ")
    elif Ventas_por_semana.index(minimo) == 2:
        print("JUEVES",end=" ")
    elif Ventas_por_semana.index(minimo) == 3:
        print("VIERNES",end=" ")
    elif Ventas_por_semana.index(minimo) == 4:
        print("SABADO",end=" ")
    elif Ventas_por_semana.index(minimo) == 5:
        print("DOMINGO",end=" ")

while True:
    Venta_diaria = float(input())
    if Venta_diaria == -1:
        break
    Ventas.append(Venta_diaria)

index = 0
numero_semanas = int(len(Ventas)/6)
for semanas in range(numero_semanas):
    for venta in range(len(Ventas)):
        if len(Ventas_por_semana)>=6:
            break
        Ventas_por_semana.append(Ventas[index])
        index+=1
    maximo = max(Ventas_por_semana)
    minimo = min(Ventas_por_semana)
    if maximo == minimo:
        print("EMPATE",end=" ")
    else:
        dia_maximo()
        dia_minimo()
    promedio = sum(Ventas_por_semana)/6
    if Ventas_por_semana[-1] > promedio:
        print("SI")
    else:
        print("NO")
    Ventas_por_semana.clear()