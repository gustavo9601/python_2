class CasiillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    # @property
    # con este decorador se especifica que retornara una propiedad de clase
    @property
    def region(self):
        return self.__region

    # @name_attribute.setter
    # Denota que hay un setter par aun atributo
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en el {self.__pais}')



casilla_1 = CasiillaDeVotacion(123, ['Colombia'])
print("Region before set", casilla_1.region)
#casilla_1.region = 'Venezuela'
casilla_1.region = 'Colombia'
print("Region after set", casilla_1.region)
