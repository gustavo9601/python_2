import time

# objeto iterable
lista1 = [1, 2, 3, 4]
# crea el iterador
iterador = iter(lista1)
iterador
# next en cada llamada va a retornar una posicion del iterador
next(iterador)
next(iterador)
next(iterador)
next(iterador)
# si llega a haber un next y no hay mas datos, se retorna la expecion de StopIteration


"""Propio iterador
Permitira recorrer una lista y retornar las posiciones pares de la lista
"""


class Iterator:

    def __init__(self, data):
        self.data = data
        self.indice = 0

    # lo llama como un for
    # genera el objeto iterable, para este caso retorna la instancia de self
    def __iter__(self):
        return self

    # recorre todos los elementos, y lanza una exepcion de stopiteration cuandno no hay mas elementos
    def __next__(self):
        if self.indice >= len(self.data):
            raise StopIteration
        elem = self.data[self.indice]
        self.indice += 2
        return elem


it1 = Iterator([])
for e in it1:
    print(e)

it2 = Iterator([1, 2, 3, 4, 5, 6])
for e in it2:
    print(e)

print('*' * 30)

# Fibonnaci
# Suma de los dos numeros anteriores
class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux


print('*' * 30)


class SumaDos:

    def __init__(self, datos):
        self.datos = datos
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.datos):
            raise StopIteration
        elemento = self.datos[self.indice] + 2
        self.indice += 1
        return elemento


print(list(SumaDos([1, 2, 3, 4, 5])))
