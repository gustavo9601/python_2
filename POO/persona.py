class Persona:
    def __init__(self, nombre, edad, *args, **kwargs):
        self.nombre = nombre
        self.edad = edad
        self.tupla_valores = args
        self.diccionario_valores = kwargs

    def imprimir_nombre_edad(self):
        print(self.nombre, self.edad)


# Sin instancia el objeto
Persona.nombre = 'Gustavo'
Persona.edad = 24
print(Persona.nombre)

# Instancia de clase
persona1 = Persona('Meliza', 22, [1, 2, 3], 1, kwargs={'llave1' : 'valor1'})
persona1.imprimir_nombre_edad()
print("persona1.tupla_valores", persona1.tupla_valores)
print("persona1.diccionario_valores", persona1.diccionario_valores)
