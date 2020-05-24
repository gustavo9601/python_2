class Supermarket:
    def __init__(self, nombre_producto, cantidad):
        self.__nombre_producto = nombre_producto
        self.__cantidad = cantidad

    def __str__(self):
        return "Nombre producto: " + self.__nombre_producto + " y cantidad: " + str(self.__cantidad)