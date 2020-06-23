from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey, Table, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    # relacion profesor
    profesor = relationship('Profesor', back_populates="curso")

    # relacion estudiante
    estudiante = relationship('Estudiante', uselist=False, back_populates="curso")
    # relacion con horario
    horario = relationship('Horario', uselist=False, back_populates="curso")

    def __repr__(self):
        return f"Curso id: {self.id} | Nombre: {self.nombre} | Descripcion: {self.descripcion}"


class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre = Column(String)
    # Releacion uno a muchos con Curso
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship('Curso', back_populates="profesor")

    # relacion con horario
    horario = relationship('Horario', uselist=False, back_populates="profesor")

    def __repr__(self):
        return f"Profesor id: {self.id} | Nombre: {self.nombre}"


class Estudiante(Base):
    __tablename__ = 'estudiante'
    id = Column(Integer, Sequence('estudiante_id_seq'), primary_key=True)
    nombre = Column(String)

    # relacion uno a uno con Curso
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship('Curso', uselist=False, back_populates='estudiante')

    def __repr__(self):
        return f"Estudiante id: {self.id} | Nombre: {self.nombre}"

class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    dia_semana = Column(String)
    hora_inicio = Column(String)
    hora_fin = Column(String)
    #relacion uno a uno con profesor
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    profesor = relationship('Profesor', uselist=False, back_populates='horario')
    # relacion uno a uno con Curso
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship('Curso', uselist=False, back_populates='horario')



    def __repr__(self):
        return f"Horario id: {self.id} | Dia semana: {self.dia_semana} | Hora Inicio: {self.hora_inicio} | Hora Fin: {self.hora_fin}"



if __name__ == '__main__':
    # Crea el esquema
    Base.metadata.create_all(engine)

    curso1 = Curso(nombre='PHP', descripcion='Solo web')
    #print("curso1", curso1)

    profesor1 = Profesor(nombre='Gustavo', curso=curso1)
    #print("profesor1", profesor1)

    profesor2 = Profesor(nombre='Meliza', curso=curso1)
    #print("profesor2", profesor2)

    estudiante1 = Estudiante(nombre='Jose', curso=curso1)
    #print("estudiante1", estudiante1)

    horario1 = Horario(dia_semana='lunes', hora_inicio='01:00', hora_fin='02:00', profesor=profesor1)
    #print("horario1", horario1)

    # Creando la sesion para manipular la data
    Session = sessionmaker(bind=engine)

    session = Session()
    # add_all(arreglo de objetos de la clase)  // añade mulitples registros
    session.add_all([curso1, profesor1, profesor2, estudiante1])

    print(session.query(Curso).all()[0].profesor[0].horario)
