from producto import Producto, input_int


prueba = Producto("LAPTOP X", "ASUS", 10000, 10)
prueba2 = Producto("LAPTOP Y", "HP", 10000, 10)
lista_productos = []
lista_productos.append(prueba)
lista_productos.append(prueba2)

def comparar_producto(np, mp, list_product):
    existe = False
    for p in list_product:
        if np.upper() == p.get_nombre().upper() and mp.upper() == p.get_marca().upper():
            print("el producto ya existe")
            existe = True
        else:
            print("agregando producto")
    return existe

def crear_producto(list_product):
    nombre_p = input("Nombre del producto: ")
    marca_p = input("Marca del producto: ")
    precio_p = input_int("Precio del producto: ", "no ingresaste bien el precio")
    cantidad_p = input_int("Cantidad del producto: ", "no ingresaste bien la cantidad")

    existencia = comparar_producto(nombre_p, marca_p, lista_productos)
    if not existencia:
        nuevo_producto = Producto(nombre_p, marca_p, precio_p, cantidad_p)
        list_product.append(nuevo_producto)

# crear_producto(lista_productos)
# print(lista_productos)
def lista_producto(list_product):
    c = 0
    for p in list_product:
        c += 1
        print(f"{c}. {p.get_info_completa()} ")
lista_producto(lista_productos)