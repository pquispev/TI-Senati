listaproductos = [{'nombre': 'ASUS', 'marca': 'ASUS', 'costo': 12, 'cantidad': 12}]

nombreproducto = 'ASUS'
cantidadproducto= 2

for producto in listaproductos:
    if producto.get("nombre") == nombreproducto:
        print("este producto ya esta registrado")
        producto["cantidad"] = producto.get('cantidad') + cantidadproducto


print(listaproductos)