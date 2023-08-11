from producto import Producto
from cliente import Cliente
from utilitarios import input_int

menu = """ CAFETIN SENATI 
    1. DESAYUNO
    2. ALMUERZO
    3. CENA
    4. EXTRAS
"""
jq = Producto("JUGO DE QUINUA", 2, 50)

# lista_cafetin = [
#     {"desayuno": [jq]},
#     {"almuerzo": []},
#     {"cena": []},
#     {"extras": []},
# ]

lista_productos = []
lista_almuerzos = []
# mi funcion crear_productos recibe como parametro
#  una lista de productos 
def crear_producto(list_product):
    nombre_p = input("Nombre del producto: ")
    precio_p = input_int("Precio del producto: ", "no ingresaste bien el precio")
    stock_p = input_int("Stock del producto: ", "no ingresaste bien el stock")
    item_p = Producto(nombre_p, precio_p, stock_p)
    list_product.append(item_p)

p = Producto("JUGO DE QUINUA", 2, 50)
c = Producto("PAN CON PALTA", 2, 50)
lista_productos.append(p)
lista_productos.append(c)


s = Producto("SECO DE POLLO", 7, 50)
b = Producto("CHIFA", 10, 50)
lista_almuerzos.append(s)
lista_almuerzos.append(b)


def listar_productos(list_product):
    contador = 0
    for item in list_product:
        contador += 1
        print(f"{contador}. {item.get_info_completa()}")

def vender_producto(product_selected, cantidad):
    product_selected.actualizar_stock(cantidad)

def ticket_venta(nombre_p, cantidad_p, sub_total,  client):
    t = f"""
    CAFETIN SENATI
    TICKET DE VENTA
    Cliente: { client }
    PRODUCTO     |  CANT. |  SUB.TOTAL
1. { nombre_p }   {cantidad_p}  {sub_total}
    
    """
    return t

def crear_cliente(list_client):
    nombre_c = input("Nombre del cliente: ")
    dni_c = input("DNI del cliente: ")
    cliente_c = Cliente(nombre_c, dni_c)
    list_client.append(cliente_c)

lista_clientes = []
print(menu)
opcion = input_int("Elija un opcion: ", "No existe esta opcion")
if opcion == 1:
    listar_productos(lista_productos)
    opcion_desayuno = input_int("Elija un desayuno: ", "No existe esta opcion")
    producto_seleccionado = lista_productos[opcion_desayuno - 1]
    pregunta = input_int("cual es la cantidad que desea: ", "No existe esta opcion")
    vender_producto(producto_seleccionado, pregunta)
    subtotal = producto_seleccionado.get_precio() * pregunta
    cliente = input("Digite el nombre del cliente: ")
    print(ticket_venta(producto_seleccionado.get_nombre(), pregunta, subtotal, cliente))
    
elif opcion == 2:
    listar_productos(lista_almuerzos)