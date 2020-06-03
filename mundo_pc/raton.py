from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones

    def __str__(self):
        # f formatea toda la cadena a string
        # se usta ("") ya que pueden ser varias lineas
        return (
            f"id: {self.__id_raton}  | tipo_entrada: {self.get_tipo_entrada()} | marca: {self.get_marca()}"
        )
