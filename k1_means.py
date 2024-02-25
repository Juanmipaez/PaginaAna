import random

S= []
k1 = random.choice(S)
S.remove(k1) #Se elimina el elemento de la lista para no tener el mismo centroíde dos veces
k2 = random.choice(S)
S.append(k1)

for iteraciones in range(40):
    dk1 = []
    dk2 = []
    dk3 = []
    for dato in S:
        distancias = []
        d1 = abs(dato-k1)
        d2 = abs(dato-k2)
        distancias.extend([d1,d2])
        
        #Se agrega cada punto muestral a la categoria que le corresponde, analizando su distanci a cada centroide
        if d1>d2:
            dk2.append(dato)
        else:
            dk1.append(dato)

    #Actualizar centroides con la media
    Nk1 = sum(dk1)/len(dk1) if len(dk1)>0 else k1
    Nk2 = sum(dk2)/len(dk2) if len(dk2)>0 else k2

    if (  (abs(Nk1-k1) <= 0.00000000001) and (abs(Nk2-k2) <= 0.00000000001) ) :
        print("rompió ciclo por convergencia")
        break

    k1 = Nk1
    k2 = Nk2


print(Nk1,Nk2)
print(dk1,dk2)

