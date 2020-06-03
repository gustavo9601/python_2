class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = computadoras

    def agregar_computadora(self, Computadora):
        self.__computadoras.append(Computadora)

    def __str__(self):
        str_computadoras = ""
        for computadora in self.__computadoras:
            str_computadoras += (computadora.__str__() + "\n")
        return (
            f"""id _orden :{self.__id_orden}
                computadoras :
                {str_computadoras}"""
        )
