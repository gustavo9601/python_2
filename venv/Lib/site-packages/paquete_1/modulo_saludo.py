class Saludos():
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return "Hola " + self.nombre