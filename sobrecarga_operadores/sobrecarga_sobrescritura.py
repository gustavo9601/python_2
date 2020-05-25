"""
Sobrecarga de operadores, denota los diferentes comportamientos que tiene un operador
en funcion del valor antes y despues del oeprador, añadiendo nuevas funcionalidades
"""
# + es un ejemplo de sobrecarga

# suma
print(1 + 2)
# concatena
print("Hola " + "Mundo")
# une listas
print([1, 2, 3] + [4, 5, 6])


class Marcas:
    def __init__(self, nombre):
        self.nombre = nombre

    # el metodo __add__ controla el comportamiento al sumar la instancia de esta clase + otra
    # para este caso se sobrescribe al compontamiento por default
    def __add__(self, other):
        return self.nombre + " " + other.nombre

    # __sub__ operacion de resta
    def __sub__(self, other):
        return "Operacion no soportada"


marca1 = Marcas("Mango")
marca2 = Marcas("Chaevignon")
# al modificar el componetamietno del __add__ de la clase, permite retorna concatenado los valores de clase
print("marca1 + marca2", marca1 + marca2)
print("marca1 - marca2", marca1 - marca2)
