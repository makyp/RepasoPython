'''
#Programa que pida un caracter e indique si es una vocal o no
letra = input("Ingrese una letra: ").lower()#lower convierte mayusculas en minusculas
if letra == "a" or letra == "e"  or letra == "i" or letra == "i" or letra == "o" or letra == "u":
    print("Es una vocal")
else:
    print("No es una vocal")
    
# Programa que simule un cajero automatico con un saldo inicial de 1000 y tendra el siguiente menu de opciones:

DineroInicial = 1000
Total = DineroInicial

while True:
    Opcion = int(input("Seleccione la acción que desea realizar.\n1. Ingresar dinero\n2. Retirar dinero de la cuenta\n3. Mostrar dinero disponible\n4. Salir\n"))
    
    if Opcion == 1:
        DineroVariable = int(input("Ingrese la cantidad de dinero que desea ingresar: "))
        Total += DineroVariable
        print("Deposito exitoso")
        
    elif Opcion == 2:
        DineroVariable = int(input("Ingrese la cantidad de dinero que desea retirar: "))
        if DineroVariable > Total:
            print("No es posible realizar ese retiro, saldo insuficiente")
        else:
            Total -= DineroVariable
            print(f"Retiro exitoso\nSu saldo actual es de {Total}")
            
    elif Opcion == 3:
        print(f"Su saldo actual es de {Total}")
        
    elif Opcion == 4:
        break
        
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
'''
# lista

lista =["lunes", "martes", "miercoles", "jueves", "viernes"]
print(lista[2])
print(lista[-4])
print(lista[0:3])#Sublista que toma desde una pocision hasta otra
print(lista[:4])#Sublista desde el valor inicial hasta donde lo defina
print(lista[:])#Muestra todos los datos
print(lista[1:3])
print(lista[3:])#Del 3 en adelante
print(len(lista))#Numero de elementos en una lista
lista.append(6)
lista.insert(2,3)
lista.extend([6,7,8])
lista.append(6)
print(len(lista))#Numero de elementos en una lista
print( ("lunes") in lista)

listanum=[1,2,3,4,5,6,7,8,9,10,13,2]
print(listanum.sort(reverse=True))#oden descendente
