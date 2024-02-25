import datetime
Cantidad_vuelos_analizar = int(input())
Casos_globales = []

for casos in range(Cantidad_vuelos_analizar):
    Informacion_por_caso = str(input())
    Casos_globales.append(Informacion_por_caso)

def analizar_vuelos(lista):
    for caso in lista:
        caso = caso.split(" ")
        Dia = datetime.timedelta(hours = 24)
        Hsv1 = datetime.timedelta(hours=int(caso[0].split(":")[0]),minutes=int(caso[0].split(":")[1]))
        Hlv1 = datetime.timedelta(hours=int(caso[1].split(":")[0]),minutes=int(caso[1].split(":")[1]))
        Hsv2 = datetime.timedelta(hours=int(caso[2].split(":")[0]),minutes=int(caso[2].split(":")[1]))
        Hlv2 = datetime.timedelta(hours=int(caso[3].split(":")[0]),minutes=int(caso[3].split(":")[1]))
        Tmc  = datetime.timedelta(hours=int(caso[4].split(":")[0]),minutes=int(caso[4].split(":")[1]))
        Dv1 = Hlv1-Hsv1
        Dv2 = Hlv2-Hsv2
        if Hsv2<Hlv1:
            Tev = ((Hsv2+Dia)-Hlv1)
        else:
            Tev=(Hsv2-Hlv1)
        #Se usan los siguientes formatos extensos porque sino, imprime en formato HH:MM:SS asi que hay que modificarlo
        if Tmc <= Tev:
            print((f'{"{0:02d}".format(Dv1.seconds//3600)}:{"{0:02}".format(Dv1.seconds%3600//60)}'), ((f'{"{0:02d}".format(Dv2.seconds//3600)}:{"{0:02}".format(Dv2.seconds%3600//60)}')), ((f'{"{0:02d}".format(Tev.seconds//3600)}:{"{0:02}".format(Tev.seconds%3600//60)}')), "Si se puede")
        elif Tmc > Tev:
            print((f'{"{0:02d}".format(Dv1.seconds//3600)}:{"{0:02}".format(Dv1.seconds%3600//60)}'), ((f'{"{0:02d}".format(Dv2.seconds//3600)}:{"{0:02}".format(Dv2.seconds%3600//60)}')), ((f'{"{0:02d}".format(Tev.seconds//3600)}:{"{0:02}".format(Tev.seconds%3600//60)}')), "No se puede")
    
analizar_vuelos(Casos_globales)