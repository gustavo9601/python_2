# doc_test permite en los mismos docstring realizar una prueba unitaria
# >>> funcion(parametros_raw)
# valor que debe retornar
# enter

# desde la termina se puede ejecutar el archivo con el comando
# py archivo.py -v
# si no se pasa el -v simplemente si pasa todos los test no muestra nada

"""
    Se le especifica en mulitplinea que lo que recibira como respuesta
    sera una exepcion que empien Tracebac.. y termina en Type...
    y con los ... en la mitad simboliza que hay continuidad de algun texto
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""


def suma(a, b):
    """
    Funcion suma(a,b) recibe 2 params y retorna la suma

    >>> suma(5,10)
    15

    >>> suma(10,10)
    21

    >>> suma(10, 'hola')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


def palindromo(palabra):
    """
    Funcion palindromo(paralbra) recibe un string y valida si es palindromo

    >>> palindromo("oso")
    True

    >>> palindromo("camaleon")
    False

    """
    if palabra.lower() == palabra[::-1].lower():
        return True
    else:
        return False


def doblar_lista(lista):
    """
    Funcion doblar_lista([]) recibe una lista numerica y la dobla sus valores

    >>> l1 = [1,2,3,4,5]
    >>> doblar_lista(l1)
    [2, 4, 6, 8, 10]

    """
    return [n * 2 for n in lista]


if __name__ == '__main__':
    # se debe importar la libreria para ser capas de ejecutar las pruebas
    import doctest

    doctest.testmod()
