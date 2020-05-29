from logger_base import logger
from conexion import Conexion
from persona import Persona


class PersonaDao:
    """DAO (Data Acces Object) CRUD sobre entidad Persona y tabla personas en la BD"""

    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    __ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email=%s WHERE id_persona = %s"
    __ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        # .mogrify(sql) mostrara el string que se ejecutara en la BD
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            # con los registros retornamos una lista de objetos con informacion de persona
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)

        Conexion.cerrarConexion()
        return personas

    @classmethod
    def insertar(cls, Persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {Persona}')
            # los valores los obtenemos accediendo al objeto, ya que se pasa un objeto de Persona
            valores = (Persona.get_nombre(), Persona.get_apellido(), Persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)

            # grabar en bd
            conexion.commit()

            # cantidad de registros afectados
            return cursor.rowcount

        except Exception as e:
            conexion.rollback()
            logger.error(f'Error al insertar persona: {e}')
        finally:
            Conexion.cerrarConexion()

    @classmethod
    def actualizar(cls, Persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {Persona}')
            # los valores los obtenemos accediendo al objeto, ya que se pasa un objeto de Persona
            valores = (Persona.get_nombre(), Persona.get_apellido(), Persona.get_email(), Persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)

            # grabar en bd
            conexion.commit()

            # cantidad de registros afectados
            return cursor.rowcount

        except Exception as e:
            conexion.rollback()
            logger.error(f'Error al actualizar persona: {e}')
        finally:
            Conexion.cerrarConexion()

    @classmethod
    def eliminar(cls, Persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {Persona}')
            # los valores los obtenemos accediendo al objeto, ya que se pasa un objeto de Persona
            valores = (Persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)

            # grabar en bd
            conexion.commit()

            # cantidad de registros afectados
            return cursor.rowcount

        except Exception as e:
            conexion.rollback()
            logger.error(f'Error al eliminar persona: {e}')
        finally:
            Conexion.cerrarConexion()


if __name__ == '__main__':
    """personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
        logger.debug(str(persona.get_id_persona()) + " " + persona.get_nombre())"""

    """persona1 = Persona(nombre="Juanes", apellido="Melissss", email="sss@sdasd.com")
    personas_insertadas = PersonaDao.insertar(persona1)
    logger.debug(f'Registros insertados {personas_insertadas}')"""

    """persona1 = Persona(49, "Rene", "Higuita", "sss@sdasd.com")
    personas_actualizadas = PersonaDao.actualizar(persona1)
    logger.debug(f'Registros actualizados {personas_actualizadas}')"""

    persona1 = Persona(54)
    personas_eliminas = PersonaDao.eliminar(persona1)
    logger.debug(f'Registros eliminados {personas_eliminas}')