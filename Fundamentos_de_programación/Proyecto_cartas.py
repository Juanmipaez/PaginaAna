import random
import datetime
def caso1():
    print(" ___   ___   ___")
    print("|J  | |Q  | |8  |")
    print("| ♦ | | ♥ | | ♣ |")
    print("|__J| |__Q| |__8|")

def caso2():
    print(" ___   ___   ___")
    print("|Q  | |J  | |8  |")
    print("| ♥ | | ♦ | | ♣ |")
    print("|__Q| |__J| |__8|")

def caso3():
    print(" ___   ___   ___")
    print("|8  | |Q  | |J  |")
    print("| ♣ | | ♥ | | ♦ |")
    print("|__8| |__Q| |__J|")

def caso4():
    print(" ___   ___   ___")
    print("|Q  | |8  | |J  |")
    print("| ♥ | | ♣ | | ♦ |")
    print("|__Q| |__8| |__J|")

def caso5():
    print(" ___   ___   ___")
    print("|J  | |8  | |Q  |")
    print("| ♦ | | ♣ | | ♥ |")
    print("|__J| |__8| |__Q|")

def caso6():
    print(" ___   ___   ___")
    print("|8  | |J  | |Q  |")
    print("| ♣ | | ♦ | | ♥ |")
    print("|__8| |__J| |__Q|")

Casos_movimientos = ["Izquierda a Derecha","Izquierda a Medio","Medio a Izquierda","Medio a Derecha","Derecha a Medio","Derecha a Izquierda"]
Paso0_noombre = 0
puntaje = 0
while True:
    print("\n¿Adónde se ha ido la reina de corazones?")
    print("Por favor digita la letra de una de las siguientes opciones:")
    print("1. Jugar (J)")
    print("2. Historial de posiciones (H)")
    print("3. Salir del juego (S)")
    while True:
        Eleccion_usuario = input("Opcion: ").upper()
        if Eleccion_usuario in ("J","H","S"):
            break
        else:
            print("Por favor seleccione una opción valida")
            continue
    if Paso0_noombre == 0:
        if Eleccion_usuario == "S":
            print("Gracias por jugar, hasta la próxima!")
            exit()
    else:
        if Eleccion_usuario == "S":
            print("Gracias por jugar, hasta la próxima!")
            file = open("C:/Users/Juanm/.vscode/Code/Fundamentos_de_programación/Puntajes.txt","a")
            print(f'{Nombre_usuario}, {puntaje}, {fecha}, {hora} ', file = file)
            file.close()
            exit()
    
    def f_puntaje():
        file = open("C:/Users/Juanm/.vscode/Code/Fundamentos_de_programación/Puntajes.txt","r")
        inicio = 0
        Lista_datos = []
        Nombres_sin_repetir = []
        for linea in file:
            linea = (linea.strip()).split(",")
            Lista_datos.append(linea)
            nombre = linea[0]
            if nombre not in Nombres_sin_repetir:
                Nombres_sin_repetir.append(nombre)
        file.close()

        Nombres_y_puntajes = {}
        for nombre in Nombres_sin_repetir:
            puntaje_por_caso = 0
            for lineas in Lista_datos:
                if nombre == lineas[0]:
                    puntaje_por_caso+=int(lineas[1])
            Nombres_y_puntajes[nombre]=puntaje_por_caso
        Nombres_y_puntajes = dict(sorted(Nombres_y_puntajes.items(), key=lambda item: item[1], reverse=True))
        
        Nombres_sin_repetir = []
        for nombre in Nombres_y_puntajes:
            Nombres_sin_repetir.append(nombre) 
        
        for index in range(5):
            nombre = Nombres_sin_repetir[index]
            Lista_para_fecha = []
            for lineas in Lista_datos:
                puntaje_fecha_hora = {}
                if nombre == lineas[0]:
                    puntaje_fecha_hora["puntaje"]=int(lineas[1])
                    combinacion =(lineas[2] + lineas[3]).upper()
                    puntaje_fecha_hora["Fecha"] = datetime.datetime.strptime(combinacion, " %Y-%m-%d %H:%M:%S")
                    Lista_para_fecha.append(puntaje_fecha_hora)

            Lista_para_fecha.sort(key=lambda item: (item["puntaje"],item["Fecha"]), reverse=True)
            Hora = Lista_para_fecha[0]["Fecha"].time()
            Hora1 = Hora.strftime("%H:%M:%S")
            print(f'{index+1}. {nombre}, {Nombres_y_puntajes[nombre]} puntos. Mejor jugada el {(Lista_para_fecha[0]["Fecha"].date())} a las {Hora1.lower()} con {(Lista_para_fecha[0]["puntaje"])} puntos')

    if Eleccion_usuario == "H":
        if Paso0_noombre==0:
            print("\n""Top de lo(a)s 5 mejores:""\n")
            f_puntaje()
            Paso0_noombre+=1
            exit()
        else:
            file = open("C:/Users/Juanm/.vscode/Code/Fundamentos_de_programación/Puntajes.txt","a")
            print(f'{Nombre_usuario}, {puntaje}, {fecha}, {hora} ', file = file)
            file.close()
            print("\n""Top de lo(a)s 5 mejores:""\n")
            f_puntaje()
            exit()

    if Paso0_noombre == 0:
        Nombre_usuario = input("Ingresa tu nombre: ").title()
        Paso0_noombre+=1

    if Eleccion_usuario == "J":
            fecha = datetime.datetime.now().date()
            hora = datetime.datetime.now().time()
            hora = hora.strftime("%H:%M:%S")
            print(f'¡{Nombre_usuario}, presta mucha atención para que puedas adivinar dónde está la reina de corazones!')
            numero_random = random.randrange(6)
            if numero_random == 0:
                Posicion_cartas = ["D","R","T"]
                caso1()
            elif numero_random == 1:
                Posicion_cartas = ["R","D","T"]
                caso2()
            elif numero_random == 2:
                Posicion_cartas = ["T","R","D"]
                caso3()
            elif numero_random == 3:
                Posicion_cartas = ["R","T","D"]
                caso4()
            elif numero_random == 4:
                Posicion_cartas = ["D","T","R"]
                caso5()
            else:
                Posicion_cartas = ["T","D","R"]
                caso6()
            inicio_juego = input("\n""Presiona ENTER cuando estés listo para jugar: ""\n")

            for num in range(random.randrange(2,5)):
                numero_random = random.randrange(6)
                if numero_random == 0:
                    print(Casos_movimientos[0])   
                    Posicion_cartas[0],Posicion_cartas[2] = Posicion_cartas[2],Posicion_cartas[0]
                elif numero_random == 1:
                    print(Casos_movimientos[1])   
                    Posicion_cartas[0],Posicion_cartas[1] = Posicion_cartas[1],Posicion_cartas[0]
                elif numero_random == 2:
                    print(Casos_movimientos[2])   
                    Posicion_cartas[1],Posicion_cartas[0] = Posicion_cartas[0],Posicion_cartas[1]
                elif numero_random == 3:
                    print(Casos_movimientos[3])   
                    Posicion_cartas[1],Posicion_cartas[2] = Posicion_cartas[2],Posicion_cartas[1]
                elif numero_random == 4:
                    print(Casos_movimientos[4])   
                    Posicion_cartas[2],Posicion_cartas[1] = Posicion_cartas[1],Posicion_cartas[2]
                else:
                    print(Casos_movimientos[5])   
                    Posicion_cartas[2],Posicion_cartas[0] = Posicion_cartas[0],Posicion_cartas[2]
            
            print(" ___   ___   ___")
            print("|   | |   | |   |")
            print("| ? | | ? | | ? |")
            print("|___| |___| |___|""\n")

            eleccion_nueva = input("¿En cuál de las cartas está la reina de corazones?: Ingresa [I], [M], [D]: ").upper()
            if eleccion_nueva == "D" and Posicion_cartas[2] == "R":
                print("Felicitaciones, +1 punto para ti")
                puntaje += 1
            elif eleccion_nueva == "M" and Posicion_cartas[1] == "R":
                print("Felicitaciones, +1 punto para ti")
                puntaje += 1
            elif eleccion_nueva == "I" and Posicion_cartas[0] == "R":
                print("Felicitaciones, +1 punto para ti")
                puntaje += 1
            else:
                print("Lo siento, has perdido")
