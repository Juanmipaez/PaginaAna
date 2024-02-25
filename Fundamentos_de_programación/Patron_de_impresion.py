Numero_de_lineas = int(input())
espacio = " "
divisiones = int((Numero_de_lineas-2)/2)
Divisiones_20 = divisiones
for primer_caso in range(divisiones):
    print(espacio*primer_caso,"*",espacio*(divisiones-1),"**",espacio*(divisiones-1),"*",espacio*primer_caso,sep="")
    divisiones-=1

for segundo_caso in range(2):
    print("*"*Numero_de_lineas)


index = Divisiones_20-1
for tercer_caso in range(Divisiones_20):
    print(espacio*index,"*",espacio*tercer_caso,"**",espacio*tercer_caso,"*",espacio*index,sep="")
    index-=1

