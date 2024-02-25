import datetime
Numero_de_publicaciones = int(input())
Lista_de_publicaciones = []
for casos in range(Numero_de_publicaciones):
    fecha_hora = str(input())
    Lista_de_publicaciones.append(fecha_hora)

def analizar_engagement(fecha):
    fecha_en_formato = datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
    if fecha_en_formato.weekday() != 1:
        if (0 <=fecha_en_formato.hour <=4) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Otro dia: Engagement bajo")
        elif (fecha_en_formato.hour == 23) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Otro dia: Engagement bajo")
        else:
            print("Otro dia: Sin informacion")
    
    elif fecha_en_formato.weekday() == 1:
        if (0 <=fecha_en_formato.hour <= 4) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement medio bajo")
        elif (fecha_en_formato.hour == 23) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement medio bajo")
        elif (5<=fecha_en_formato.hour<=6) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement medio")
        elif (16<=fecha_en_formato.hour<=23) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement medio")
        elif (fecha_en_formato.hour==7) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement medio alto")
        elif (14<=fecha_en_formato.hour<=15) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement medio alto")
        elif (8<=fecha_en_formato.hour<=13) and (0<=fecha_en_formato.minute<=59) and (0<=fecha_en_formato.second<=59):
            print("Martes: Engagement alto")

for fecha in Lista_de_publicaciones:
    analizar_engagement(fecha)