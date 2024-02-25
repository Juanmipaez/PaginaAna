Lista_cambios_totales = []

while True:
    Dimesion_matriz = int(input())
    if Dimesion_matriz == 0:
        break
    Tabla_inicial = []
    for fila in range(Dimesion_matriz):
        Tabla_por_entrada = []
        Fila = input()
        for entrada in Fila:
            Tabla_por_entrada.append(entrada)
        Tabla_inicial.append(Tabla_por_entrada)
    Cambios_a_realizar = input()
    Cambios_a_realizar = Cambios_a_realizar.split(" x")
    Lista_cambios = (Cambios_a_realizar[0].split(" "))
    for index_cambios in range(0,len(Lista_cambios),2):
        if Lista_cambios[index_cambios] == "f":
            if int(Lista_cambios[index_cambios+1]) > 0:
                Tabla_temporal = Tabla_inicial[int(Lista_cambios[index_cambios+1])-1].copy() #Extraer el numero de la fila sobre el que se va a realizar el cambio
                for cambio in range(len(Tabla_inicial)):
                    if (cambio+1) == Dimesion_matriz:
                        Tabla_inicial[int(Lista_cambios[index_cambios+1])-1][0] = Tabla_temporal[cambio]
                    else:
                        Tabla_inicial[int(Lista_cambios[index_cambios+1])-1][cambio+1]= Tabla_temporal[cambio]
            else:
                Tabla_temporal = Tabla_inicial[abs(int(Lista_cambios[index_cambios+1]))-1].copy() #Extraer el numero de la fila sobre el que se va a realizar el cambio
                for cambio in range(len(Tabla_inicial)):
                    if (cambio+1) == Dimesion_matriz:
                        Tabla_inicial[abs(int(Lista_cambios[index_cambios+1]))-1][cambio] = Tabla_temporal[0]
                    else:
                        Tabla_inicial[abs(int(Lista_cambios[index_cambios+1]))-1][cambio]= Tabla_temporal[cambio+1]
                
        elif Lista_cambios[index_cambios] == "c":
            Tabla_temporal2= []
            for elementos_columna in range(Dimesion_matriz):
                Tabla_temporal2.append(Tabla_inicial[elementos_columna][abs(int(Lista_cambios[index_cambios+1]))-1])

            if int(Lista_cambios[index_cambios+1]) > 0:
                for cambio in range(len(Tabla_inicial)):
                    if (cambio+1) == Dimesion_matriz:
                        Tabla_inicial[0][int(Lista_cambios[index_cambios+1])-1] = Tabla_temporal2[cambio]
                    else:
                        Tabla_inicial[cambio+1][int(Lista_cambios[index_cambios+1])-1]= Tabla_temporal2[cambio]
            else:
                for cambio in range(len(Tabla_inicial)):
                    if (cambio+1) == Dimesion_matriz:
                        Tabla_inicial[cambio][abs(int(Lista_cambios[index_cambios+1]))-1] = Tabla_temporal2[0]
                    else:
                        Tabla_inicial[cambio][abs(int(Lista_cambios[index_cambios+1]))-1]= Tabla_temporal2[cambio+1]
    Lista_cambios_totales.append(Tabla_inicial)
for tablas in Lista_cambios_totales:
    for tabla1 in tablas:
        print(*tabla1,sep="")
    print("---")