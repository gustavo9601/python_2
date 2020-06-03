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
sql = 'SELECT * FROM persona WHERE id_persona IN %s'
# se debe enviar com ouna tupa de tuplas
ids = ((1,2,3),)

# ejecutando la sentencia
# como segundo parametro sera los n parametros en el orden que este en la sentencia sql
cursor.execute(sql, ids)
# capturando los regusdaos
registros = cursor.fetchall()


for registro in registros:
    print(registro)

# cerrando las conexiones
cursor.close()
conexion.close()