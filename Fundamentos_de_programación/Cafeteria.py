Casos_de_prueba = int(input())

Estudiantes_que_no_cambian = []

def organizar_fila(x):
    contador = 0
    copia = x.copy()
    copia.sort(reverse = True)
    for nota in x:
        if x.index(nota) == copia.index(nota):
            contador+=1
    Estudiantes_que_no_cambian.append(contador)


for caso in range(Casos_de_prueba):
    Numero_estudiantes_en_la_fila = int(input())
    Notas_por_caso = []
    Notas_por_caso.clear()
    for nota in range(Numero_estudiantes_en_la_fila):
        Nota_estudiante = float(input())
        Notas_por_caso.append(Nota_estudiante)
    organizar_fila(Notas_por_caso)

for estudiantes in Estudiantes_que_no_cambian:
    print(estudiantes)
    
