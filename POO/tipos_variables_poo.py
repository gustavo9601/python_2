class MiClase:

    #variable de clase
    variable_de_clase = "Variable de clase"

    def __init__(self, variable_de_instancia):
        # variable de instancia
        self.variable_de_instancia = variable_de_instancia

    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")

    # la diferencia es que los metodos de clase, reciben el this te clase como parametro, pero n orequiere instancia
    @classmethod
    def metodo_de_clase(cls):
        print("Metodo de clase")


# Con variables de clase, se puede acceder directamente a la variable sin instanciua
# Es la homologacion a variables estaticas

print("MiClase.variable_de_clase", MiClase.variable_de_clase)

clase1 = MiClase("Variable instancia")
clase1.variable_de_clase = "Cambio de valor en variable de clase"
print("clase1.variable_de_instancia", clase1.variable_de_instancia)
print("clase1.variable_de_clase", clase1.variable_de_clase)

# Los metodos de clase estaticos, no necesitan instancia
MiClase.metodo_estatico()
MiClase.metodo_de_clase()
