# improtanodo libreria
import sqlite3

# creando la conexion, o el archivo nuevo si no existe
conexion = sqlite3.connect('test_bd.db')

cursor = conexion.cursor()

#sql_create_table = 'CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))';
#sql_insert_register = "INSERT INTO usuarios VALUES ('Gustavo', 24, 'gus@s.cm')"

# insertando varios registros
usuarios_insert = [
    ('Laura', 22, 'laur'),
    ('Martha', 55, 'mart'),
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios_insert)

conexion.commit()

sql_query = "SELECT * FROM usuarios"

#Ejecutando script
cursor.execute(sql_query)

# recuperando registros
usuarios = cursor.fetchall()

print("usuarios", usuarios)




conexion.close()