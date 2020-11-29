from collections import Counter

#Counter retorna un diccionario con los elementos de objeto , string, agrupando y contando sus valores
lista1 = [1,2,3,1,2,3,1,23,45,6,4879,123,1,2,3]

contador_lista1 = Counter(lista1)
print("contador_lista1 => ", contador_lista1)
# Genera un diccionario, donde cada lettra de la palabra es el indice, y como valor devuelve la cantidad de ocurriencias
print("Counter('Hola Mundo') => ", Counter("Hola Mundoa"))

# Saber elementos comunes en la agrupacion
print("contador_lista1.most_common(1) => ", contador_lista1.most_common(1)) # pasando n retorna el numero de elementos a buscar en comun


# Libreria que permite generar indices por default al acceder a posiciones inexistentes de un ject
from collections import defaultdict

d = defaultdict(float)  # se pasa el tipo de dato que generara por defecto si no encuentra el indice
d['algo']
print("d['algo']", d['algo'])

# Libreria que permite ordenar a un diccionario en el orden de pusheo de elementos
from collections import OrderedDict
diccionario_ordenado = OrderedDict()
diccionario_ordenado['uno'] = 'ONE'
diccionario_ordenado['dos'] = 'TWO'
print("diccionario_ordenado", diccionario_ordenado)
