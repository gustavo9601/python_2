class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, Monitor, Teclado, Raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = Monitor
        self.__teclado = Teclado
        self.__raton = Raton

    def get_id_computadora(self):
        return self.__id_computadora

    def get_nombre(self):
        return self.__nombre

    def get_monitor(self):
        return self.__monitor

    def get_teclado(self):
        return self.__teclado

    def get_raton(self):
        return self.__raton

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_monitor(self, Monitor):
        self.__monitor = Monitor

    def set_teclado(self, Teclado):
        self.__teclado = Teclado

    def set_raton(self, Raton):
        self.__raton = Raton

    def __str__(self):
        return (
            f"""
                id: {self.__id_computadora}
                    nombre: {self.__nombre}
                    Monitor: {self.get_monitor().__str__()}
                    Teclado: {self.get_teclado().__str__()}
                    Raton: {self.get_raton().__str__()}
            """
        )
