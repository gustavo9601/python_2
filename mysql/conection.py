# pip install mysql-connector-python


import mysql.connector
import random
import math

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test_py'
)

cursor = midb.cursor()

query = 'select * from users'
cursor.execute(query)


"""
Consultar
.fetchall()  // Todos los registros
.fetchone()  // El primer elemento retornado
"""
resultado = cursor.fetchall()

print(resultado)

"""
Insertar datos
"""
query = 'INSERT INTO users (name, surname, age) VALUES (%s, %s, %s)'

random_number = math.ceil(random.random() * 10)
values = ('gustavo_' + str(random_number), 'mar', random_number)

# .execute(sql, fields values)
cursor.execute(query, values)
midb.commit()


"""
Actualizar datos
"""
query = 'UPDATE USERS set name = %s WHERE id = %s'
values = ('adolfoo' * random_number, 1)
cursor.execute(query, values)
midb.commit()


"""
Eliminar datos
"""
query = 'DELETE FROM users WHERE id = %s'
values = (2,)
cursor.execute(query, values)
midb.commit()
