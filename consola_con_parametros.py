# Se importa la librera porpia del sistema para poder poner parametros al ejecutar el comando por consola
import sys


#en consola:
# py consola_con_parametros 10

text = sys.argv
print(text)

for idx, numero in enumerate(range(0, int(text[1]))):
    print("Numero", idx, 'valor=>', numero)
