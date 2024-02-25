Cantidad_de_nombres = int(input())
Nombres = []
for casos in range(Cantidad_de_nombres):
    nombre = str(input())
    Nombres.append(nombre)

def origen_nombre(x):
    terminacion = x[-2]+x[-1]
    if terminacion == "ix":
        return "Galo"
    elif terminacion == "us":
        return "Romano"
    elif terminacion == "ic":
        return "Godo"
    elif terminacion == "as":
        return "Griego"
    elif terminacion == "af":
        return "Normando"
    elif terminacion in ["is","ax"]:
        return "Breton"
    elif terminacion == "ez":
        return "Hispano"
    elif x[-1] == "a":
        return "Indio"
    else:
        return "Desconocido"
    
for nombre in Nombres:
    print(origen_nombre(nombre))