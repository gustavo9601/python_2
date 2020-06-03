from logger_base import logger
from conexion import Conexion
from persona import Persona
from cursor_del_pool import CursorDelPool


class PersonaDao:
    """DAO (Data Acces Object) CRUD sobre entidad Persona y tabla personas en la BD"""

    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    __ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email=%s WHERE id_persona = %s"
    __ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

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
            personas = []
            for registro in registros:
                # con los registros retornamos una lista de objetos con informacion de persona
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, Persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {Persona}')
            # los valores los obtenemos accediendo al objeto, ya que se pasa un objeto de Persona
            valores = (Persona.get_nombre(), Persona.get_apellido(), Persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)

            # cantidad de registros afectados
            return cursor.rowcount

    @classmethod
    def actualizar(cls, Persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {Persona}')
            # los valores los obtenemos accediendo al objeto, ya que se pasa un objeto de Persona
            valores = (Persona.get_nombre(), Persona.get_apellido(), Persona.get_email(), Persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)

            # cantidad de registros afectados
            return cursor.rowcount

    @classmethod
    def eliminar(cls, Persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {Persona}')
            # los valores los obtenemos accediendo al objeto, ya que se pasa un objeto de Persona
            valores = (Persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)

            # cantidad de registros afectados
            return cursor.rowcount


if __name__ == '__main__':
    """personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
        logger.debug(str(persona.get_id_persona()) + " " + persona.get_nombre())"""

    """persona1 = Persona(nombre="Ecehvarry", apellido="Doter", email="sss@sdasd.com")
    personas_insertadas = PersonaDao.insertar(persona1)
    logger.debug(f'Registros insertados {personas_insertadas}')"""

    persona1 = Persona(55, "Rene", "Higuita", "sss@sdasd.com")
    personas_actualizadas = PersonaDao.actualizar(persona1)
    logger.debug(f'Registros actualizados {personas_actualizadas}')

    """persona1 = Persona(54)
    personas_eliminas = PersonaDao.eliminar(persona1)
    logger.debug(f'Registros eliminados {personas_eliminas}')"""
