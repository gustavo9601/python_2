# importacion de libreria
import psycopg2

# abriendo la conexion
conexion = psycopg2.connect(user='postgres',
                            password='(Gustavo960131)',
                            host='localhost',
                            port='5432',
                            database='py_db_1')
# inicializando la conexion
cursor = conexion.cursor()
# sql, %s concota que recibira un parametro
sql = 'UPDATE persona SET nombre = %s, email = %s WHERE id_persona = %s'

valores = (('Juanes', 'perez@ggg.com', 18), ('Laura', 'laurisqs.com', 19))

# ejecutando sql con executemany para actualizar varios a la ves
cursor.executemany(sql, valores)
# guardando en la bd
conexion.commit()

registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

# cerrando las conexiones
cursor.close()
conexion.close()
