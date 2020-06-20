from cliente import Cliente
from producto import Producto
import csv


class CajaRegistradora:
    cliente = None
    ticket = 1
    valor_a_pagar = 0
    valor_pagado = 0
    lista_productos = []
    lista_productos_agregados = []

    @classmethod
    def cargar_productos(cls):
        # Lectura del archivo
        with open('BD/productos_bd.csv', 'r') as csv_example:
            reader_csv = csv.reader(csv_example)
            for row in reader_csv:
                # hacemos la separacion del string
                string_producto = ', '.join(row)
                arreglo_producto = string_producto.split(';')
                producto = Producto(arreglo_producto[0], arreglo_producto[1], arreglo_producto[2], arreglo_producto[3])
                cls.lista_productos.append(producto)

    @classmethod
    def listar_productos(cls):
        for idx, producto in enumerate(cls.lista_productos):
            print(str(idx + 1), producto)

    @classmethod
    def buscar_producto_sku(cls, sku):
        for idx, producto in enumerate(cls.lista_productos):
            if producto.sku == str(sku):
                return producto

    @classmethod
    def agregar_producto_carrito(cls, producto):
        cls.lista_productos_agregados.append(producto)

    @classmethod
    def listar_productos_carrito(cls):
        for idx, producto_agregado in enumerate(cls.lista_productos_agregados):
            print(str(idx + 1) + '.', producto_agregado)

    @classmethod
    def eliminar_producto_carrito(cls, id_item):
        if id_item <= len(cls.lista_productos_agregados) and id_item > 0:
            cls.lista_productos_agregados.pop(id_item - 1)
            return True
        else:
            return False

    @classmethod
    def cantidad_productos_carrito(cls):
        return len(cls.lista_productos_agregados)

    @classmethod
    def subtotal_compra_carrito(cls):
        subtotal = 0
        for producto_carrito in cls.lista_productos_agregados:
            subtotal += int(producto_carrito.precio)
        return subtotal

    @classmethod
    def pagar_carrito(cls, dinero_cliente):

        if cls.valor_a_pagar == 0:
            cls.valor_a_pagar = cls.subtotal_compra_carrito()
        cls.valor_a_pagar -= dinero_cliente
        cls.valor_pagado += dinero_cliente
        return cls.valor_a_pagar

    @classmethod
    def imprimir_ticket(cls):
        print(f"""
====================================================
====================================================
====================================================
            TICKET DE VENTA NO. {cls.ticket}
====================================================
====================================================
====================================================
    
          ID cliente: {cls.cliente.id_cliente}
          Nombre cliente: {cls.cliente.nombre}

-----------------------------------------------------
                 Listado productos:
""")
        for idx, producto_carrito in enumerate(cls.lista_productos_agregados):
            print(f"""
# Item          Nombre        Cantidad       Precio
""")
            print("{value:<15}".format(value=idx), "{value:<15}".format(value=producto_carrito.nombre),
                  "{value:<15}".format(value=1), "{value:<15}".format(value=producto_carrito.precio))

        print(f"""
----------------------------------------------------
        Total: {cls.subtotal_compra_carrito()} COP
        Cantidad productos: {cls.cantidad_productos_carrito()}
        Valor pagado por el cliente: {abs(cls.valor_pagado)}
        Cambio a favor del cliente: {abs(cls.valor_a_pagar)}
    

      Gracias por su compra, vuelva pronto !!!!!
-----------------------------------------------------
    """)

    @classmethod
    def reset_carrito(cls):
        cls.lista_productos_agregados = []
        cls.ticket += 1
        cls.cliente = None
        cls.valor_a_pagar = 0
        cls.valor_pagado = 0


def menuOpciones():
    menu_inicial = f"""
    ====================================================
            Bienvenido - ticket # {CajaRegistradora.ticket} 
    ====================================================
    Por favor seleccione alguna de las siguientes opciones:
    1. Inciar proceso de facturacion
    7. Finalizar
    """
    opcion = int(input(menu_inicial))
    while opcion != 1 and opcion != 7:
        print("Opcion invalida, seleccione una de las siguientes!!!")
        opcion = int(input(menu_inicial))

    if opcion == 1:
        id_cliente = input("Por favor ingresa el ID/DNI/Cedula del cliente: ")
        nombre_cliente = input("Por favor ingresa el nombre del cliente: ")
        cliente = Cliente(id_cliente, nombre_cliente)
        CajaRegistradora.cliente = cliente

    while (opcion != 7):
        menu = """
        ===========================================================
                         MENU DE OPCIONES DASHBOARD
        ===========================================================
        Seleccione alguna de las siguientes opciones para facturar:
        1. Listar productos disponibles
        2. Agregar producto
        3. Eliminar producto agregado
        4. Proceder a pagar el ticket
        5. Listar productos agregados al carrito
        6. Conocer subtotal del ticket
        7. Finalizar compra
        """
        opcion_menu_facturacion = int(input(menu))

        while opcion_menu_facturacion != 1 and opcion_menu_facturacion != 2 and opcion_menu_facturacion != 3 and opcion_menu_facturacion != 4 and opcion_menu_facturacion != 5 and opcion_menu_facturacion != 6 and opcion_menu_facturacion != 7:
            print("Opcion invalida, seleccione una de las siguientes!!!")
            opcion_menu_facturacion = int(input(menu))

        # Incializando la carga de productos disponibles
        CajaRegistradora.cargar_productos()
        if opcion_menu_facturacion == 1:
            print("**Lista de productos disponibles a la venta**")
            CajaRegistradora.listar_productos()
        elif opcion_menu_facturacion == 2:
            sku = input("Ingrese el SKU del articulo a agregar al carrito: ")
            producto_seleccionado = CajaRegistradora.buscar_producto_sku(sku)
            while not producto_seleccionado:
                print("SKU invalido o no encontrado !!!")
                sku = input("Ingrese el SKU del articulo a agregar al carrito: ")
                producto_seleccionado = CajaRegistradora.buscar_producto_sku(sku)
            CajaRegistradora.agregar_producto_carrito(producto_seleccionado)
            print("**SKU Agregado a la lista del carrito**")
        elif opcion_menu_facturacion == 3:
            if CajaRegistradora.cantidad_productos_carrito():
                item_eliminar = int(input("Digite el numero de item de la lista, a eliminar: "))
                while not CajaRegistradora.eliminar_producto_carrito(item_eliminar):
                    print("El item no es valido, o no se enconttro!!!")
                    item_eliminar = int(input("Digite el numero de item de la lista, a eliminar"))
                print("**Item eliminado de la lista del carrito**")
            else:
                print("No tienes productos agregados a la lista del carrito")
        elif opcion_menu_facturacion == 4:
            if CajaRegistradora.cantidad_productos_carrito():

                print(f"El valor total a pagar por el ticket es: {CajaRegistradora.subtotal_compra_carrito()}")
                valor_pagar_cliente = int(input("Con cuanto dinero en efectivo va a cancelar?: "))

                while CajaRegistradora.pagar_carrito(valor_pagar_cliente) > 0:
                    valor_pagar_cliente = int(input(
                        f"Te hace falta por pagar: {CajaRegistradora.valor_a_pagar}, por favor digita el nuevo monto a cancelar: "))

                CajaRegistradora.imprimir_ticket()


                opcion_finalizar_ticket = input("Desas continuar con otro ticket SI/NO?")
                while opcion_finalizar_ticket != "SI" and opcion_finalizar_ticket != "NO":
                    print("Opcion invalida !!!!")
                    opcion_finalizar_ticket = input("Desas continuar con otro ticket SI/NO? ")

                if opcion_finalizar_ticket == "SI":
                    CajaRegistradora.reset_carrito()
                    print("""
===========================================================
===========================================================
                    """)
                    id_cliente = input("Por favor ingresa el ID/DNI/Cedula del cliente: ")
                    nombre_cliente = input("Por favor ingresa el nombre del cliente: ")
                    cliente = Cliente(id_cliente, nombre_cliente)
                    CajaRegistradora.cliente = cliente

                else:
                    opcion = 7
                    break
            else:
                print("No tienes productos agregados a la lista del carrito")
        elif opcion_menu_facturacion == 5:
            print("**Lista de productos agregados al carrito**")
            CajaRegistradora.listar_productos_carrito()
        elif opcion_menu_facturacion == 6:
            print(f"**Subtotal Ticket # {CajaRegistradora.ticket}: {CajaRegistradora.subtotal_compra_carrito()}")
            print(f"**Unidades Ticket # {CajaRegistradora.ticket}: {CajaRegistradora.cantidad_productos_carrito()}")
        elif opcion_menu_facturacion == 7:
            opcion = 7
            break

    print("Gracias por usar la caja_registradora_1.0 Courser GM")


if __name__ == '__main__':
    menuOpciones()
