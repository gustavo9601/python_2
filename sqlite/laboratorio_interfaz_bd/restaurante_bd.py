# improtanodo libreria
import sqlite3


class ConectionRestaurante:


    def __init__(self):
        # creando la conexion, o el archivo nuevo si no existe
        self.conexion = sqlite3.connect('restaurante.db')
        self.cursor = self.conexion.cursor()
        self.create_table_restaurante()

    
    def create_table_restaurante(self):
        create_table = """CREATE TABLE IF NOT EXISTS
                            restaurante
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            menu VARCHAR (100) NOT NULL,
                            platos VARCHAR (100) NOT NULL)"""
        self.cursor.execute(create_table)

    
    def cerrar_conection(self):
        self.conexion.close()

    
    def insert_values(self):
        sql_insert = "INSERT INTO restaurante VALUES (null, ?,?)"
        platos = [
            ('Principal', 'Arroz con leche, Arroz apanadado, Arroz con pollo'),
            ('Secundario', 'Panela, Ensalada, Carne'),
        ]
        self.cursor.executemany(sql_insert, platos)
        self.conexion.commit()

    
    def query_platos(self):
        sql_query = "SELECT * FROM restaurante"
        self.cursor.execute(sql_query)
        platos = self.cursor.fetchall()
        return platos


if __name__ == '__main__':
    restaurante = ConectionRestaurante()
    restaurante.insert_values()
    platos = restaurante.query_platos()
    print("platos", platos)