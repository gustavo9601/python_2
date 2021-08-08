from datetime import datetime
"""
Decoradores: (Un clousere espcial)
Son wrapper que empaquetan una funcion, y que a su ves reciben esa funcion como parametro
Permite ejecutar al inicio y al fin cierta logica, como exteneder la funcionalidad
"""


def decorador(func):
    # print(type(func))
    def envoltura():
        print('Añade al inicio')
        func()
        print('Añade al final')

    return envoltura

@decorador
def saludo():
    print('Holaaa!')

saludo()
print("*" * 30)


def mayusculas(func):
    def envoltura(text):
        return func(text).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, ahora en Mayus"

print(mensaje('Gustavo'))
print("*" * 30)


def execution_time(func):
    # Envoltura
    # *args, **kwargs // se pueden enviar o no argumentos posionales o de llave
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        # .total_seconds()  // func of datetime to get the seconds from a diff dates
        seconds_elapsed = (final_time - initial_time).total_seconds()
        print(f"Pasaron {seconds_elapsed} segundos.")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,10000000):
        pass

@execution_time
def random_sum(a, b):
    return a + b

random_func()
random_sum(1,2)

print("*" * 30)

def smart_division(div_funcion):
    def div(a, b):
        if b == 0:
            print("No se puede divir por cero*")
            return
        return div_funcion(a, b)

    return div


# @name of function decorador
@smart_division
def division(a, b):
    return a / b


print("division(10, 5)", division(10, 5))
print("division(2, 0)", division(2, 0))


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


print("*" * 30)
print(f"division_2(50,2): {division_2(50, 0)}")
