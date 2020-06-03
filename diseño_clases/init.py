from producto import Producto
from orden import Orden

"""
Pruebas de producto
"""

producto1 = Producto('Arroz', 1000)
print(producto1)

producto2 = Producto('Panela', 2000)
print(producto2)

producto3 = Producto('Aguacate', 3000)
print(producto3)

lista_productos = [producto1, producto2]

print("*******************Ordenes*******************")
orden1 = Orden(lista_productos)
print(orden1)


orden2 = Orden(lista_productos)
orden2.agregar_producto(producto3)
print(orden2)
