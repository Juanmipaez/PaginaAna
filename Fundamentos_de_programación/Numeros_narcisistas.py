def narcisista(x):
    Numero_en_string = str(x)
    Exponentes_de_numeros = []
    Longitud_numero = len(Numero_en_string)
    for digito in Numero_en_string:
        Exponentes_de_numeros.append((int(digito)**Longitud_numero))
    if x == sum(Exponentes_de_numeros):
        return 1
    else: 
        return 0
