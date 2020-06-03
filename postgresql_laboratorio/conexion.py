import psycopg2 as db
import sys
from logger_base import logger


class Conexion:
    __DATABASE = 'py_db_1'
    __USERNAME = 'postgres'
    __PASSWORD = '(Gustavo960131)'
    __DB_PORT = '5432'
    __HOST = 'localhost'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        # verifica si no se ha inicializado la conexion
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE
                )
                logger.debug(f'Conexion exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la BD: {e}')
                sys.exit()  # finaliza la ejecucion del programa
        return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                # asginamos la conexion a la variable de clase, y llamamos la funcion .cursor() ya que retorna un objeto de conexion
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrio el cursor correctamente: {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls.__cursor

    @classmethod
    def cerrarConexion(cls):
        # pregunta si no es None
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
                logger.debug('Cerro el cursor con exito')
            except Exception as e:
                logger.error(f"Error al cerrar cursor: {e}")
                sys.exit()

        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
                logger.debug('Cerro la conexion a la BD con exito')
            except Exception as e:
                logger.error(f"Error al cerrar la conexion: {e}")
                sys.exit()

