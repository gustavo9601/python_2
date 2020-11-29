# Importando libreria para abrir archivos
from io import open

texto1 = 'Linea 1\nLinea 2\nLinea 3'

# open(path/nombre_archivo, modo de apertura)  // de inmediato abre o crea el archivo si no existe
fichero1 = open('./files_manipulacion/fichero1.txt', 'w')  # w => modo escritura

# .write(string_a_escribir)
fichero1.write(texto1)

# .close() cerramos el archivo
fichero1.close()

############################################
fichero2 = open('./files_manipulacion/fichero1.txt', 'r')  # r => lectura
# a => modo lectura, pero si no existe lo crea
# r+  => modo escritura con el puntero en la posicion inicial

# .readlines()  lee la data y la deuvelve cada linea en una lista
text_fichero1 = fichero2.readlines()
fichero2.close()
print("text_fichero1", text_fichero1)

###########################################
with open('./files_manipulacion/fichero1.txt', 'r') as fichero:
    for idx, linea in enumerate(fichero):
        print("idx => ", idx, ' linea =>', linea)

#############################################
# Guardar valores en binarios con libreria pickle
# guardar colecciones, diccionarios, clasess
import pickle

lista1 = [1, 2, 3, 4, 56, 210]

fichero3 = open('./files_manipulacion/fichero.pickle', 'wb')
# wb => escritura binaria, si existe sobrescribira toda la estrictura
# ab+ => abre en modo escritura, y se posiona del puntero al final del documento
# .dump(lista de valores, archivo) # escribira en el archivo
pickle.dump(lista1, fichero3)

fichero3.close()


fichero4 = open('./files_manipulacion/fichero.pickle', 'rb')
# rb => lectura binaria

# .load(archivo binario) // trasnforma los datos al valor inicial mente escrito
lista_recuperada = pickle.load(fichero4)
print("lista_recuperada", lista_recuperada)