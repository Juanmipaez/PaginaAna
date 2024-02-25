import datetime
Cantidad_de_reservas_a_evaluar = int(input())
Casos_de_entrada = []

for reservas in range(Cantidad_de_reservas_a_evaluar):
    reserva = str(input())
    Casos_de_entrada.append(reserva)

for reservas in Casos_de_entrada:
    Ocupacion_max_diaria = datetime.timedelta(hours=12,minutes=0)
    Duracion_ocupacion = datetime.timedelta(hours=0,minutes=0)
    reservas = reservas.split(" ")
    for index in range(0,(len(reservas)),2):
        Valor_inicio = datetime.timedelta(hours=int(reservas[index].split(":")[0]),minutes=int(reservas[index].split(":")[1]))
        Valor_final = datetime.timedelta(hours=int(reservas[index+1].split(":")[0]),minutes=int(reservas[index+1].split(":")[1]))
        Duracion_unitaria_por_reserva = Valor_final-Valor_inicio
        Duracion_ocupacion+=Duracion_unitaria_por_reserva
    Porcentaje_de_ocupacion = (1-(Duracion_ocupacion.seconds/Ocupacion_max_diaria.seconds))*100
    print(f'Porcentaje de tiempo libre: {round(Porcentaje_de_ocupacion,0)}%')
    