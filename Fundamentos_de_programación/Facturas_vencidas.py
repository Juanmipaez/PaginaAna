from datetime import datetime
Numero_de_facturas = int(input())
Resultados = []
def revisar_vencimiento(lista):
    Fecha_referencia_formato_fecha = datetime.strptime(lista[0], "%Y-%m-%d")
    Fecha_vencimiento_formato_fecha = datetime.strptime(lista[1], "%Y-%m-%d")
    diferencia = Fecha_vencimiento_formato_fecha - Fecha_referencia_formato_fecha

    if (diferencia.days) <= -30:
        mensaje = (f'Vencida: mes(es): {abs(diferencia.days)//30}, horas: {abs(diferencia.days)*24}, minutos: {abs(diferencia.days)*1440}, segundos: {abs(diferencia.days)*86400}')
        Resultados.append(mensaje)
    elif -30 < (diferencia.days) < 0:
        mensaje = (f'Vencida: dias: {abs(diferencia.days)}, horas: {abs(diferencia.days)*24}, minutos: {abs(diferencia.days)*1440}, segundos: {abs(diferencia.days)*86400}')
        Resultados.append(mensaje)
    elif diferencia.days >= 0:
        mensaje = (f'A tiempo: vence en {diferencia.days} dias')
        Resultados.append(mensaje)

Lista_temporal = []
for casos in range(Numero_de_facturas):
    Fecha_referencia = str(input())
    Fecha_de_vencimiento = str(input())
    Lista_temporal.append(Fecha_referencia);Lista_temporal.append(Fecha_de_vencimiento)
    revisar_vencimiento(Lista_temporal)
    Lista_temporal.clear()

for resultado in Resultados:
    print(resultado)