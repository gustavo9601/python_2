import random

# random numero deciamal aletaorio entre 0 y 1
numero1 = random.random()
print("numero1", round(numero1 * 10))

# numero random de 1 a 10 | despues numeros de 0 a 5 | se suma 1 al resultado | convierte a entero para descartar decimales
numero2 = int((random.random() * 10) % 6 + 1)

# en funcion de la lista pasada por paraemtro seleccia uno aletaroio
numero_aletaroria = random.choice([1, 2, 5, 10, 3, 4])
print("numero_aleatorio", numero_aletaroria)

# da un nuevo orden a una lista
lista_ordenada = [1, 2, 3, 4, 5, 6]
random.shuffle(lista_ordenada)
print("lista_aletaroria_desordenada", lista_ordenada)

# da una muestra de elementos aleatorios
# sample(lista, cantidad_numeros_a_seleccionar_aleatoriamente)
print("random.sample(lista_ordenada, 2)", random.sample(lista_ordenada, 2))

# devuelve una lista, con la cantidad de valores aletaroios que se pasan por 2 pareamtro
lista_aletaroios = random.choices([10, 50, 100, 6], k=3)
print("lista_aletaroios k=3 =>", lista_aletaroios)

# devuelve un random flotante de acuerdo al rango proprocinado, sin contar con el inicial ni el final
numeros_rango = random.uniform(0, 11)  # numeros de 0 a 11
print("numeros_rango => ", numeros_rango)

# devuelve un random entero
print("random.randrange(11) => ", random.randrange(11))  # numeros >= 0 y <11
print("random.randrange(0,101,5) => ", random.randrange(0, 101, 5))  # numero >= 0 and < 101 de 5 en 5


word_list = ['a', 'b', 'c']
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

print(generate_password())