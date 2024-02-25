import datetime

file = open("C:/Users/Juanm/.vscode/Code/Fundamentos_de_programación/puntajes2.txt","r")
Top_a_generar = int(input())
inicio = 0
Lista_datos = []
Nombres_sin_repetir = []

#Coger todas lass lineas del archivo y meterlas en una lista, además, sacar todos los nombres que hay (sin repeticiones)
for linea in file:
    linea = (linea.strip()).split(",")
    Lista_datos.append(linea)
    nombre = linea[0]
    if nombre not in Nombres_sin_repetir:
        Nombres_sin_repetir.append(nombre)
file.close()

#Crear un diccionario con el nombre de cada jugador, y la suma de todos sus puntajes
Nombres_y_puntajes = {}
for nombre in Nombres_sin_repetir:
    puntaje_por_caso = 0
    for lineas in Lista_datos:
        if nombre == lineas[0]:
            puntaje_por_caso+=int(lineas[1])
    Nombres_y_puntajes[nombre]=puntaje_por_caso
#Organizar el diccionario de mayor a menor puntaje total
Nombres_y_puntajes = dict(sorted(Nombres_y_puntajes.items(), key=lambda item: item[1], reverse=True))

Nombres_sin_repetir = []
for nombre in Nombres_y_puntajes:
    Nombres_sin_repetir.append(nombre) #Organizar la lista de nombres inicial en función de la suma de los puntos


for index in range(Top_a_generar):
    nombre = Nombres_sin_repetir[index]
    #En esta lista se van a añadir mini-diccionarios. Van a tener el puntaje, fecha y hora.
    Lista_para_fecha = []
    for lineas in Lista_datos:
        puntaje_fecha_hora = {}

        if nombre == lineas[0]:
            puntaje_fecha_hora["puntaje"]=int(lineas[1])
            combinacion_para_fecha_hora = (lineas[2] + lineas[3]).upper()
            puntaje_fecha_hora["Fecha"] = datetime.datetime.strptime(combinacion_para_fecha_hora, " %Y-%m-%d %I:%M%p")
            Lista_para_fecha.append(puntaje_fecha_hora)
    #Organizar dicha lista, primero por puntaje, y luego si tienen el mismo puntaje, por la fecha más reciente
    Lista_para_fecha.sort(key=lambda item: (item["puntaje"],item["Fecha"]), reverse=True)
    Hora = Lista_para_fecha[0]["Fecha"].time()
    Hora1 = Hora.strftime("%I:%M%p")
    print(f'{index+1}. {nombre}, {Nombres_y_puntajes[nombre]} puntos. Mejor jugada el {(Lista_para_fecha[0]["Fecha"].date())} a las {Hora1.lower()} con {(Lista_para_fecha[0]["puntaje"])} puntos')

