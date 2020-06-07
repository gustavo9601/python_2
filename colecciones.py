nombres = ["Martha", "Gustavo", "Meliza", "Adolfo"]
print("nombres", nombres)

cantidad_nombres = len(nombres)
print("cantidad_nombres", cantidad_nombres)

print("nombres[1]", nombres[1])
print("nombres[1:]", nombres[1:])
print("nombres[:1]", nombres[:1])
print("nombres[-1]", nombres[-1])
print("nombres[0:2]", nombres[0:2])
print("nombres[::-1]", nombres[::-1])

# .index('Valor_buscar, posicion_inicial, posicion_final)  retorna la posicion del encontrado
print("nombres.index('Meliza')", nombres.index('Meliza'))

nombres.append("Rodolfo")  # inserta en la ultima posicion
nombres.insert(2, "Cecilia")  # inserta en la posicion indicada
nombres.insert(-2, "Nombre hacia atras")  # si el idice es negativo, empieza hacia atras
print("nombres.append() and nombres.insert()", nombres)

nombres.remove("Gustavo")  # elimina el primer encontrado, elemento proporcionado por parametro
print("nombres.remove()", nombres)

nombres.pop()  # elimina el ultimo elemento de la lista
print("nombres.pop()", nombres)
nombres.pop(3)  # pasando el indice como parametro elimina el elemento
print("nombres.pop(3)", nombres)

del nombres[2]  # elimina el indice indicado
print("del nombre[]", nombres)

nombres.clear()  # vacia los elementos de la lista
print("nombres.clear()", nombres)

# elimina la variable de memoria
del nombres

# .sort(reverse=True)  ordena una lista de numeros
lista_numeros = [20, 20, 5, 6, 100, 20000]
lista_numeros.sort()
print("lista_numeros.sort()", lista_numeros)

# .sort(funcion comprenhension que retorna un iterable)
lista_pares_numeros = [(6, 2), (1, 5), (2, 3), (4, 1), (5, 2), (1, 3)]
lista_pares_numeros.sort(key=lambda x: x[0] + x[1])
print("lista_pares_numeros.sort(key=lambda x: x[0] + x[1])", lista_pares_numeros)

# -reverse() revierte el orden a su estado normal
lista_numeros.reverse()

# sorted(objeto_iterable, reverse=True)  # permite ordenar cualquier tipo de dato de un objeto iterable
lista_paises = ['colombia', 'brasil', 'argentica', 'canada']
lista_paises = sorted(lista_paises)
print("sorted(lista_paises)", lista_paises)

# Ejericio numeros divisbles por 3
for valor in range(0, 11):
    if valor % 3 == 0:
        print("valor divisible por 3", valor)

# Listas como colas
# primero en entrar primero en salir, al ingresar los elementos se van encolado y van saliendo en orden de llegada

queue = [1, 2, 3]

queue.append(44)
queue.append(45)
print("queue.append", queue)

queue.pop(0)  # eliminamos la primer posicion
print("queue.pop", queue)

# usando la libreria de colas de PY
from collections import deque

# usando deque hace eficiente la cola
queue = deque([1, 2, 3, 4])

queue.append(50)
queue.append(100)
# .popleft() saca el primer elemento
queue.popleft()
print("queue.popleft()", queue)

"""
Listas por comprenhension
# permiten iterar dentro de una lista u tener logica, y para cada iteracion retornara el valor
"""

cuadrados_2 = [x ** 2 for x in range(10)]  # para cada iteracion del for  x se mutipliacara * 2 y retornara el valor
print("cuadrados_2 comprenhension", cuadrados_2)

# usando map   // map retorna un generador y con list lo parsea a lista
cuadrados_3 = list(map(lambda x: x ** 2, range(10)))
print("cuadrados_3 map", cuadrados_3)

# usando comprenhencion con una condicion en la funcion
lista_enteros = [-2, 5, 10, -5, -500, 1, 3, -90]
lista_enteros_positivos = [x for x in lista_enteros if x >= 0]
print("lista_enteros_positivos", lista_enteros_positivos)
# usando funcion filter para ejecutar la condicion
lista_enteros_negativos = list(
    filter(lambda x: x < 0, lista_enteros))  # // filter(lambda variable_temporal: condicion, objeto_iterable)
print("lista_enteros_negativos", lista_enteros_negativos)

# Retornando una pareja de valores numero y su cuadrado
# //[(valor, valor_operacion) for valor in lista_iterable]
pares_cuadrados_10 = [(x, x ** 2) for x in range(1, 11)]
print("pares_cuadrados_10", pares_cuadrados_10)

# lista de valores en pareja, combinados
lista_pares_combinados = [(x, y) for x in [100, 200, 300] for y in [1000, 2000, 3000] if x != y]
print("lista_pares_combinados", lista_pares_combinados)

# Iterar sobre dos o mas secuencias al mismo tiempo
# zip(n_cantidad_objetos_iterables) permite ser recorrido al tiempo n_cantidad_iterables siempre con la misma cantidad de posicions
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
    print(p, r)

"""
Tuplas
"""
frutas = ("pera", "banano", "papaya", "coco")
print("frutas", frutas)
print("frutas[0:1]", frutas[0:2])
frutas_list = list(frutas)
print("frutas_list", frutas_list)

tupla_numeros = 122, 2323, 500
print("tupla_numeros", tupla_numeros)

# asginacion masiva a variables, en funcion de la misma posicion
a, b, c = tupla_numeros
print("a,b,c", a, b, c)

tupla_coma = 'tupla_con_coma',
print("tupla_coma", tupla_coma)

"""
Coleccion de tipo set, "conjunto"
No se pueden modificar pero si agregar o modificar, no se permiten valores repetidos, no tiene orden por lo cual no se puede acceder por indice
"""

planetas = {"Marte", "Jupiter", "Tierra"}
print("planetas", planetas)

cantidad_planetas = len(planetas)
print("cantidad_planetas", cantidad_planetas)

# Veriicar si un elemento esta dentro de la coleccion de tipo set
print("Esta Satruno en planetas?", "Saturno" in planetas)

# agregando un valor en cualquier posicion
planetas.add("Saturno")

# eliminar un valor en la coleccion set
planetas.remove("Tierra")
print("planetas.remove", planetas)

# eliminar con discard, no arroja un aexcepcion en caso de no encontrar el valor
planetas.discard("Tierra")
print("planetas.discard", planetas)

# vaciando el set
planetas.clear()
print("planetas.clear()", planetas)

# eleiminando la variable
del planetas

a = set('abracadabra')  # crea un conjunto o coleccion de tipo set, de todas las letras, eliminado los repetidos
b = set('alacazam')
print(a, b)

# operaciones de conjuntos
print("a - b", a - b)  # letras en a pero no en b
print("a | b", a | b)  # letras en a o en b o en ambas
print("a & b", a & b)  # letras en a y en b
print("a ^ b", a ^ b)  # letras en a o b pero no en ambas

# comprension en conjuntos
a = {x for x in 'abracadabra' if x not in 'abc'}  # retorna todas las letras, que no este dentro de abc
print("{x for x in 'abracadabra' if x not in 'abc'}", a)

"""
Diccionarios
# no manejan indices, pero si maneja llaves y su valor asociado
"""

libros = {
    "categorias": {
        "Accion", "Peliculas", "Terror", "Emprendimiento", "Programacion"
    },
    "id": 101,
    "caracteristica": ["Lo mejor", "cool"],
    "genero": "no definido"
}

print("libros", libros)
print("libros['id']", libros['id'])
print("libros.get('id')", libros.get('id'))
print("cantidad_objetos_libros", len(libros))

libros['genero'] = 'Especial'
# con .get(llave, valor_si_no_Existe_llave)
print("libros.get('genero')", libros.get('genero', 'full xx'))

# .setdefault(llave, valor?)  si existe la llave devuelve el valor, en caso contrario la crea y asigna el valor
libros.setdefault('precios', 1000)

# .update({}  | [(),()])  Recibe un diccionario o una lista con tuplas (llave, valor) actualiza de encontrar, sino lo crea
libros.update({'precios' : 800000})

for llave in libros:
    print("llave => ", llave, " | valor => ", libros.get(llave))

# .libros.values() devuelve los valores del diccionario
print("libros.values()", libros.values())

# .libros.keys() devuelve las llaves del diccionario
print("libros.keys()", libros.keys())

# libros.items()   devuelve un objeto de secuencia iterable, como una lista de tuplas [(), ()]
print("libros.items()", libros.items())

# comprobar si una llave esta en el diccionario
print("id existe en el libros", "id" in libros)

# para añadir uno nuevo se coloca como lista el nuvo valor de la llave, y se asigna el valor
libros["favoritos"] = "terror"
print("Anadiendo nuevos llave/valor al diccionario", libros)

# Eliminar valores de diccionario
libros.pop("id")
print("libros.pop", libros)

# Elimina el ultimo elemento ingresado : orden LIFO
libros.popitem()

# limpiando el diccionario
libros.clear()
print("libros.clear()", libros)

# eliminado diccionario
del libros

# Se puede crear el diccionario con la funcion dict(clave=valor)
frutas_precio = dict(manzana=50, pera=80, kiwii=900)
print("frutas_precio", frutas_precio)
# se puede crear, pasando una lista, con tuplas [(llave, valor), (llave, valor)]
frutas_sabor = dict([('manzana', 'dulce'), ('pera', 'acida'), ('kiwii', 'tropical')])
print("frutas_sabor", frutas_sabor)
