"""
Un generador es una forma de generar iteradores
Va produciendo una secuencia de valores
usa yield para retornar el valor y continuar la iteracion
"""


def fisrt_1000():
    "Genera los primeros 1000 numeros"
    for x in range(1000):
        yield x


for valor in fisrt_1000():
    print(valor)


def numeros_pares(n):
    # Se puede usar comprenhension entre ()  y no [] como una lista
    return (x for x in range(n) if x % 2 == 0)


gen = numeros_pares(15)

print(gen.__next__())

print(gen.__next__())

# // misma fuincionaclidad de variable_generador.__next__()
# next(variable_generador)

# parseando de lista normal a un objeto iterador
lista_normal = [x for x in range(1, 10)]
lista_normal_a_iterador = iter(lista_normal)
print("next(lista_normal_a_iterador)", next(lista_normal_a_iterador))

"""
Funciones recursivas
//se llaman asi misma la funcion 
"""


def cuenta_regresiva(minutos):
    minutos -= 1
    # importante que siempre halla una condicion que controle que no sea infinita
    if minutos > 0:
        print("minuto", minutos)
        cuenta_regresiva(minutos)
    else:
        print("Boom exploto la funcion")


print("Funciones recursivas")
cuenta_regresiva(100)


def factorial(num):
    print("Valor inicial ->", num)
    if num > 1:
        # se hace recursiva la funcion
        num = num * factorial(num - 1)
    # Devuelve el valor total
    print("Valor final ->", num)
    return num


print("Funcion factorial", factorial(10))
