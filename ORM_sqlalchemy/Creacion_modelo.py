"""
ORM Obrject relation mapping
Crea un modelamiento o abstaccion de las tablas relacionales en el programa, permitiendo
acceder a la BD a traves de esta interfaz
"""

# pip install SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

#Definimos la clase con los elementos que componen la tabla
class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

#Crea el esquema
Base.metadata.create_all(engine)

print("Author.__table__", Author.__table__)

author1 = Author(firstname='Gustavo', lastname='Marquez')
author2 = Author(firstname='Laura', lastname='Prieto')
print("author1", author1)

#Creando la sesion para manipular la data
Session = sessionmaker(bind=engine)

session = Session()
# add(Objeto de la clase)  // añade de a un registro
session.add(author1)
session.add(author2)

#add_all(arreglo de objetos de la clase)  // añade mulitples registros
session.add_all([author1, author2])

# sesscion.query(Clase modelo).funcion a ejecutar
query_author = session.query(Author).first()
print("query_author session.query(Author).first()", query_author)

query_author = session.query(Author).all()
print("query_author session.query(Author).all()", query_author)

# Guardadndo la informacion en la BD
session.commit()

# se puede revertir todo
#session.rollback()

