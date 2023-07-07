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
# Glues together all elements in the list using the separator string: F,B,I

print(len("Rumpelstiltskin"))
# String length: 15
print("ear" in "earth")
# Contains: True