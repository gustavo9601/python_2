from conexion import Conexion
from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import logger


class UsuarioDao:
    __SELECCIONAR = "SELECT * FROM usuario"
    __INSERTAR = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    __ACTUALIZAR = "UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s"
    __ELIMINAR = "DELETE FROM usuario WHERE id_usuario = %s"

    @classmethod
    def seleccionar(cls):
        # con with abre el cursor y lo cierra de forma automatica, usada comun mente para abrir y cerrar recursos
        """
        Con la definicion de esta forma se obiene la ejecucion atuomatica de los siguientes metodos:
            __enter__() cuando crea la variable
            __exit__() cuando finaliza las lineas de codigo que contenga
        """
        with CursorDelPool() as cursor:
            # .mogrify(sql) mostrara el string que se ejecutara en la BD
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                # con los registros retornamos una lista de objetos con informacion de usuario
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, Usuario):
        with CursorDelPool() as cursor:
            # .mogrify(sql) mostrara el string que se ejecutara en la BD
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            valores_insertar = (Usuario.get_username(), Usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores_insertar)

            cantidad_insertados = cursor.rowcount
            return cantidad_insertados

    @classmethod
    def actualizar(cls, Usuario):
        with CursorDelPool() as cursor:
            # .mogrify(sql) mostrara el string que se ejecutara en la BD
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            valores_actualizar = (Usuario.get_username(), Usuario.get_password(), Usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores_actualizar)

            cantidad_actualizados = cursor.rowcount
            return cantidad_actualizados

    @classmethod
    def eliminar(cls, Usuario):
        with CursorDelPool() as cursor:
            # .mogrify(sql) mostrara el string que se ejecutara en la BD
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            valores_actualizar = (Usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores_actualizar)

            cantidad_eliminados = cursor.rowcount
            return cantidad_eliminados


if __name__ == '__main__':
    """ usuarios = UsuarioDao.seleccionar()
     for usuario in usuarios:
         print(usuario)"""

    """usuario1 = Usuario(username="melizamp", password="la mas larga de todas")
    insertando_usuario = UsuarioDao.insertar(usuario1)
    logger.debug(f"insertando_usuario : {insertando_usuario}")"""

""" usuario1 = Usuario(id_usuario=3, username="cinthyap", password="la mas larga de todas")
 actualizando_usuario = UsuarioDao.actualizar(usuario1)
 logger.debug(f"actualizando_usuario: {actualizando_usuario}")"""

"""usuario1 = Usuario(id_usuario=3)
eliminando_usuario = UsuarioDao.eliminar(usuario1)
logger.debug(f"eliminando_usuario: {eliminando_usuario}")"""