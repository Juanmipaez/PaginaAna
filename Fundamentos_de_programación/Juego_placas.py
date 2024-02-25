Numero_de_casos = int(input())
Resultados = []

for caso in range(Numero_de_casos):
    Placa = str(input())
    Lista_placa = Placa.split(" ")
    Placa_en_que_viajo = Lista_placa[0]
    contador = 0
    for placas in Lista_placa:
        if Placa_en_que_viajo < placas:
            Resultados.append("Parece que hay otro vehiculo mas modeludo en el camino")
            contador = 0
            break
        elif Placa_en_que_viajo > placas:
            contador+=1
    if contador >=1:
        Resultados.append("Estoy viajando en el vehiculo mas modeludo del camino")
        

for resultado in Resultados:
    print(resultado)