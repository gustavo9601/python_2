archivo1 = open("prueba.txt", "r")

# print(archivo1.read())
# archivo.read(cantidad_caracteres) leer el archivo y captura todos los valores
# archivo1.read(5)      // especifica la cantidad de caracteres a leer
# archivo1.readline()    // lee una sola linea
# archivo1.readlines()    // retorna una lista con todas las lineas del archivo
# archivo1.readlines()[indice]    // retorna la linea especificada en el indice


# se recorre y leera linea a linea
# for linea in archivo1:
#    print("linea", linea)

# Creando una copia del archivo

archivo2 = open("copia_pruebas.txt",
                "a")  # open(path archivo, parametro) a => es un append de forma que no sobreescribe el archivo
archivo2.write(archivo1.read())
archivo2.close()
archivo1.close()

"""
Abriendo y cerrando automaticamente un archivo
usando content manager con With

 with ejecuta __enter__ y al finalizar __exit__
"""

with open("prueba.txt", 'r') as archivo_con_with:
    print(archivo_con_with.readlines())  # readlines  genera una lista con cada linea


"""
f.seek(posicion_inicial, desde_donde)  
posicion_inicial => posicion en bytes a ubicarse en el archivo
desde_donde => 0 inicio, 1 posicion actual, 2 final archivo
"""
with open("prueba.txt", 'r') as archivo_con_with:
    for idx, line in enumerate(archivo_con_with):
        print(f"linea en la ubicacion {idx} : {line} : posicion en el archivo : {archivo_con_with.tell}")




