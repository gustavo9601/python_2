from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()


# Definimos la clase con los elementos que componen la tabla
class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    # Relacion con book
    books = relationship('Book', order_by='Book.id', back_populates='author', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

# Tabla de asosiacion o pivote
book_categories = Table('book_categories', Base.metadata,
                        Column('book_id', ForeignKey('book.id'), primary_key=True),
                        Column('category_id', ForeignKey('book_category.id'), primary_key=True)
                        )


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    isbn = Column(String)
    title = Column(String)
    description = Column(String)
    # Llave foranea
    author_id = Column(Integer, ForeignKey('author.id'))

    # relacion con tabla author
    author = relationship('Author', back_populates='books')
    #relacion pivote enre book y categories
    categories = relationship('BookCategory', secondary=book_categories, back_populates='books')

    def __repr__(self):
        return f"{self.title}"



class BookCategory(Base):
    __tablename__ = 'book_category'
    id = Column(Integer, Sequence('book_category_id_ses'), primary_key=True)
    name = Column(String)

    books = relationship('Book',
                         secondary=book_categories,
                         back_populates='categories')
    def __repr__(self):
        return f"{self.name}"



# Crea el esquema
Base.metadata.create_all(engine)

author1 = Author(firstname='Gustavo', lastname='Marquez')
author2 = Author(firstname='Laura', lastname='Prieto')

# Creando la sesion para manipular la data
Session = sessionmaker(bind=engine)

session = Session()
# add_all(arreglo de objetos de la clase)  // añade mulitples registros
session.add_all([author1, author2])

# Consultas

# .order_by(Clase.columna)
for author in session.query(Author).order_by(Author.id):
    print(author.firstname, author.lastname)

# session.query(Author.firstname, Author.lastname)  devuelve solo las columnas pasadas por parametro
for firstname, lastname in session.query(Author.firstname, Author.lastname):
    print(firstname, lastname)

# .all()
for row in session.query(Author).all():
    print(row)

# [1:3]  hace el slice de la lista de acuerdo a los registros
for row in session.query(Author).all()[1:3]:
    print(row)

# session.query(Author.firstname.label('firstname_label')).all()  // añade una etiqueta a la columan para hacer refrencia
for row in session.query(Author.firstname.label('firstname_label')).all():
    print(row.firstname_label)

# aliased(Author, name="author_alias")  # permite dar un alias al nombre de la clase para acceder
author_alias = aliased(Author, name="author_alias")
for row in session.query(author_alias).all():
    print(row)

# .filter_by(firstname='Gustavo', kwargs):   // filtra por los parametros pasados
for row in session.query(Author).filter_by(firstname='Gustavo'):
    print(row)

# .count() retorna la cantidad de registros retornados
cantidad_registros_retornados = session.query(Author).filter_by(firstname='Gustavo').count()
print("cantidad_registros_retornados", cantidad_registros_retornados)

"""
Creando objetos relacionales
"""
author3 = Author(firstname='Martha', lastname='Gutierrez')
# usando la relacion de autor, podemos insertar inmediatamente el registro, ya relacionado al id de author
author3.books = [
    Book(isbn='123456', title='Harry Potter', description='bla bla de harry'),
    Book(isbn='123457', title='La camara', description='Erase una vez')
]

session.add(author3)
session.commit()

# imprimiendo los libros, para el author con firstname='Martha'
print(session.query(Author).filter_by(firstname='Martha').one().books)

# filtra dos tblas, por id e isbn
for an_author, a_book in session.query(Author, Book).filter(Author.id == 3).filter(Book.isbn == '123456').all():
    print(an_author, '=>', a_book)

# Join
print(session.query(Author).join(Book).filter(Book.isbn == '123456').all())

# Join con condicion implicita de ids
print(session.query(Author).join(Book, Author.id == Book.author_id).all())

# Filtra los autores con like
print(session.query(Author).filter(Author.lastname.like('%Prieto%')).all())

"""
Relaciones muchos a muchos
"""
author4 = Author(firstname='Jose', lastname='Miranda')
session.add(author4)

book = Book(isbn='55084467', title='Full libro code', description='solo para programadores')

categoria1 = BookCategory(name='Desarrollo')
categoria2 = BookCategory(name='Software')

book.categories.append(categoria1)
book.categories.append(categoria2)

book.author = author4

print(session.query(Book).filter(Book.categories.any(name='Desarrollo')).all())

"""
Eliminado un objeto
"""
session.delete(author3)  # recibe el objeto que se desea eliminar
print(session.query(Author).all())
