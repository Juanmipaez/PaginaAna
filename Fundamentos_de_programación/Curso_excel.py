Letras =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Numero_filas = int(input())
orden = ["A1=3","B4:E4=5","C8=SUMA(E5)","D1=5"]
orden.sort(key = lambda item:item[1])
print(orden)