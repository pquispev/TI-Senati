

flag=True
while flag: #esto da vueltas
    try: #captura errores
        #parte1 que si todo sale bien
        numero = int(input('Ingrese solo numeros: '))
        print(numero)
        flag=False
    except ValueError as e:
        #que si en la parte1 hubo un error imprime esto de aqui
        print("usted escribio una letra")
