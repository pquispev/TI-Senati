def crearproductos(lista_productos):
    producto = {}
    flag=True
    while flag:
        try: 
            nombreproducto = input("Nombre del producto: ")
            marcaproducto = input("Marca del producto: ")
            costoproducto = numerosdenetrada("Costo del producto: ")
            cantidadproducto = numerosdenetrada("Cantidad del producto: ")
        except ValueError:
            print("ALGO SALIO MAL INTENTALO OTRA VEZ")
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]= costoproducto
            producto["cantidad"]= cantidadproducto
            flag_repeticion = coincidenciaproducto(nombreproducto, cantidadproducto, lista_productos)
            if not flag_repeticion:
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

def numerosdenetrada(mensaje): 
    while True:
        try:
            numero_ingreso = int(input(mensaje))
        except ValueError:
            print("te equivocaste esto debe ser un numero")
        else:
            break
    return numero_ingreso

numerosdenetrada("dsfsdfsdfsfsdfsd")

def coincidenciaproducto(nombreproducto, cantidadproducto, lista_productos):
    flag = False
    for producto in lista_productos:
        if producto.get("nombre") == nombreproducto:
            print("este producto ya esta registrado")
            producto["cantidad"] = producto.get('cantidad') + cantidadproducto
            flag = True
    return flag