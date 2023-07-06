flag=True
while flag: #esto da vueltas
    try: #captura errores
        #parte1 que si todo sale bien
        numero = int(input('Ingrese solo numeros: '))
        print(numero)
    except ValueError as e:
        #que si en la parte1 hubo un error imprime esto de aqui
        print("usted escribio una letra")
    
bandera=True
suma=0
while bandera:
    if suma==10:
        bandera=False
    print(suma)
    suma+=1
