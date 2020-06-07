class Jugador:

    def __init__(self, nombre=None, estado=None, caracter=None):
        self.nombre = nombre
        self.estado = estado
        self.caracter = caracter

    def __str__(self):
        return f"Nombre jugador: {self.nombre} | estado: {self.estado}"


class Tateti:
    matriz = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]

    @classmethod
    def resetear_matriz(cls):
        cls.matriz = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ]

    @classmethod
    def imprimir_matriz(cls):
        print(f"""
          |0|1|2|
        |0|{cls.matriz[0][0]}|{cls.matriz[0][1]}|{cls.matriz[0][2]}|
        |1|{cls.matriz[1][0]}|{cls.matriz[1][1]}|{cls.matriz[1][2]}|
        |2|{cls.matriz[2][0]}|{cls.matriz[2][1]}|{cls.matriz[2][2]}|
        """)

    @classmethod
    def editar_matriz(cls, x, y, caracter):
        cls.matriz[x][y] = caracter

    @classmethod
    def posicion_valida(cls, x, y):
        if x >= 0 and x <= 2 and y >= 0 and y <= 2:
            return True
        else:
            return False

    @classmethod
    def posicion_disponible(cls, x, y):
        if cls.matriz[x][y] != '_':
            return False
        else:
            return True

    @classmethod
    def matriz_disponible(cls):
        for lista_matriz in cls.matriz:
            if '_' in lista_matriz:
                return True
        return False

    @classmethod
    def validar_ganador(cls, caracter):
        "Validacion filas"
        for lista_matriz in cls.matriz:
            if lista_matriz[0] == caracter and lista_matriz[1] == caracter and lista_matriz[2] == caracter:
                return True
        "Validacion columnas"
        if (cls.matriz[0][0] == caracter and cls.matriz[1][0] == caracter and cls.matriz[2][0] == caracter) or (
                cls.matriz[0][1] == caracter and cls.matriz[1][1] == caracter and cls.matriz[2][1] == caracter) or (
                cls.matriz[0][2] == caracter and cls.matriz[1][2] == caracter and cls.matriz[2][2] == caracter):
            return True

        "Validacion diagonal"
        if (cls.matriz[0][0] == caracter and cls.matriz[1][1] == caracter and cls.matriz[2][2] == caracter) or (
                cls.matriz[2][0] == caracter and cls.matriz[1][1] == caracter and cls.matriz[0][2] == caracter):
            return True
        return False


def jugar_tateti():
    nombre_jugador_1 = input("Por favor digite el nombre para el Jugador # 1: ")
    nombre_jugador_2 = input("Por favor digite el nombre para el Jugador # 2: ")

    jugador_1 = Jugador(nombre=nombre_jugador_1, estado='Empate', caracter='X')
    jugador_2 = Jugador(nombre=nombre_jugador_2, estado='Empate', caracter='O')

    jugadores = [jugador_1, jugador_2]
    Tateti.imprimir_matriz()
    while Tateti.matriz_disponible():

        for jugador in jugadores:
            print(f"Turno jugador - {jugador.nombre} [{jugador.caracter}]")
            x = int(input("Posicion fila (0-2): "))
            y = int(input("Posicion columna (0-2): "))

            while not Tateti.posicion_valida(x, y):
                print("Posicion invalida, por favor intente de nuevo")
                x = int(input("Posicion fila (0-2): "))
                y = int(input("Posicion columna (0-2): "))

            while not Tateti.posicion_disponible(x, y):
                print("Posicion ocupada, por favor intente de nuevo")
                x = int(input("Posicion fila (0-2): "))
                y = int(input("Posicion columna (0-2): "))
                while not Tateti.posicion_valida(x, y):
                    print("Posicion invalida, por favor intente de nuevo")
                    x = int(input("Posicion fila (0-2): "))
                    y = int(input("Posicion columna (0-2): "))

            Tateti.editar_matriz(x, y, jugador.caracter)
            Tateti.imprimir_matriz()
            if Tateti.validar_ganador(jugador.caracter):
                jugador.estado = 'Ganador'
                print(f"Felicidades el Jugador - {jugador.nombre} a Ganado!!!")
                Tateti.resetear_matriz()
                return
            if not Tateti.matriz_disponible():
                print("***No hay casillas disponibles - Empate!!!!***")
                print(jugadores[0])
                print(jugadores[1])
                Tateti.resetear_matriz()
                return



def menu_tateti():
    print("**********************************")
    print("**********************************")
    print("Bienvenido al Juego TaTeTi")
    print("Por favor seleccione una de las siguientes opciones")
    opcion = None

    while opcion != 2:
        opcion = input("""
            1. Jugar
            2. Salir del programa
            """)
        if int(opcion) == 1:
            jugar_tateti()
        elif int(opcion) == 2:
            print("Gracias por jugar TaTeTi")
            return
        else:
            print("Opcion invalida. Por favor seleccione una de las siguientes:")


menu_tateti()

