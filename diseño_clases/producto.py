class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        # Incrementando la variable en cada instancia
        Producto.contador_productos += 1

        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def __str__(self):
        return "ID producto: " + str(self.__id_producto) + ", Nombre: " + self.__nombre + ", precio: " + str(self.__precio)
