class Carro:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self._velocidad = velocidad   # colocando _nameVairable hace que sea protected la variable
        self.__color = color  # colocando __nameVariable hace que sea privada la variable y solo se puede usar dentro de la clase

    """
    Por convencion para acceder o editar valores a atributos privados de clase
    se pueden usar funciones que inicien get_nameVarible y set_nameVariable
    
    publica: accede desde instancia, heradado y de clase
    protected: accede desde instancia heradado y de clase
    private: accede desde clase
    
    """
    def get_color(self):
        return self.__color

    def set_color(self, nuevo_color):
        self.__color = nuevo_color

    #__ antes de la funcion la privatiza
    def __funcion_privada(self):
        print("Funciona privada")

    #_ antes de la funcion la protege
    def _funcion_protegida(self):
        print("Funcion protegida")


carro1 = Carro('Chevrolet', 'Negro', 100)
print("carro1.marca", carro1.marca)
print("carro1.get_color()", carro1.get_color())
carro1.set_color('Dorado')
print("carro1.get_color()", carro1.get_color())
carro1._velocidad = 2;
print("carro1._velocidad", carro1._velocidad)


