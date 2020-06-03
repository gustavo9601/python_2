import sys
from psycopg2 import pool
from logger_base import logger

"""
Pool de conexiones permite ir liberando conexiones y asignado a nuevos request por los clientes

De esta forma se optimiza la cantidad de memoria disponible en el servidor y limitara la cantidad de conexiones al tiempo
"""


class Conexion:
    __DATABASE = 'py_db_1'
    __USERNAME = 'postgres'
    __PASSWORD = '(Gustavo960131)'
    __DB_PORT = '5432'
    __HOST = 'localhost'
    __MIN_CON = 1
    __MAX_CON = 3
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool == None:
            try:
                # usamos el objeto de pysql pool  para crear el pool
                # pool.SimpleConnectionPool(cantidad_minima_conexiones, cantidad_maxima_conexiones, datos_de_conexion)
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE
                )
                logger.debug(f'Creacion exitosa del pool: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.error(f"Erro al crear el pool de conexiones: {e}")
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):
        # Obtener una conexion del objeto pool
        # .getcoon()  metodo encargado de retornar una de las conexiones disponibles en la bd
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, Conexion):
        # Regresar el objeto conexion al pool
        # .putcoon(Conexion) devolvera al pool de conexiones, la pasada por parametro para liberarla en otra peticion
        cls.obtenerPool().putconn(Conexion)
        logger.debug(f'Regresamos la conexion al pool: {Conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')

    @classmethod
    def cerrarConexiones(cls):
        # Cerrar el pool y todas las conexiones
        cls.obtenerPool().closeall()
        logger.debug(f"Se cerraron todas las conexiones del pool: {cls.__pool}")



if __name__ == '__main__':
    # Obtener una conexion a partir del poool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()

    #liberando la conexion
    Conexion.liberarConexion(conexion1)
    conexion4 = Conexion.obtenerConexion()
    # cerramos todas las conexiones
    Conexion.cerrarConexiones()
