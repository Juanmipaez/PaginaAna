Casos_de_prueba = int(input())
Total_a_pagar = []

for caso in range(Casos_de_prueba):

    Productos_y_precios = []
    while True:
        Precio = float(input())
        if Precio == -1:
            break
        Nombre_producto = str(input())
        Productos_y_precios.append(Precio);Productos_y_precios.append(Nombre_producto)

    Pedido_del_domicilio = []
    Numero_productos = 0
    Subtotal = 0
    while True:
        Cantidad_del_producto = int(input())
        if Cantidad_del_producto == -1:
            break
        Nombre_del_producto = str(input())
        Total_por_producto = Cantidad_del_producto * Productos_y_precios[Productos_y_precios.index(Nombre_del_producto)-1]
        Subtotal += Total_por_producto
        Numero_productos+=Cantidad_del_producto
        Pedido_del_domicilio.append(Cantidad_del_producto);Pedido_del_domicilio.append(Nombre_del_producto)
    
    if (Numero_productos) == 1:
        Total = Subtotal*1.1
    elif 2<=(Numero_productos)<=5:
        Total = Subtotal*1.07
    elif 6<=(Numero_productos)<=10:
        Total = Subtotal*1.05
    else:
        Total = Subtotal
    Total_a_pagar.append(round(Total,0))

for totales in Total_a_pagar:
    print("$",totales,sep="")

