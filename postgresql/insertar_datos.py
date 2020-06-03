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
sql = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = ('Carlos','Max','csssq@s.com')

#ejecutando sql
cursor.execute(sql, valores)
#guardando en la bd
conexion.commit()

registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

# cerrando las conexiones
cursor.close()
conexion.close()