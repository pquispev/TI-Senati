

def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonantes=0
    
    for letra in n:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u": 
            cantidad_vocales += 1
        else:
            cantidad_consonantes += 1
    r = f"""Nombre: {n} 
            Numero de vocales: {cantidad_vocales}
            Numero de consonantes: { cantidad_consonantes}
            Numero de letras:  { len(n)}"""
    return r
print(cant_vc('juan'))