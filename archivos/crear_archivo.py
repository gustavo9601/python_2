# open(path archivo, "parametro")  permite abrir o crear archivos, en funcion del parametro
"""
w  abre el archivo si no existe lo crea
"""
try:
    archivo1 = open("prueba.txt", "w")

    for numero in range(1,11):
        # archivo.write(string a escribir) con \n hace el salto de linea
        archivo1.write(str(numero) + "\n")


except Exception as e:
    print("Error y el detalle => ", e)
finally:
    #La funcion close cierra el archivo y libera la memoria usada
    archivo1.close()
