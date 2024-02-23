#Crear un diccionario de agenda telefonica que almacene los nombres y los numero de telefono hasta que el usuario lo desee
#Mostrar los datos
#Mostrar los numeros de telefono
#Permitir la consulata de los numeros por el nombre
#Obtener el total de personas registradas
#Puede ingrar los contactos que quiera
agenda_telefonica = {}

while True:
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    
    agenda_telefonica[nombre] = telefono
    
    continuar = input("¿Desea agregar otro contacto? (s/n): ")
    if continuar.lower() != 's':
        break
while True: 
    opcion = int(input("Selecciona la acción que deseas realizar: \n1.Mostrar los datos\n2.Mostrar los numeros de telefono\n3.Consulta los numeros por el nombre\n4. Total de personas registradas\n5.Eliminar un contacto\n6.Copia de seguridad de los contactos\n7.Salir "))
    if opcion ==1:
        print("\n--- Datos en la agenda telefónica ---")
        for nombre, telefono in agenda_telefonica.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    elif opcion ==2:
        
        print("\n--- Números de teléfono en la agenda ---")
        for telefono in agenda_telefonica.values():
            print(telefono)
    elif opcion ==  3:
        buscar_nombre = input("\nIngrese el nombre del contacto para consultar su número de teléfono: ")
        if buscar_nombre in agenda_telefonica:
            print(f"El número de teléfono de {buscar_nombre} es: {agenda_telefonica[buscar_nombre]}")
        else:
            print("El nombre ingresado no está en la agenda telefónica.")
    elif opcion ==4:
        total_contactos = len(agenda_telefonica)
        print(f"\nTotal de personas registradas en la agenda telefónica: {total_contactos}")
    elif opcion==5:
        contacto_eliminar=input("Ingrese el nombre del contacto que desea eliminar")
        del(agenda_telefonica[contacto_eliminar])
        for nombre, telefono in agenda_telefonica.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    elif opcion==6:
        print("Copia de Seguridad de tus contactos")
        tupla=tuple(agenda_telefonica)
        print(tupla)
    elif opcion==7:
        print("Ha salido de contactos")
        break
    else:
        print("Seleccione una opción valida")