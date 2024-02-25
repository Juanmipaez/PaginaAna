Numeros_a_letras = {"0":["0"," "],"1":["1",".",",","!",":"],"2":["2","A","B","C"],"3":["3","D","E","F"],"4":["4","G","H","I"],"5":["5","J","K","L"],"6":["6","M","N","O"],"7":["7","P","Q","R","S"],"8":["8","T","U","V"],"9":["9","W","X","Y","Z"],"*":["*"],"#":["#"],".":["11"],",":["111"],"!":["1111"],":":["11111"],"A":["22"],"B":["222"],"C":["2222"],"D":["33"],"E":["333"],"F":["3333"],"G":["44"],"H":["444"],"I":["4444"],"J":["55"],"K":["555"],"L":["5555"],"M":["66"],"N":["666"],"O":["6666"],"P":["77"],"Q":["777"],"R":["7777"],"S":["77777"],"T":["88"],"U":["888"],"V":["8888"],"W":["99"],"X":["999"],"Y":["9999"],"Z":["99999"]," ":["00"]}
Lista_entrada = []
while True:
    Mensaje = str(input()).upper()
    if Mensaje == "-1":
        break
    Lista_entrada.append(Mensaje)

for Mensajes in Lista_entrada:
    Entero = False
    try:
        Caracter_inicial = int(Mensajes[0])
        Entero = True
    except:
        Entero = False
    
    if Entero == True:
        Mensajes = Mensajes.split("_")
        for palabras in Mensajes:
            Numero_sub0 = palabras[0]
            print(Numeros_a_letras.get(str(Numero_sub0))[len(palabras)-1],end="")
        print("")
    elif Entero == False:
            for index in range(len(Mensajes)-1):
                Entero = False
                try:
                    Caracter = int(Mensajes[index])
                    Entero = True
                except:
                    Entero = False
                if Entero == True:
                    print(Caracter,end="_")
                else:
                    print(*Numeros_a_letras.get(Mensajes[index]),end="_")
            print(*Numeros_a_letras.get(Mensajes[-1]))
