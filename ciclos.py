"""
While
"""

contador = 0
while contador < 10:
    print(contador)
    contador+=1

"""
For
"""
for idx, valor in enumerate(range(0,100, 5)):
    print(idx, valor)

for letra in "Hola Mundo":
    print(letra)
else:  # se ejecutara al finalizar el ciclo
    print("Fin del ciclo imprimio Hola Mundo")


condicionA = 5
condicionB = 8
for valor in range(1,10):
    if condicionA == valor:
        continue # hara un salto en la ejecucion de los valores
    if condicionB == valor:
        break # rompera el ciclo
    print(valor)

