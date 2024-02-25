file = open("Fundamentos_de_programación/Discursos.txt","r")
Ex_opositivas = ["Por otro lado","A pesar de","En cambio","Mientras que","No solo","Sin embargo"]
Ex_causativas = ["Hacer que","Obligar a","Convencer a","Inducir a","Permitir que"]

for linea in file:
    contador_opositivos = 0
    contador_causativos = 0
    for expresionOp in Ex_opositivas:
        if expresionOp in linea or expresionOp.lower() in linea:
            contador_opositivos+=1
    for expresionCau in Ex_causativas:
        if expresionCau in linea or expresionCau.lower() in linea:
            contador_causativos+=1
    print(f'Opositivos {contador_opositivos} Causativos {contador_causativos}')
