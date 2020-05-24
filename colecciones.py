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

nombres.append("Rodolfo")  # inserta en la ultima posicion
nombres.insert(2, "Cecilia")  # inserta en la posicion indicada
print("nombres.append() and nombres.insert()", nombres)

nombres.remove("Gustavo")  # elimina el elemento proporcionado por parametro
print("nombres.remove()", nombres)

nombres.pop()  # elimina el ultimo elemento de la lista
print("nombres.pop()", nombres)

del nombres[2]  # elimina el indice indicado
print("del nombre[]", nombres)

nombres.clear()  # vacia los elementos de la lista
print("nombres.clear()", nombres)

# elimina la variable de memoria
del nombres

# Ejericio numeros divisbles por 3
for valor in range(0, 11):
    if valor % 3 == 0:
        print("valor divisible por 3", valor)

"""
Tuplas
"""
frutas = ("pera", "banano", "papaya", "coco")
print("frutas", frutas)
print("frutas[0:1]", frutas[0:2])
frutas_list = list(frutas)
print("frutas_list", frutas_list)

"""
Coleccion de tipo set
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

for llave in libros:
    print("llave => ", llave,  " | valor => ", libros.get(llave))

# .libros.values() devuelve los valores del diccionario
print("libros.values()", libros.values())

# .libros.keys() devuelve las llaves del diccionario
print("libros.keys()", libros.keys())

#comprobar si una llave esta en el diccionario
print("id existe en el libros", "id" in libros)

# para añadir uno nuevo se coloca como lista el nuvo valor de la llave, y se asigna el valor
libros["favoritos"] = "terror"
print("Anadiendo nuevos llave/valor al diccionario", libros)

#Eliminar valores de diccionario
libros.pop("id")
print("libros.pop", libros)


# limpiando el diccionario
libros.clear()
print("libros.clear()", libros)

# eliminado diccionario
del libros