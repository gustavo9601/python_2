# importacion de libreria
import psycopg2

# abriendo la conexion
conexion = psycopg2.connect(user='postgres',
                            password='(Gustavo960131)',
                            host='localhost',
                            port='5432',
                            database='py_db_1')

try:
    # Se realiza el auto commit, de forma que ya despues no es necesario llamarlo
    # conexion.autocommit = True

    # inicializando la conexion
    cursor = conexion.cursor()
    # sql, %s concota que recibira un parametro
    sql = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = (('Jose', 'Max', 'csssq@s.com'), ('riell', 'Max', 'csssq@s.com'), ('Xandeal', 'test', 'csssq@s.com'))
    # ejecutando sql, con executemany para que soporte mulitples insersiones
    cursor.executemany(sql, valores)

    registros_insertados = cursor.rowcount
    print(f'Registros insertados: {registros_insertados}')

    sql = 'UPDATE persona SET nombre = %s WHERE id_persona = %s'
    valores = ('Alfonzo perez', 48)
    cursor.execute(sql, valores)
    registros_actualizados = cursor.rowcount

    # con el commit, si todas las sentencias se ejecutan correctamente se ejecutan de lo contrario no hace nada
    conexion.commit()
    print(f'Registros actualizados: {registros_actualizados}')

except Exception as e:
    print(f"Ocurrio un error en la transaccion {e}")
    # si falla, lanza una expecion la contralamos y podemos lanzar el rollback
    conexion.rollback()
finally:
    # cerrando las conexiones
    cursor.close()
    conexion.close()
