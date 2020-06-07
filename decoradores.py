"""
Decoradores:
Son wrapper que enpaquetan una funcion, y que su ves reciben esa funcion como parametro
Permite ejecutar al inicio y al fin cierta logica
"""


def smart_division(div_funcion):
    def div(a, b):
        if b == 0:
            print("No se puede divir por cero*")
            return
        return div_funcion(a, b)

    return div


@smart_division
def division(a, b):
    return a / b


print(division(10, 5))
print(division(2, 0))


def log(funcion):
    def wrap(*args, **kwargs):
        print(f"Ejecutando la funcion {funcion.__name__} con los argumentos: {', '.join([str(args)])}")
        return funcion(*args, **kwargs)

    return wrap


@log
def suma(a, b):
    return a + b


print(f"suma(10,100) : {suma(10, 100)}")


# Se puede decorar una funcion con varios decoradores

@log
@smart_division
def division_2(a, b):
    return a / b

print("**************************************")
print(f"division_2(50,2): {division_2(50, 0)}")
