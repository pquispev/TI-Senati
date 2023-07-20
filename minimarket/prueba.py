listaproductos = [
    {'nombre': 'MOUSE', 'marca': 'ASUS', 'costo': 12, 'cantidad': 12},
    {'nombre': 'LAPTOP', 'marca': 'ASUS', 'costo': 1200, 'cantidad': 12}
]
s = int(input('elija el numero del producto: '))
print(listaproductos[s-1])