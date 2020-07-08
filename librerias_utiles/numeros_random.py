import random
#random numero deciamal aletaorio entre 0 y 1

numero1 = random.random()

# numero random de 1 a 10 | despues numeros de 0 a 5 | se suma 1 al resultado | convierte a entero para descartar decimales
numero2 = int((random.random()*10)%6+1)

# en funcion de la lista pasada por paraemtro seleccia uno aletaroio
aletarorio = random.choice([1,2,5,10,100])

# devuelve una lista, con la cantidad de valores aletaroios que se pasan por pareamtros
lista_aletaroios = random.choices([10,50,100,6], k=2)