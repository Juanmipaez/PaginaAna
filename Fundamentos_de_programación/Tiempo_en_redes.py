import datetime
casos_a_probar = int(input())
Red_a_analizar = str(input())
Datos_ingreso = []
for casos in range(casos_a_probar):
    fecha_hora = str(input())
    Datos_ingreso.append(fecha_hora)

NumeroDeVecesEnLaRed = 0
Tiempo = datetime.timedelta(hours=0,minutes=0,seconds=0)
for registro in Datos_ingreso:
    red_social = registro.split(".")[1] #Extraer el nombre de la red social en el string
    registro = registro.split(" ")
    if red_social == Red_a_analizar:
        NumeroDeVecesEnLaRed += 1
        tiempo_inicio = datetime.datetime.strptime(registro[1], "%H:%M:%S")
        tiempo_final = datetime.datetime.strptime(registro[2], "%H:%M:%S")
        Total_tiempo = tiempo_final-tiempo_inicio
        Tiempo+=Total_tiempo
Tiempo = (Tiempo.seconds)//NumeroDeVecesEnLaRed
Horas = Tiempo//3600
Minutos = (Tiempo%3600)//60
Segundos = Tiempo%60
# Tiempo1 = datetime.datetime.strptime(str(Tiempo//NumeroDeVecesEnLaRed), "%H:%M:%S")
# print(f'{Red_a_analizar}: {NumeroDeVecesEnLaRed} veces, promedio: {Tiempo1.hour} horas, {Tiempo1.minute} minutos, {Tiempo1.second} segundos')
print(f'{Red_a_analizar}: {NumeroDeVecesEnLaRed} veces, promedio: {Horas} horas, {Minutos} minutos, {Segundos} segundos')
