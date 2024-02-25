''''
Integrantes: 
Daniela Sofia Gamboa Torres
Angie Juliana Rojas Montaño
Maira Tatiana Quiroga Peralta

Enunciado: 
Crear un sistema de gestión bibliotecaria en el cual se almacenen los libros en orden alfabetico relacionando el nombre del libro y el autor.
'''
biblioteca= {}
copia=()
while True:
    libro = input("Ingrese el nombre del libro: ").lower
    letrainicial = libro[0]
    letrainicial={}
    autor = input("Ingrese el autor del libro: ")
    biblioteca[letrainicial][libro]=autor
    continuar = input("¿Desea agregar otro libro? (s/n): ")
    if continuar.lower() != 's':
        break
while True: 
    opcion = int(input("Selecciona la acción que deseas realizar: \n1.Mostrar los libros existentes\n2.Mostrar los autores disponible\n3.Buscar los libros por el autor\n4. Total de libros agregados\n5.Eliminar un libro\n6.Copia de seguridad de los libros\n7.Añadir otro libro\n8. Salir"))
    if opcion ==1:
        print("\n--- Software bibliotecario ---")
        for letrainicial,libro, autor in biblioteca.items():
            print(f"Libro: {libro}, Autor: {autor}")
    elif opcion ==2:
        
        print("\n--- Autores disponibles en la biblioteca ---")
        for autor in biblioteca.values():
            print(autor)
    elif opcion ==  3:
        BuscaAutor = input("\nIngrese el nombre del libro para consultar su autor")
        if BuscaAutor in biblioteca:
            print(f"El nombre del libro es: {BuscaAutor}  y su autor es : {biblioteca[BuscaAutor]}")
        else:
            print("No se encuentra ese libro en la biblioteca")
    elif opcion ==4:
        total_libros = len(biblioteca)
        print(f"\nTotal de libros registrados en biblioteca es: {total_libros}")
    elif opcion==5:
        libro_eliminar=input("Ingrese el nombre del libro que desea eliminar")
        del(biblioteca[libro_eliminar])
        for libro, autor in biblioteca.items():
            print(f"Libro: {libro}, Autor: {autor}")
    elif opcion==6:
        print("Copia de Seguridad de tus contactos")
        copia=tuple(biblioteca)    
    elif opcion==7:
        print(copia)
    elif opcion==8:
        libro = input("Ingrese el nombre del libro: ").lower
        letrainicial = libro[0]
        letrainicial={}
        autor = input("Ingrese el autor del libro: ")
        biblioteca[letrainicial][libro]=autor
    elif opcion==9:
        letrabuscar=input("Ingrese la letra de los libros que desea buscar").lower
        print(f"Letra:{letrabuscar}")
    elif opcion==10:
        print("Ha salido")
        break
    else:
        print("Seleccione una opción valida")