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
    estudiante = relationship('Estudiante', back_populates="curso")
    # relacion con horario
    horario_id = Column(Integer, ForeignKey('horario.id'))
    horario = relationship('Horario', back_populates="curso")

    def __repr__(self):
        return f"Curso id: {self.id} | Nombre Curso: {self.nombre} | Descripcion Curso: {self.descripcion}"


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
        return f"Profesor id: {self.id} | Nombre Profesor: {self.nombre}"


class Estudiante(Base):
    __tablename__ = 'estudiante'
    id = Column(Integer, Sequence('estudiante_id_seq'), primary_key=True)
    nombre = Column(String)

    # relacion uno a uno con Curso
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship('Curso', back_populates='estudiante')

    def __repr__(self):
        return f"Estudiante id: {self.id} | Nombre Estudiante: {self.nombre}"


class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    dia_semana = Column(String)
    hora_inicio = Column(String)
    hora_fin = Column(String)
    # relacion uno a uno con profesor
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    profesor = relationship('Profesor', uselist=False, back_populates='horario')

    curso = relationship('Curso', back_populates='horario')

    def __repr__(self):
        return f"Horario id: {self.id} | Dia semana: {self.dia_semana} | Hora Inicio: {self.hora_inicio} | Hora Fin: {self.hora_fin}"


if __name__ == '__main__':

    mensaje_bienvenida = """
    =============================================
    =============================================
    Bienvenido al Sistema de Escuelas Coursera GM
    =============================================
    =============================================
    """
    mensaje_menu_inicial = """
     Seleccione una de las siguientes opciones
           para interactuar con el menu
    =============================================
                    MENU INICIAL
    =============================================
    1. Menu creacion
    2. Menu de asociacion
    3. Menu de reportes
    4. Salir de la aplicacion
    =============================================
    """

    mensaje_menu_creacion = """
    =============================================
                  MENU CREACION
      Seleccione una de las siguientes opciones
    =============================================
    1. Crear curso
    2. Crear profesor
    3. Crear estudiante
    4. Crear horario
    5. Volver al menu anterior
    =============================================
    """

    mensaje_menu_asosiacion = """
    =============================================
                MENU ASOCIACION
      Seleccione una de las siguientes opciones
    =============================================
    1. Asociar a un curso un profesor
    2. Asociar a un estudiante un curso
    3. Asociar a un horario un curso
    4. Volver al menu anterior
    =============================================
        """

    mensaje_menu_reportes = """
    =============================================
                 MENU REPORTES
      Seleccione una de las siguientes opciones
    =============================================
    1. Listar cursos
    2. Listar profesores
    3. Listar estudiantes
    4. Listar horarios
    5. Listar alumnos por id curso
    6. Listar horarios por id profesor
    7. Listar horarios por id curso
    8. Volver al menu anterior
    =============================================
            """
    mensaje_invalido = """
    =============================================
                 OPCION INVALIDA
    =============================================
    """
    mensaje_rellenar_campos = """
    =============================================
           DILIGENCIE LOS SIGUIENTES CAMPOS
    =============================================
    """
    mensaje_despedida = """
        =============================================
            !!! GRACIAS POR USAR EL SISTEMA !!!
        =============================================
        """


    def imprimir_cursos(session):
        print("======================================")
        print("Lista de cursos")
        print("======================================")
        for row in session.query(Curso).all():
            print(row)


    def imprimir_profesores(session):
        print("======================================")
        print("Lista de profesores")
        print("======================================")
        for row in session.query(Profesor).all():
            print(row)


    def imprimir_estudiantes(session):
        print("======================================")
        print("Lista de estudiantes")
        print("======================================")
        for row in session.query(Estudiante).all():
            print(row)


    def imprimir_horarios(session):
        print("======================================")
        print("Lista de horarios")
        print("======================================")
        for row in session.query(Horario).all():
            print(row)


    def menu():
        print(mensaje_bienvenida)
        opcion_inicial = int(input(mensaje_menu_inicial))

        # Crea el esquema
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        while not opciones_validas(1, 5, opcion_inicial):
            print(mensaje_invalido)
            opcion_inicial = int(input(mensaje_menu_inicial))

        while opcion_inicial != 4:
            if opcion_inicial == 1:
                opcion_creacion = int(input(mensaje_menu_creacion))
                while not opciones_validas(1, 6, opcion_creacion):
                    opcion_creacion = int((input(mensaje_menu_creacion)))
                    # creacion curso
                if opcion_creacion == 1:
                    print(mensaje_rellenar_campos)
                    nombre_curso = input("Nombre del curso: ")
                    descripcion_curso = input("Descripcion del curso: ")
                    nuevo_curso = Curso(nombre=nombre_curso, descripcion=descripcion_curso)
                    session.add(nuevo_curso)
                    # creacion profesor
                elif opcion_creacion == 2:
                    print(mensaje_rellenar_campos)
                    nombre_profesor = input("Nombre del profesor: ")
                    nuevo_profesor = Profesor(nombre=nombre_profesor)
                    session.add(nuevo_profesor)
                    # crear estudiante
                elif opcion_creacion == 3:
                    print(mensaje_rellenar_campos)
                    nombre_estudiante = input("Nombre del estudiante: ")
                    nuevo_estudiante = Estudiante(nombre=nombre_estudiante)
                    session.add(nuevo_estudiante)
                    # crear horario
                elif opcion_creacion == 4:
                    print(mensaje_rellenar_campos)
                    dia_semana_horario = input("Dia de la semana (Lunes a Domingo): ")
                    hora_inicio_horario = input("Hora de inicio (HH:MM): ")
                    hora_fin_horario = input("Hora de Fin (HH:MM): ")
                    nuevo_horario = Horario(dia_semana=dia_semana_horario, hora_inicio=hora_inicio_horario,
                                            hora_fin=hora_fin_horario)
                    session.add(nuevo_horario)
                    # Volver al menu anterior
                elif opcion_creacion == 5:
                    opcion_inicial = int(input(mensaje_menu_inicial))
                    while not opciones_validas(1, 6, opcion_inicial):
                        print(mensaje_invalido)
                        opcion_inicial = int(input(mensaje_menu_inicial))
                    # opcion invalida
                else:
                    print(mensaje_invalido)
                    opcion_inicial = int(input(mensaje_menu_inicial))
                    while not opciones_validas(1, 6, opcion_inicial):
                        print(mensaje_invalido)
                        opcion_inicial = int(input(mensaje_menu_inicial))
            elif opcion_inicial == 2:
                opcion_asociacion = int(input(mensaje_menu_asosiacion))
                while not opciones_validas(1, 6, opcion_asociacion):
                    opcion_asociacion = int((input(mensaje_menu_asosiacion)))

                # Asociar a un curso un profesor
                if opcion_asociacion == 1:
                    if session.query(Curso).count() > 0:
                        print("Por favor digite el ID de uno de los siguientes cursos:")
                        imprimir_cursos(session)
                        id_curso = int(input())
                        curso = session.query(Curso).filter(Curso.id == id_curso).first()
                        if curso:
                            if session.query(Profesor).count() > 0:
                                print("Por favor digite el ID de uno de los siguientes profesores")
                                imprimir_profesores(session)
                                id_profesor = int(input())
                                profesor = session.query(Profesor).filter(Profesor.id == id_profesor).first()
                                if profesor:
                                    curso.profesor.append(profesor)
                                else:
                                    print("*******Profesor no encontrado*****")
                            else:
                                print("*****No hay profesores creados****")
                        else:
                            print("*******Curso no encontrado*****")
                    else:
                        print("*****No hay cursos creados****")
                # Asociar a un estudiante un curso
                elif opcion_asociacion == 2:
                    if session.query(Estudiante).count() > 0:
                        print("Por favor digite el ID de uno de los siguientes estudiantes:")
                        imprimir_estudiantes(session)
                        id_estudiante = int(input())
                        estudiante = session.query(Estudiante).filter(Estudiante.id == id_estudiante).first()
                        if estudiante:
                            if session.query(Curso).count() > 0:
                                print("Por favor digite el ID de uno de los siguientes cursos")
                                imprimir_cursos(session)
                                id_curso = int(input())
                                curso = session.query(Curso).filter(Curso.id == id_curso).first()
                                if curso:
                                    estudiante.curso = curso
                                else:
                                    print("*******Curso no encontrado*****")
                            else:
                                print("*****No hay cursos creados****")
                        else:
                            print("*******Estudiante no encontrado*****")
                    else:
                        print("*****No hay estudiantes creados****")
                # Asociar a un horario un curso
                elif opcion_asociacion == 3:
                    if session.query(Horario).count() > 0:
                        print("Por favor digite el ID de uno de los siguientes horarios:")
                        imprimir_horarios(session)
                        id_horario = int(input())
                        horario = session.query(Horario).filter(Horario.id == id_horario).first()
                        if horario:
                            if session.query(Curso).count() > 0:
                                print("Por favor digite el ID de uno de los siguientes cursos")
                                imprimir_cursos(session)
                                id_curso = int(input())
                                curso = session.query(Curso).filter(Curso.id == id_curso).first()
                                if curso:
                                    curso.horario = horario
                                else:
                                    print("*******Curso no encontrado*****")
                            else:
                                print("*****No hay cursos creados****")
                        else:
                            print("*******Horario no encontrado*****")
                    else:
                        print("*****No hay horarios creados****")
                elif opcion_asociacion == 4:
                    opcion_inicial = int(input(mensaje_menu_inicial))
                    while not opciones_validas(1, 5, opcion_inicial):
                        print(mensaje_invalido)
                        opcion_inicial = int(input(mensaje_menu_inicial))
                else:
                    print(mensaje_invalido)
                    opcion_inicial = int(input(mensaje_menu_inicial))
                    while not opciones_validas(1, 5, opcion_inicial):
                        print(mensaje_invalido)
                        opcion_inicial = int(input(mensaje_menu_inicial))
            elif opcion_inicial == 3:
                opcion_reportes = int(input(mensaje_menu_reportes))
                while not opciones_validas(1, 9, opcion_reportes):
                    opcion_reportes = int((input(mensaje_menu_reportes)))
                # Listar cursos
                if opcion_reportes == 1:
                    imprimir_cursos(session)
                # listar profesores
                elif opcion_reportes == 2:
                    imprimir_profesores(session)
                # Listar estudiantes
                elif opcion_reportes == 3:
                    imprimir_estudiantes(session)
                # listar horarios
                elif opcion_reportes == 4:
                    imprimir_horarios(session)
                # Listar alumnos por id curso
                elif opcion_reportes == 5:
                    print("Por favor digite el ID de uno de los siguientes cursos:")
                    imprimir_cursos(session)
                    id_curso = int(input())
                    curso = session.query(Curso).filter(Curso.id == id_curso).first()
                    if curso:
                        print("======================================")
                        print("Lista de estudiantes por el ID de curso: " + str(id_curso))
                        print("======================================")
                        for rowE, rowC in session.query(Estudiante, Curso).join(Curso).filter(
                                Curso.id == id_curso).all():
                            print(rowE, '|', rowC)
                    else:
                        print("*******Curso no encontrado*****")
                # Listar horarios por id profesor
                elif opcion_reportes == 6:
                    print("Por favor digite el ID de uno de los siguientes profesores:")
                    imprimir_profesores(session)
                    id_profesor = int(input())
                    profesor = session.query(Profesor).filter(Profesor.id == id_profesor).first()
                    if profesor:
                        print("======================================")
                        print("Lista de horarios por el ID de profesor: " + str(id_profesor))
                        print("======================================")
                        for rowP, rowC, rowH in session.query(Profesor, Curso, Horario).filter(
                                Profesor.id == id_profesor).filter(
                            Profesor.curso_id == Curso.id).filter(
                            Curso.horario_id == Horario.id).all():
                            print(rowP, '|', rowC, '|', rowH)
                    else:
                        print("*******Profesor no encontrado*****")
                # Listar horarios por id curso
                elif opcion_reportes == 7:
                    print("Por favor digite el ID de uno de los siguientes cursos:")
                    imprimir_cursos(session)
                    id_curso = int(input())
                    curso = session.query(Curso).filter(Curso.id == id_curso).first()
                    if curso:
                        print("======================================")
                        print("Lista de horarios por el ID de curso: " + str(id_curso))
                        print("======================================")
                        for rowC, rowH in session.query(Curso, Horario).join(Horario).filter(
                                Curso.id == id_curso).all():
                            print(rowC, '|', rowH)
                    else:
                        print("*******Curso no encontrado*****")
                # volver al menu anterior
                elif opcion_reportes == 8:
                    opcion_inicial = int(input(mensaje_menu_inicial))
                    while not opciones_validas(1, 6, opcion_inicial):
                        print(mensaje_invalido)
                        opcion_inicial = int(input(mensaje_menu_inicial))
                else:
                    print(mensaje_invalido)
                    opcion_inicial = int(input(mensaje_menu_inicial))
                    while not opciones_validas(1, 6, opcion_inicial):
                        print(mensaje_invalido)
                        opcion_inicial = int(input(mensaje_menu_inicial))
            elif opcion_inicial == 4:
                print(mensaje_despedida)
            else:
                print(mensaje_invalido)


    def opciones_validas(desde, hasta, opcion):
        for op in range(desde, hasta):
            if opcion == op:
                return True
        return False


    menu()
