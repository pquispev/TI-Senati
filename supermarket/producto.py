def agregarproductos(lista_productos):
    producto = {
        "nombre": "", 
        "marca": "",
        "costo": 0,
        "cantidad": 0,
    }
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
            pregunta = str(input("Desea agrear mas Productos? SI/NO"))
            if pregunta.upper() != "SI":
                flag = False
    
    return lista_productos


def listarproducto(lista_productos):
    contador = 0
    print('N  Producto | Marca | Precio | Cantidad')
    for producto in lista_productos:
        contador+=1
        print(f"{contador}. {producto.get('nombre')}|{producto.get('marca')}|{producto.get('costo')}| {producto.get('cantidad')}  ")
