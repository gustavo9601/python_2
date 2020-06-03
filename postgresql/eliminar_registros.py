# importacion de libreria
import psycopg2

# abriendo la conexion
conexion = psycopg2.connect(user='postgress',
                            password='(Gustavo960131)',
                            host='localhost',
                            port='5432',
                            database='py_db_1')
# inicializando la conexion
cursor = conexion.cursor()
# sql, %s concota que recibira un parametro
sql = 'DELETE FROM persona WHERE id_persona = %s'

valores = (21,)

# ejecutando sql con executemany para actualizar varios a la ves
cursor.execute(sql, valores)
# guardando en la bd
conexion.commit()

registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

# cerrando las conexiones
cursor.close()
conexion.close()
