alimenticios=[]
aseo=[]
licores=[]
general=[]
tupla=()

busquedae= False

print("Bienvenido al software del supermercado, antes de iniciar agrege sus produtos de acuerdo a las solicitudes inciales")
for i in range(1,8):
    nuevo=input(f"Ingrese el nombre del nuevo producto alimenticio {i} ")
    alimenticios.append(nuevo)
for i in range(1,6):
    nuevo=input(f"Ingrese el nombre del nuevo producto de aseo {i} ")
    aseo.append(nuevo)
for i in range(1,5):
    nuevo=input(f"Ingrese el nombre del nuevo producto de licor {i} ")
    licores.append(nuevo)
while True:
    general=alimenticios+aseo+licores
    menuinicial=int(input("Seleccione alguna de las siguientes opciones:\n1.Agregar un nuevo producto\n2.Ver lista general de productos\n3.Busca algun producto\n4.Eliminar un producto\n5.Generar copia de seguridad de todos los productos\n6.Ver copia de seguridad\n7.Salir "))
    if menuinicial==1:
        opcion = int(input("Que tipo de producto desea almacenar:\n1.Producto alimenticio\n2.Producto de aseo\n3.Producto de licoreria "))
        if opcion==1:
            nuevo=input("Ingrese el nombre del nuevo producto ")
            alimenticios.append(nuevo)
        elif opcion==2:
            nuevo=input("Ingrese el nombre del nuevo producto ")
            aseo.append(nuevo)
        elif opcion==3:
            nuevo=input("Ingrese el nombre del nuevo producto ")
            licores.append(nuevo)
        else:
            print("No selecciono una opción valida")
    elif menuinicial==2:
        if len(general)==0:
            print("No cuenta con productos registrados")
        else:
            print(f"Lista general\n{general}\nLista de productos alimenticios\n{alimenticios}\nLista de productos de aseo\n{aseo}\nLista de licores\n{licores}\n")
    elif menuinicial ==3:
        busqueda = input("Ingrese el producto que desea buscar ")
        Existe=(busqueda in general)
        if (busqueda in alimenticios)==True:
            print("El producto existe y esta registrado en la lista alimenticios\n")
            print(alimenticios)
        elif(busqueda in aseo)==True:
            print("El producto existe y esta registrado en la lista aseo\n",aseo)
            print(aseo)
        elif(busqueda in licores)==True:
            print("El producto existe y esta registrado en la lista de licores\n",licores)
            print(licores)
        else:
            print("No fue encontrado ese producto")
    elif menuinicial==4:
        eliminar = input("Ingrese el nombre del producto que desea eliminar ")
        busqueda=(eliminar in general)
        if busqueda == True:
            general.remove(eliminar)
            if (eliminar in alimenticios)==True:  
                alimenticios.remove(eliminar)
                print("El producto ha sido eliminado de la lista general y de los productos alimenticios")
                print(general)
            elif(eliminar in aseo)==True:
                aseo.remove(eliminar)
                print("El producto ha sido eliminado de la lista general y de los productos de aseo")
                print(general)
            else:
                licores.remove(eliminar)
                print("El producto ha sido eliminado de la lista general y de los licores")
                print(general)
        else:
            print("El producto indicado para eliminar no existe")
    elif menuinicial==5:
        tupla=tuple(general)
        print(tupla)
    elif menuinicial==6:
        print(tupla)
    elif menuinicial==7:
        print("Gracias por usar nuestros servicios")
        break

    else:
        print("Seleccione una opción valida")
    