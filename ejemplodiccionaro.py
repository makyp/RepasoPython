#Recorrer un diccionario
diccionario ={ "Pedro":33, "Juan":6546, "Sandra": 20, "Milena": 19}
for i in diccionario:
    print(f"{i} -> {diccionario[i]}")

for clave, valor in diccionario.items():
    print(f"{clave} -> {valor}")