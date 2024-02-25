import random
S= [-8,-6,-9,-1,0,1,8,6,9]
k1 = random.choice(S)
S.remove(k1) #Se elimina el elemento de la lista para no tener el mismo centroíde dos veces
k2 = random.choice(S)
S.remove(k2)
k3 = random.choice(S)
S.append(k1)
S.append(k2)
S.sort()

while True:
    dk1 = []
    dk2 = []
    dk3 = []
    for dato in S:
        distancias = []
        d1 = abs(dato-k1)
        d2 = abs(dato-k2)
        d3 = abs(dato-k3)
        distancias.extend([d1,d2,d3])

        #Se agrega cada punto muestral a la categoria que le corresponde, analizando su distanci a cada centroide
        if min(distancias) == d1:
            dk1.append(dato)
        elif min(distancias) == d2:
            dk2.append(dato)
        else:
            dk3.append(dato)
    
    #Actualizar centroides con la media
    Nk1 = sum(dk1)/len(dk1)
    Nk2 = sum(dk2)/len(dk2)
    Nk3 = sum(dk3)/len(dk3)

    if (  (abs(Nk1-k1) <= 0.00000000000001) and (abs(Nk2-k2) <= 0.00000000000001) and (abs(Nk3-k3) <= 0.00000000000001) ) :
        print("rompió ciclo por convergencia")
        break
    
    k1 = Nk1
    k2 = Nk2
    k3 = Nk3


print(Nk1,Nk2,Nk3)
print(dk1,dk2,dk3)

