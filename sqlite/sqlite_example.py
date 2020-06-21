#Permite crear una BD en memoria, puede ser usada para correr test unitarios
import sqlite3

# sqlite3.connect(path_archivo_BD || memory)
# si esta en memoria, una ves finalizada la ejecicion la memoria se pierde
connection = sqlite3.connect(':memory:')

# Cursor
cursor = connection.cursor()

#Consulta sql a ejecutar
sql = """CREATE TABLE currency
        (ID INTEGER PRIMARY KEY, NAME TEXT, SYMBOL TEXT)"""

#Ejecutando la consulta
cursor.execute(sql)

#Insertando registros
sql1 = "INSERT INTO currency VALUES (1, 'Peso Colombiano', '$');"
sql2 = "INSERT INTO currency VALUES (2, 'Dollar estadounidense', 'US$');"

#Ejecutanso los registros de insercion
cursor.execute(sql1)
cursor.execute(sql2)

#Guardando los cambios
connection.commit()

#Revirtiendo los cambios
#connection.rollback()

#Consulta sobre los registros
sql = "SELECT * FROM currency"
#ejecutando la consulta
cursor.execute(sql)
#obteniendo los registros
values = cursor.fetchall()
print(values)
# fetchone()  retorna la siguiente fila de los  registro retornados
print(cursor.execute("SELECT * FROM currency").fetchone())


#Cerrando la conexion
connection.close()
