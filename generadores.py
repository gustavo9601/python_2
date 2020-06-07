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