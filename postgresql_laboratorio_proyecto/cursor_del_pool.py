from conexion import Conexion
from logger_base import logger


class CursorDelPool:

    def __init__(self):
        self.__conn = None
        self.__cursor = None

    # inicio de la sentencia With
    def __enter__(self):
        logger.debug('Inicio de with metodo __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()  # asignamos el cursor retornado de la conexion del pool

        return self.__cursor

    # fin del metodo With
    def __exit__(self, exception_type, exception_value, excepction_traceback):
        logger.debug('Se ejecuta metodo __exit__')
        # si exception_value , significa que hubo algun error
        if exception_value:
            self.__conn.rollback()
            logger.error(f'Ocurrio una exepcion: {exception_value}')
        else:
            self.__conn.commit()  # commit de la informacion (inserte, update, delete)
            logger.debug('Commit de la transaccion y regresando la conexion al pool')

        self.__cursor.close()  # cerramos el cursor
        Conexion.liberarConexion(self.__conn)

if __name__ == '__main__':
    # Obtenemos un cursor a parti de la conexion del pool
    # with ejecuta __enter__ y al finalizar __exit__

    with CursorDelPool() as cursor1:
        cursor1.execute('SELECT * FROM persona')
        registros = cursor1.fetchall()
        logger.debug(f'Listado de personas: {registros}')
