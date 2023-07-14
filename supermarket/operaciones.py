from producto import agregarproductos, listarproducto

def menu():
    omenu = """
    SUPERMARKET
    ___________________
    1.Listar productos
    2.Agregar productos
    3.Vender productos
    4.Salir
    """
    list_productos = []
    flag = True
    while flag:
        try:
            print(omenu)
            opcion = int(input("Elije la opcion: "))
        except ValueError:
            pass
        else:
            if opcion == 1:
                print("*Listando productos")
                if len(list_productos) == 0:
                    print("Agrega productos, regresando al menu principal")
                else:
                    listarproducto(list_productos)
            elif opcion == 2:
                print("*Agregando productos")
                list_productos = agregarproductos(list_productos)
            elif opcion == 4:
                flag = False
                print("*A salido del menu")
            else:
                print("No existe esta opcion agrega al menu")