# llamando el archivo modulo_funciones y con alias funciones accedemos a todas las ufnciones
# import carpeta.nombre_archivo
import modules.modulo_funciones as funciones
print("funciones.multiplicar(5,5,100)", funciones.multiplicar(5,5,100))

# from carpeta.nombre_archivo import nombreClase or nombreFuncion or * or nameClase, nameClase2
from modules.modulo_clase import Supermarket
supermarket1 = Supermarket('Carne', '2 LB')
print("supermarket1", supermarket1)

"""
dir() lista los nombres de las funciones que contiene el modulo
dir(nombre_Modulo) lista los nombres de los modulos definidos del modulo pasado por parametro
"""
print("dir(funciones):", dir(funciones))