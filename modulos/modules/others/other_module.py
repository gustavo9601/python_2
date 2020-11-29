import sys

#Contiene el arreglo de rutas, donde buscara las importaciones
print("sys.path antes", sys.path)

# Le insertamos al arreglo de rutas, que tambien busque un directorio atras con  ..
sys.path.insert(1, '..')

print("sys.path despues", sys.path)

from modulo_clase import Supermarket

print("Supermarket", Supermarket)