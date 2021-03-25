
from os import path
# open(path archivo, "parametro")  permite abrir o crear archivos, en funcion del parametro
"""
w  abre el archivo si no existe lo crea
"""
try:
    # path.isFile('path/name.extencion') # retorna si existe el archivo pasado por parametro
    if path.isfile('prueba.txt'):
        print("Ciudado !!! El archivo prueba.txt ya existe")

    # w => sobrescribe datos si el archivo ya existe, de existir y no pusehar registros lo dejara vacio
    archivo1 = open("prueba.txt", "w")

    for numero in range(1, 11):
        # archivo.write(string a escribir) con \n hace el salto de linea
        archivo1.write(str(numero) + "\n")


except Exception as e:
    print("Error y el detalle => ", e)
finally:
    # La funcion close cierra el archivo y libera la memoria usada
    archivo1.close()

"""
Escribiendo el archivo usando with
"""
with open('archivo_with.txt', 'w') as archivo_with:
    archivo_with.writelines('ssss')  # .writelines recibe una lista de parametros y las pushea

with open('archivo_with.txt', 'a') as archivo_with:  # a => pushea los datos y no reemplaza
    archivo_with.writelines(['\nLina3\n', 'Linea4\n'])  # .writelines recibe una lista de parametros y las pushea
