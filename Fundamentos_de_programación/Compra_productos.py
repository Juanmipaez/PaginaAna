Cantidad_de_productos_en_inventario = int(input())
Productos_precio = {}

for productos in range(Cantidad_de_productos_en_inventario):
    ProductoPrecio = str(input())
    ProductosPrecio_lista = ProductoPrecio.split(":")
    Productos_precio[ProductosPrecio_lista[0]]= int(ProductosPrecio_lista[1])

Cantidad_de_productos_a_comprar = int(input())

Total = 0
for compra in range(Cantidad_de_productos_a_comprar):
    Compra = str(input())
    Compra_lista = Compra.split(" ")
    Total_por_producto = Productos_precio[Compra_lista[0]] * int(Compra_lista[1])
    Total += float(Total_por_producto)

if Total<100000:
    print(Total)
else:
    print(Total*0.7)