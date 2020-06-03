class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def get_tipo_entrada(self):
        return self._tipo_entrada

    def get_marca(self):
        return self._marca

    def set_tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    def set_marca(self, marca):
        self._marca = marca