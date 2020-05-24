# llamando el archivo modulo_funciones y con alias funciones accedemos a todas las ufnciones
# import carpeta.nombre_archivo
import modules.modulo_funciones as funciones
print(funciones.multiplicar(5,5,100))

# from carpeta.nombre_archivo import nombreClase
from modules.modulo_clase import Supermarket
supermarket1 = Supermarket('Carne', '2 LB')
print(supermarket1)
