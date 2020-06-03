from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden


raton1 = Raton("display port", "hp")
teclado1 = Teclado("cable", "compaq")
monitor1 = Monitor("samsung", "25 pulgadas")
computadora1 = Computadora("gamer", monitor1, teclado1, raton1)
computadora2 = Computadora("solo para trabajo", monitor1, teclado1, raton1)
computadora3 = Computadora("para programadores", monitor1, teclado1, raton1)

computadoras1 = [computadora1]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora2)
print(orden1)

computadoras2 = [computadora1, computadora3]
orden2 = Orden(computadoras2)
print(orden2)


