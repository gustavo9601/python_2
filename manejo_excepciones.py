"""
Para capturar el error y controlarlo
se usa try y except
"""

try:
    10 / 0
    # Exception es la execpcion mas generica
except Exception as e:
    print("Ocurrio un error y el detalle es => ", e)
    print("type(e)", type(e))

try:
    "1" / 2
    # ZeroDivisionError, TypeError diferentes tipos de exepciones, que permiten controlar de forma diferente la secuencia del error
    # se pueden por n tipos de except, hasta que se verifique todos los posibles errores
except ZeroDivisionError as e:
    print("ZeroDivisionError y el detalle es => ", e)
    print("type(e)", type(e))
except TypeError as e:
    print("TypeError y el detalle es => ", e)
    print("type(e)", type(e))
except Exception as e:
    print("Ocurrio un error y el detalle es => ", e)
    print("type(e)", type(e))
# else permite ejecutar codigo si no hubo ninguna exepcion en la ejecucion
else:
    print("No hubo ningun error")
finally:
    # finally se ejecutara si hubo o no errores de ejecucion
    print("Fatalityyyy")

"""
Creando propias excepciones
"""


# Se crea una clase que herede de Excepction
class NumerosIgualesExepcion(Exception):
    def __init__(self, mensaje):
        #message se hereda de la clase exception
        self.message = mensaje

try:
    val1 = int(input("Digite valor 1:\n"))
    val2 = int(input("Digite valor 1:\n"))

    # validacion simple si son iguales
    if val1 == val2:
        # lanza la expecion personalizada
        raise NumerosIgualesExepcion("Los numeros son iguales")

except Exception as e:
    print("Error =>", e)
