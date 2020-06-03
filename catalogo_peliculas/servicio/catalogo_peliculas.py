import os


class CatalogoPeliculas:
    ruta_archivo = "C:\\xampp\\htdocs\\python\\python_2\\catalogo_peliculas\\db\\db_peliculas.txt"

    @staticmethod
    def agregar_pelicula(Pelicula):
        archivo_peliculas = open(CatalogoPeliculas.ruta_archivo, "a")
        archivo_peliculas.write(Pelicula.nombre + "\n")
        archivo_peliculas.close()

    @staticmethod
    def listar_peliculas():
        archivo_peliculas = None
        try:
            archivo_peliculas = open(CatalogoPeliculas.ruta_archivo, "r")
            for idx, pelicula in enumerate(archivo_peliculas):
                print(str(idx + 1) + ". " + pelicula)
        except FileNotFoundError as e:
            print("No ha sido creado el catalogo, por favor ingrese una pelicula")
        finally:
            archivo_peliculas.close()

    @staticmethod
    def eliminar():
        os.remove(CatalogoPeliculas.ruta_archivo)
        print("Catalogo eliminado...")
