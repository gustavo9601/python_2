class Producto:

    def __init__(self, sku, nombre, precio, divisa='COP'):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
        self.divisa = divisa

    def __str__(self):
        return (f"SKU: {self.sku} | Nombre: {self.nombre} | Precio : {self.precio}")
