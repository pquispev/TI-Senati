## Los importantes metodos de String
y = " This is lazy\t\n "

print(y.strip())
# Remueve espacios en blanco: 'This is lazy'

print("DrDre".lower())
# convierte el String a minuscula: 'drdre'

print("attention".upper())
# convierte el String a mayuscula: 'ATTENTION'


print("smartphone".startswith("smart"))
# Compara que inicie con smart el string smartphone: True

print("smartphone".endswith("phone"))
# Compara que el string smartphone termine en phone: True

print("another".find("other"))
# Compara si el string another contine other y enque indice inicia: 2


print("cheat".replace("ch", "m"))
# Reemplaza ch por m en el string cheat: meat


print(','.join(["F", "B", "I"]))
# Une todos los elementos F B I  agregando una coma por elemento: F,B,I

print(len("Rumpelstiltskin"))
# Cuenta la cantidad de letras: 15

print("ear" in "earth")
# Verifica si el string ear esta dentro de earth: True


print("senati".capitalize())
# Convierte la primera letra en Mayuscula: Senati