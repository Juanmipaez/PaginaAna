import random
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

print("\n¿Adónde se ha ido la reina de corazones?")
print("Por favor digita la letra de una de las siguientes opciones:")
print("1. Jugar (J)")
print("2. Historial de posiciones (H)")
print("3. Salir del juego (S)")
while True:
    Eleccion_usuario = input("Opcion: ").capitalize() 
    if Eleccion_usuario in ("J","H","S"):
        break
    else:
        print("Por favor seleccione una opción valida")
        continue
    
if Eleccion_usuario == "S":
    print("Gracias por jugar, hasta la próxima!")
    exit()
    
if Eleccion_usuario == "H":
    exit()

Nombre_usuario = input("Ingresa tu nombre: ").capitalize()
if Eleccion_usuario == "J":
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
        #print(Posicion_cartas)

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
        
        #print("\n",Posicion_cartas)
        print(" ___   ___   ___")
        print("|   | |   | |   |")
        print("| ? | | ? | | ? |")
        print("|___| |___| |___|""\n")
    
        eleccion_nueva = input("¿En cuál de las cartas está la reina de corazones?: Ingresa [I], [M], [D]: ")
        if eleccion_nueva == "D" and Posicion_cartas[2] == "R":
            print("Felicitaciones, +1 punto para ti")
        elif eleccion_nueva == "M" and Posicion_cartas[1] == "R":
            print("Felicitaciones, +1 punto para ti")
        elif eleccion_nueva == "I" and Posicion_cartas[0] == "R":
            print("Felicitaciones, +1 punto para ti")
        else:
            print("Lo siento, has perdido")


while True:
    print("\n""Por favor digita la letra de una de las siguientes opciones:")
    print("1. Jugar (J)")
    print("2. Historial de posiciones (H)")
    print("3. Salir del juego (S)")
    while True:
        Eleccion_usuario = input("Opcion: ").capitalize() 
        if Eleccion_usuario in ("J","H","S"):
            break
        else:
            print("Por favor seleccione una opción valida")
            continue
        
    if Eleccion_usuario == "S":
        print("Gracias por jugar, hasta la próxima!")
        exit()
        
    if Eleccion_usuario == "H":
        exit()
    
    print("Ingresa nombre:",Nombre_usuario)
    if Eleccion_usuario == "J":
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
        inicio_juego = input("\n""Presiona ENTER cuando estés listo para jugar: ")
        print(Posicion_cartas)

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
        
        #print("\n",Posicion_cartas)
        print(" ___   ___   ___")
        print("|   | |   | |   |")
        print("| ? | | ? | | ? |")
        print("|___| |___| |___|""\n")
    
        eleccion_nueva = input("¿En cuál de las cartas está la reina de corazones?: Ingresa [I], [M], [D]: ")
        if eleccion_nueva == "D" and Posicion_cartas[2] == "R":
            print("Felicitaciones, +1 punto para ti")
        elif eleccion_nueva == "M" and Posicion_cartas[1] == "R":
            print("Felicitaciones, +1 punto para ti")
        elif eleccion_nueva == "I" and Posicion_cartas[0] == "R":
            print("Felicitaciones, +1 punto para ti")
        else:
            print("Lo siento, has perdido")

