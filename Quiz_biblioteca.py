''''
Integrantes: 
Daniela Sofia Gamboa Torres
Angie Juliana Rojas Montaño
Maira Tatiana Quiroga Peralta

Enunciado: 
La biblioteca Edu necesita llevar un control de los libros, puesto que al hacer el inventario se evidenció que hacen falta algunos de ellos. Se necesita un programa que permita registrar los libros, buscar los autores por el nombre del libro, crear una copia de seguridad de todos los libros, eliminar el libro que desee (ya sea porque se equivocó en algo que agregó), añadir un nuevo libro, visualizar todos los libros, obtener el total de libros que hay, mostrar los libros que se encuentran en alguna letra del abecedario y cuantos libros tiene un autor en especifíco'''
biblioteca = {}#diccionario
copia_seguridad = []#lista
copiafinal=()
autoreslibros = []

while True:
    libro = input("Ingrese el nombre del libro: ").lower()
    autor = input("Ingrese el autor del libro: ").lower()
    autoreslibros.append(autor)
    letrainicial = libro[0]
    if letrainicial not in biblioteca:
        biblioteca[letrainicial] = {}
    biblioteca[letrainicial][libro] = autor
    continuar = input("¿Desea agregar otro libro? (s/oprima cualquier otra tecla): ")
    if continuar.lower() != 's':
        break

while True:
    opcion = int(input("Selecciona la acción que deseas realizar: \n1. Mostrar los libros existentes\n2. Mostrar los autores disponibles\n3. Buscar los libros por el autor\n4. Total de libros agregados\n5. Eliminar un libro\n6. Generar Copia de seguridad de los libros\n7. Ver Copia de Seguridad\n8. Añadir otro libro\n9. Mostrar libros por letra\n10. Buscar cuantos libros tengo de un autor\n11. Salir\n"))
    
    if opcion == 1:
        print("\n--- Software bibliotecario ---")
        for letrainicial, libros in biblioteca.items():
            print(letrainicial)
            for libro, autor in libros.items():
                print(f"Libro: {libro}, Autor: {autor}")
    
    elif opcion == 2:
        print("\n--- Autores disponibles en la biblioteca ---")
        autores = set() #Elimina duplicados de una lista antes de imprimirlos
        for libros in biblioteca.values():
            for autor in libros.values():
                autores.add(autor)
        for autor in autores:
            print(autor)
    
    elif opcion == 3:
        BuscaAutor = input("\nIngrese el nombre del autor para consultar sus libros: ")
        found = False
        for letrainicial, libros in biblioteca.items():
            for libro, autor in libros.items():
                if autor.lower() == BuscaAutor.lower():
                    print(f"Libro: {libro}, Autor: {autor}")
                    found = True
        if not found:
            print("No se encontraron libros para ese autor.")
    
    elif opcion == 4:
        total_libros = sum(len(libros) for libros in biblioteca.values())
        print(f"\nTotal de libros registrados en la biblioteca: {total_libros}")
    
    elif opcion == 5:
        libro_eliminar = input("Ingrese el nombre del libro que desea eliminar: ").lower()
        for letrainicial in biblioteca:
            if libro_eliminar in biblioteca[letrainicial]:
                del biblioteca[letrainicial][libro_eliminar]
                break
        else:
            print("El libro no se encuentra en la biblioteca.")
    
    elif opcion == 6:
        print("\nCopia de Seguridad de los libros:")
        copia_seguridad.append([f"Libro: {libro}, Autor: {autor}" 
            for libros in biblioteca.values() 
            for libro, autor in libros.items()])
        print(copia_seguridad.sort(reverse=True))
    elif opcion == 7:
        copiafinal=tuple(copia_seguridad)
        if len(copiafinal)>0:
            print(copiafinal)
        else:
            print("No se cuenta actualemtente con una copia de seguridad")
    elif opcion == 8:
        libro = input("Ingrese el nombre del libro: ").lower()
        letrainicial = libro[0]
        if letrainicial not in biblioteca:
            biblioteca[letrainicial] = {}
        autor = input("Ingrese el autor del libro: ")
        biblioteca[letrainicial][libro] = autor
    
    elif opcion == 9:
        letra = input("Ingrese la letra de los libros que desea consultar: ")
        if letra.lower() not in biblioteca:
            print("No tenemos libros con esa letra.")
        else:
            for inicial, libros in biblioteca.items():
                if inicial.lower() == letra.lower():  # Buscamos coincidencia de letras
                    for libro, autor in libros.items():
                        print(f"Libro: {libro}, Autor: {autor}")
    elif opcion==10:        
        autorabuscar=input("Ingrese el nombre del autor").lower()
        numeroDeLibros = autoreslibros.count(autorabuscar)
        if numeroDeLibros>0:
            print(f"El autor {autorabuscar} cuenta con {numeroDeLibros} en la biblioteca")
        else:
            print(f"No se cuenta con libros del autor {autorabuscar} en la biblioteca")
    elif opcion==11:        
        print("Saliendo del programa.")
        break
    else:
        print("Seleccione una opción válida.")

