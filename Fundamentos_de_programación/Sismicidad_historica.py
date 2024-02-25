import datetime
Numero_de_registros_a_evaluar = int(input())

Casos_de_registros = []

for registro_sismico in range(Numero_de_registros_a_evaluar):
    registro_sismico = str(input())
    Casos_de_registros.append(registro_sismico)

Suma_total = 0
for index in range(1,len(Casos_de_registros)):
    Tiempo_inicial = datetime.datetime.strptime(Casos_de_registros[index-1], "%Y/%m/%d %H:%M")
    Tiempo_final = datetime.datetime.strptime(Casos_de_registros[index], "%Y/%m/%d %H:%M")
    Tiempo_entre_evento = Tiempo_final-Tiempo_inicial
    Suma_total += int(Tiempo_entre_evento.total_seconds())
    print(f'{Tiempo_entre_evento.days} dias, {Tiempo_entre_evento.seconds//3600} horas, {(Tiempo_entre_evento.seconds%3600)//60} minutos')

Promedio = Suma_total/(Numero_de_registros_a_evaluar-1)
print(f'Promedio: {int((Promedio)//86400)} dias, {int((Promedio%86400)//3600)} horas, {int(((Promedio%86400)%3600)//60)} minutos ')

