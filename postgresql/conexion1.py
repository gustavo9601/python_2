"""
Instalar el dirver y modulo de conexion en py para conexion pgsql
pip install psycopg2

Mysql
pip install mysql-connector
"""
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
sql = 'SELECT * FROM persona WHERE id_persona = %s'
id = (str(2),)  # el parametro debe ir encerrado en tupla y valor string

# ejecutando la sentencia
# como segundo parametro sera los n parametros en el orden que este en la sentencia sql
cursor.execute(sql, id)
# capturando los regusdaos
registros = cursor.fetchall()
"""
.fetchone()  retorna un registro
"""
print(registros)
# cerrando las conexiones
cursor.close()
conexion.close()
