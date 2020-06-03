from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas


def menu():
    print("*** Peliculas Gus ****")
    opcion = 0
    while opcion != 4:
        opcion = int(input("""Seleccione una de las siguientes opciones por favor:
               1. Agregar pelicula
               2. Listar peliculas
               3. Eliminar catalogo de peliculas
               4. Salir
           """))

        if opcion == 1:
            nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
            CatalogoPeliculas.agregar_pelicula(Pelicula(nombre_pelicula))
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar()
        elif opcion == 4:
            print("Gracias por usar **Peliculas Gus**")
        else:
            print("Opcion invalida")

menu()