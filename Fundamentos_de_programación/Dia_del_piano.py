import datetime
Numero_de_fechas = int(input())
Fechas = []

for fecha in range(Numero_de_fechas):
    fecha = str(input())
    Fechas.append(fecha)

def analizarFechas(lista):
    for fecha in lista:
        fecha = fecha.split(" ")
        Fecha1 = datetime.datetime.strptime(str(fecha[0]), "%d/%m/%Y").date()
        Fecha2 = datetime.datetime.strptime(str(fecha[1]), "%d/%m/%Y").date()
        Marzo29 = datetime.date(Fecha1.year,3,29)
        Marzo28 = datetime.date(Fecha1.year,3,28)
        Año = datetime.timedelta(days=366)
        Contador_28Marzo = 0
        Contador_29Marzo = 0
        for años in range((Fecha2.year-Fecha1.year)+1):
            if Fecha1 < Marzo28:
                if ((Fecha1.year)%400 == 0) or ((Fecha1.year%4==0) and (Fecha1.year%100 !=0)):
                    if Fecha1<Marzo28<(Fecha1+Año):
                        Contador_28Marzo+=1
                else:
                    if Fecha1<Marzo29<(Fecha1+Año):
                        Contador_29Marzo+=1
                Fecha1+=Año
                Marzo28+=Año
                Marzo29+=Año
            elif Marzo28 < Fecha1:
                if ((Fecha1.year)%400 == 0) or ((Fecha1.year%4 == 0) and (Fecha1.year%100 !=0)):
                    if Fecha1<(Marzo28+Año)<(Fecha1+Año):
                        Contador_28Marzo+=1
                else:
                    if Fecha1<(Marzo29+Año)<(Fecha1+Año):
                        Contador_29Marzo+=1
                Fecha1+=Año
                Marzo28+=Año
                Marzo29+=Año
        print("29 de marzo:",Contador_29Marzo);print("28 de marzo:",Contador_28Marzo)
analizarFechas(Fechas)