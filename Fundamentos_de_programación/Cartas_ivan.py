import random
from datetime import datetime

tabla_posiciones = {}

def MostrarCartas(lista):
    Renglones = ["", "", "", ""]
    for elemento in lista:
        if elemento == 1: Dato = carta1
        elif elemento == 2: Dato = carta2
        elif elemento == 3: Dato = carta3
        for i in range(4):
            Renglones[i] += Dato[i]
    for elemento in Renglones: print(elemento)

def MoverCartas(lista):
    cambio = [random.randint(0, 2)]
    elemento_dato = lista[cambio[0]]
    while True:
        cambio.append(random.randint(0, 2))
        if cambio[1] != cambio[0]:
            break
        cambio.pop()
    lista[cambio[0]] = lista[cambio[1]]
    lista[cambio[1]] = elemento_dato
    Resultado = "Intercambio"
    if cambio[0] == 0: Resultado += "izquierda (I) con la "
    elif cambio[0] == 1: Resultado += "la del medio (M) con la "
    elif cambio[0] == 2: Resultado += "derecha (D) con la "
    if cambio[1] == 0: Resultado += "izquierda (I)"
    elif cambio[1] == 1: Resultado += "del medio (M)"
    elif cambio[1] == 2: Resultado += "derecha (D)"
    print(Resultado)
    return lista

carta1 = [
    " ___  ",
    "|J  | ",
    "| ♦ | ",
    "|__J| ",
]

carta2 = [
    " ___  ",
    "|Q  | ",
    "| ♥ | ",
    "|__Q| ",
]

carta3 = [
    " ___  ",
    "|8  | ",
    "| ♣ | ",
    "|__8| ",
]

print()
print("Adivina dónde está la reina de corazones")
print()

while True:
    ingresar_usuario = input("> Seleccione: Jugar[J], tabla de posiciones[T], salir[S]:").upper()
    nombre = input("> Por favor, indique su nombre: ")

    if ingresar_usuario == "J":
        print("¡"+nombre+" mantén tus bien ojos abiertos mientras las cartas se mueven!")

        lista = []
        for i in range(3):
            while True:
                A = random.randint(1, 3)
                if A not in lista:
                    lista += [A]
                    break

        it = random.randint(2, 4)
        MostrarCartas(lista)
        print()
        input("> Presiona ENTER cuando estés listo(a)")

        for i in range(it):
            lista = MoverCartas(lista)

        Adivina = input("> ¿En cuál de las cartas está la reina de corazones? [I], [M], [D]:").upper()

        if (Adivina == "I" and lista[0] == 2) or (Adivina == "M" and lista[1] == 2) or (Adivina == "D" and lista[2] == 2):
            MostrarCartas(lista)
            print()
            print("¡Felicitaciones, reclama una olla a presión!")
            print()

            # Guardar el resultado en la tabla de posiciones
            puntaje = 10  # Puedes ajustar el puntaje según tus criterios
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tabla_posiciones[nombre] = {"puntos": puntaje, "mejor_jugada": fecha_hora}

        else:
            MostrarCartas(lista)
            print()
            print("¡Lo siento, reclama un tarrito para que recojas las lágrimas!")
            print()

    elif ingresar_usuario == "T":
        print("Tabla de Posiciones:")
        if tabla_posiciones:
            # Mostrar la tabla de posiciones ordenada por puntos de mayor a menor
            posiciones_ordenadas = sorted(tabla_posiciones.items(), key=lambda x: x[1]["puntos"], reverse=True)
            for i, (jugador, datos) in enumerate(posiciones_ordenadas, start=1):
                print(f"{i}. {jugador}, {datos['puntos']} puntos. Mejor jugada el {datos['mejor_jugada']}")
        else:
            print("¡La tabla de posiciones está vacía!")

    elif ingresar_usuario == "S":
        print("¡Adiós!")
        break