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
            flag_repeticion = coincidenciaproducto(nombreproducto,marcaproducto, cantidadproducto, lista_productos)
            if not flag_repeticion:
                lista_productos.append(producto)
            producto = {}
            pregunta = input("Desea agrear mas Productos? SI/NO")
            if str(pregunta) != "SI":
                flag = False

    return lista_productos


def listarproductos(lista_productos):
    print('N° | Producto | Cantidad | Precio')
    counter = 0
    for producto in lista_productos:
        counter += 1
        print(f"{counter} |{producto.get('nombre')} | {producto.get('cantidad')} | {producto.get('costo')}")

def numerosdenetrada(mensaje): 
    while True:
        try:
            numero_ingreso = int(input(mensaje))
        except ValueError:
            print("te equivocaste esto debe ser un numero")
        else:
            break
    return numero_ingreso


def coincidenciaproducto(nombreproducto, marcaproducto, cantidadproducto, lista_productos):
    flag = False
    for producto in lista_productos:
        if producto.get("nombre") == nombreproducto and producto.get("marca") == marcaproducto:
            print("este producto ya esta registrado")
            producto["cantidad"] = producto.get('cantidad') + cantidadproducto
            flag = True
    return flag


def ventaproductos(lista_de_productos):
    lista_venta = []
    producto_venta = {}
    listarproductos(lista_de_productos)
    flag=True
    while flag:
        try:
            seleccionproducto = int(input('elija el numero del producto: '))
            producto = lista_de_productos[seleccionproducto-1]
            cantidadproducto = int(input(f'Escriba cantidad de {producto.get("nombre")}: '))
        except ValueError:
            print('algo salio mal')
        else:
        
            producto["cantidad"] = producto.get("cantidad") - cantidadproducto
            producto_venta["producto"] = producto.get("nombre")
            producto_venta["cantidad"] = cantidadproducto
            producto_venta["subtotal"] = cantidadproducto * producto.get("costo")
            lista_venta.append(producto_venta)
            listarproductos(lista_de_productos)
            producto_venta = {}
            print(lista_venta)
            pregunta = str(input("Desea vender otro Producto? SI/NO"))
            if (pregunta).upper == "NO":
                flag = False