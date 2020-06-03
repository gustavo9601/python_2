class Monitor:
    contador_monitor = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitor += 1
        self.__id_monitor = Monitor.contador_monitor
        self.__marca = marca
        self.__tamanio = tamanio

    def get_id_monitor(self):
        return self.__id_monitor

    def get_marca(self):
        return self.__marca

    def get_tamanio(self):
        return self.__tamanio

    def set_marca(self, marca):
        self.__marca = marca

    def set_tamanio(self, tamanio):
        self.__tamanio = tamanio

    def __str__(self):
        return (
            f"id: {self.__id_monitor} | marca: {self.__marca} | tamaño: {self.__tamanio}"
        )
