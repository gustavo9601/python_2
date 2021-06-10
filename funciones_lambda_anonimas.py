from functools import reduce

# lamda parametros: valor a retornar
# son utililes para usarlas pasadas como parametros

# lambda parámetros: expresión

sumatoria = lambda x: x + 1

print("lambda x: x + 1 => ", str(sumatoria(1)))

# lamda con varios parametros
prod = lambda x, y: x * y
print("prod > ", prod(1, 2))

# Se corresponde a la ecuación x^2 + 2x + 1 = 0, cuya única solución es x = -1
discriminante = lambda a, b, c: b ** 2 - 4 * a * c
print("discriminante > ", discriminante(1, 5, 1))

# retornando una tupla
double_square = lambda x: (x, 2 * x, x ** 2)
print("double_square > ", double_square(2))

numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

# map // allow to execute a function for each iteration of the list and return a new value
# list // convert to list
averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

celsius = [0, 5, 30, 40]
celsius_to_farenheit = list(map(lambda x: (x * 9 / 5) + 32, celsius))
print("celsius_to_farenheit > ", celsius_to_farenheit)

# filter // allow execute a function for each iteration and return if met the condition
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
short_cities = list(filter(lambda city: len(city) < 10, cities))
print(short_cities)

"""
La función reduce()
Aplica continuamente una misma función a los elementos de un objeto iterable

Aplica la función a los primeros dos elementos
Aplica la función al resultado del paso anterior y el tercer elemento
Aplica la función al resultado del paso anterior y el cuarto elemento
Sigue así hasta que solo queda un elemento
Devuelve el valor resultante
"""

nums = [1, 2, 3, 4, 5, 6]
print("reduce > ", reduce(lambda x, y: x * y, nums))

"""
La función sorted()
Ordena los elementos del objeto iterable que indiquemos de acuerdo a la función que pasemos por parámetro
Como output, devuelve una permutación del objeto iterable ordenado según la función indicada
"""
words = ["zapato", "amigo", "yoyo", "barcossssssssssssss", "xilófono", "césped"]
# key=recibe la funcion a evaluar por cada iteracion que indicara el orden
words_sorted = sorted(words, key=len, reverse=True)
print("words_sorted > ", words_sorted)
