import datetime;import math
Casos_a_procesar = int(input())
Lista_datos_ingreso = []

for datos in range(Casos_a_procesar):
    Horas = str(input())
    Campanadas = str(input())
    Lista_datos_ingreso.append(Horas); Lista_datos_ingreso.append(Campanadas)

for index in range(0,len(Lista_datos_ingreso),2):
    Horas = Lista_datos_ingreso[index].split(" ")
    Info_campanadas = Lista_datos_ingreso[index+1].split(" ")
    Hora_inicial = datetime.datetime.strptime(str(Horas[0]),"%H:%M:%S")
    Hora_final = datetime.datetime.strptime(str(Horas[1]),"%H:%M:%S")
    Numero_campanadas = int(Info_campanadas[0])
    Campanada_a_tocar = int(Info_campanadas[1])
    Dia = datetime.timedelta(hours=24)

    if Hora_final<Hora_inicial:
        Diferencia_horaria = math.ceil(((((Hora_final+Dia) - Hora_inicial).total_seconds())//Numero_campanadas -1))
        Intervalos_entre_campanadas = datetime.timedelta(seconds=Diferencia_horaria)
        if Campanada_a_tocar == 1:
            print(Hora_inicial.time())
        elif Campanada_a_tocar==Numero_campanadas:
            print(Hora_final.time())
        else:
            hora = Hora_inicial + ((Campanada_a_tocar-1)*Intervalos_entre_campanadas)
            print(hora.time())
    
    elif Hora_inicial<Hora_final:
        Diferencia_horaria = math.ceil((((Hora_final - Hora_inicial).total_seconds())//Numero_campanadas -1))
        Intervalos_entre_campanadas = datetime.timedelta(seconds=Diferencia_horaria)
        if Campanada_a_tocar == 1:
            print(Hora_inicial.time())
        elif Campanada_a_tocar==Numero_campanadas:
            print(Hora_final.time())
        else:
            hora = Hora_inicial + ((Campanada_a_tocar-1)*Intervalos_entre_campanadas)
            print(hora.time())