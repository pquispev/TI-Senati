# Pedir por consola N cantidad nombres
# Verificar que ningun nombre se repita
# Cada nombre debe tener la primera letra en mayuscula
# La salida por consola debe ser la siguiente:

# ['Juan', 'Ana']
# se ingreso 2 nombres

# Juan numero de letras 4
# Ana numero de letras 3
def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonantes=0
    n = n.lower()
    for letra in n:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u": 
            cantidad_vocales += 1
        else:
            cantidad_consonantes += 1
    r = f"""Nombre: {n.capitalize()} 
            Numero de vocales: {cantidad_vocales}
            Numero de consonantes: { cantidad_consonantes}
            Numero de letras:  { len(n)}"""
    return r


lista_nombres = []
flag=True
while flag:
    nombres = input("Ingrese nombre o para terminar escriba x: ")
    if nombres == "x":
        flag=False
    else:
        cnombre = nombres.capitalize()
        if cnombre in lista_nombres:
            pass
        else:
            lista_nombres.append(cnombre)

lista_nombres.sort()
print(lista_nombres)
print(f"la cantidad de nombres son {len(lista_nombres)}")


for i in lista_nombres:
    print(cant_vc(i))















# Expansion de ejercicio
# Contar el numero de vocales y consonantes
# Ordenar la lista alfabeticamente
# Convertir todo el ejercicio en funcion
# La salida por consola debe ser la siguiente:


# ['Ana', Juan']
# se ingreso 2 nombres y estan ordenandos

# Nombre: Ana 
# Numero de vocales: 2
# Numero de consonantes: 1
# Numero de letras: 3

# Nombre: Juan
# Numero de vocales: 2
# Numero de consonantes: 2
# Numero de letras: 4
