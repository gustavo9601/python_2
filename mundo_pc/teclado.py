from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados

    def __str__(self):
        return (
            f"id: {self.__id_teclado}  | tipo_entrada: {self.get_tipo_entrada()} | marca: {self.get_marca()}"
        )
