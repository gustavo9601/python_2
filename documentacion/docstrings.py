# dosctring
# """texto"""
# para ejecutar y ver la documentacion se engloba la funcion o el objeto dentro de la funcion help(objeto/funcion)

"""Documentacion del archivo o modulo"""

def hola():
    """Entre comillas pasamos la documentacion de la funcion"""
    print("Hello Wolrd")

class Clase:
    """Este es el docstring de la clase"""
    def __init__(self):
        """Este es el dosctring de la funcion"""
        self.nombre = 'Gus'
        pass

# help() funcion que imprime el docstring
help(hola)

objeto_clase = Clase()
help(objeto_clase)

# tambien para imprimir solo la documentacion del string
# modulo.__doc__    // cumple la misma funcion que el help