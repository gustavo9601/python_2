from producto import Producto
class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def total_orden(self):
        total = 0
        for producto in self.__productos:
            # al ser una lista de objetos, accedemos a las propiedades de clase
            total += producto.get_precio()
        return total

    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            # se concatenara cada producto enviado y ejecutara la funcion str que retorna el string
            productos_str += producto.__str__() + " | "

        return "id_orden: " + str(self.__id_orden) + ", productos: " + productos_str + " **Total: " + str(self.total_orden())
