from usuario_dao import UsuarioDao
from usuario import Usuario


def menu_app_usuarios():
    print("*Bienvenido al aplicativo Crud de usuarios*\n")
    menu = (f"""
    Por favor seleccione una de las siguientes opciones:
        1. Listar usuarios
        2. Agregar Usuario
        3. Actualizar Usuario
        4. Eliminar Usuario
        5. Salir
    """)

    opcion = int(input(menu))

    while opcion != 5:
        opciones(opcion)
        opcion = int(input(menu))

    print("Gracias por usar el aplicativo CRUD de usuarios")


def opciones(opcion):
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for idx, usuario in enumerate(usuarios):
            print(f"#{idx} - {usuario.__str__()}")
    elif opcion == 2:
        username = input("Username: ")
        password = input("Password: ")
        usuario = Usuario(username=username, password=password)
        usuario_insertar = UsuarioDao.insertar(usuario)
        print(f'Usuario insertado: {usuario_insertar}')
    elif opcion == 3:
        id_usuario = int(input("Id Usuario: "))
        username = input("Username: ")
        password = input("Password: ")
        usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
        usuario_actualizar = UsuarioDao.actualizar(usuario)
        print(f'Usuario actualiar: {usuario_actualizar}')
    elif opcion == 4:
        id_usuario = int(input("Id Usuario: "))
        usuario = Usuario(id_usuario=id_usuario)
        usuario_eliminar = UsuarioDao.eliminar(usuario)
        print(f'Usuario eliminar: {usuario_eliminar}')
    else:
        print("Opcion invalida, digite un valor del (1-5)")


menu_app_usuarios()
