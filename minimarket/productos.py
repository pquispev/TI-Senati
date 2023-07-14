def crearproductos(lista_productos):
    producto = {}
    flag=True
    while flag:
        try: 
            nombreproducto = input("Nombre del producto: ")
            marcaproducto = input("Marca del producto: ")
            costoproducto = int(input("Costo del producto: "))
            cantidadproducto = int(input("Cantidad del producto: "))
        except ValueError:
            print("ALGO SALIO MAL INTENTALO OTRA VEZ")
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]= costoproducto
            producto["cantidad"]= cantidadproducto
            lista_productos.append(producto)
            producto = {}
            pregunta = input("Desea agrear mas Productos? SI/NO")
            if str(pregunta) != "SI":
                flag = False

    return lista_productos


def listarproductos(lista_productos):
    print('Producto | Cantidad | Precio')
    for producto in lista_productos:
        print(f"{producto.get('nombre')} | {producto.get('cantidad')} | {producto.get('costo')}")

