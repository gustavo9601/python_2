import unittest
from caja_registradora import CajaRegistradora
from cliente import Cliente
from producto import Producto


class TestCajaRegistradora(unittest.TestCase):

    def test_is_type_cliente(self):
        cliente1 = Cliente(9612, 'Gustavo')
        cliente2 = Cliente(9852, 'Laura')
        self.assertIs(type(cliente1), type(cliente2))

    def test_is_type_producto(self):
        producto1 = Producto(9612, 'Arroz', 5000, 'COP')
        producto2 = Producto(1234, 'Maiz', 100)
        self.assertIs(type(producto1), type(producto2))

    def test_lista_productos_null(self):
        self.assertEqual([], CajaRegistradora.lista_productos)

    @unittest.skip('Verifica cada objeto pusheado sea de tipo Producto')
    def test_lista_productos(self):
        CajaRegistradora.cargar_productos()
        producto1 = Producto(9612, 'Arroz', 5000, 'COP')
        for producto in CajaRegistradora.lista_productos:
            self.assertIs(type(producto), type(producto1))

    def test_buscar_producto_sku(self):
        sku_to_find = 1223456  # No lo debe encontrar
        self.assertFalse(CajaRegistradora.buscar_producto_sku(sku_to_find))

    def test_agregar_producto_carrito(self):
        producto1 = Producto(9612, 'Arroz', 5000, 'COP')
        CajaRegistradora.agregar_producto_carrito(producto1)
        self.assertEqual(CajaRegistradora.cantidad_productos_carrito(), 1)
        lista_productos_agregados = CajaRegistradora.lista_productos_agregados
        self.assertIn(producto1, lista_productos_agregados)

    def test_eliminar_producto_carrito(self):
        id_eliminar = 1
        cantidad_antes_eliminar = CajaRegistradora.cantidad_productos_carrito()
        self.assertTrue(CajaRegistradora.eliminar_producto_carrito(id_eliminar))
        self.assertEqual((cantidad_antes_eliminar - 1), CajaRegistradora.cantidad_productos_carrito())

    def test_cantidad_productos_carrito(self):
        self.assertEqual(CajaRegistradora.cantidad_productos_carrito(), len(CajaRegistradora.lista_productos_agregados))

    def test_subtotal_carrito(self):
        subtotal = 0
        for producto_carrito in CajaRegistradora.lista_productos_agregados:
            subtotal += int(producto_carrito.precio)
        self.assertEqual(subtotal, CajaRegistradora.subtotal_compra_carrito())

    def test_pagar_carrito(self):

        dinero_cliente = 500

        CajaRegistradora.cargar_productos()
        CajaRegistradora.agregar_producto_carrito(Producto(123, 'Arroz', 50, 'US'))
        CajaRegistradora.agregar_producto_carrito(Producto(12323, 'Pan', 50, 'US'))
        CajaRegistradora.agregar_producto_carrito(Producto(1199923, 'Maiz', 90, 'US'))

        CajaRegistradora.pagar_carrito(dinero_cliente)
        self.assertEqual(CajaRegistradora.valor_a_pagar, (CajaRegistradora.subtotal_compra_carrito() - dinero_cliente))
        self.assertEqual(CajaRegistradora.valor_pagado, dinero_cliente)

    def test_reset_carrito(self):
        CajaRegistradora.reset_carrito()

        self.assertEqual(CajaRegistradora.lista_productos_agregados, [])
        self.assertEqual(CajaRegistradora.ticket, 2)
        self.assertEqual(CajaRegistradora.cliente, None)
        self.assertEqual(CajaRegistradora.valor_a_pagar, 0)
        self.assertEqual(CajaRegistradora.valor_pagado, 0)

if __name__ == '__main__':
    unittest.main()
