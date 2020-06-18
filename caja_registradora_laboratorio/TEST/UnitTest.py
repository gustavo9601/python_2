if __name__ == '__main__':

    CajaRegistradora.cargar_productos()
    # CajaRegistradora.listar_productos()
    # CajaRegistradora.buscar_producto_sku(sku=1235456)
    CajaRegistradora.agregar_producto_carrito(Producto(123, 'asdasdasd', 50, 'US'))
    CajaRegistradora.agregar_producto_carrito(Producto(12323, 'as', 50, 'US'))
    CajaRegistradora.agregar_producto_carrito(Producto(1199923, 'eeessdasd', 90, 'US'))
    CajaRegistradora.listar_productos_carrito()
    #print("Eliminando")
    #CajaRegistradora.eliminar_producto_carrito(1)
    cliente1 = Cliente(9612, 'Gustavo')
    CajaRegistradora.cliente = cliente1
    CajaRegistradora.imprimit_ticket()
