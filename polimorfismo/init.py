"""
Polimorfismo, => hace referencia a las diferentes formas que podra tomar una variable al llamar diferentes clases o instancias
"""
from empleado import Empleado
from gerente import Gerente


# funcion que recibira como parametro una clase de tipo empleado "padre"
def imprimir_detalles(objeto_de_clase):
    #type resuleve el tipo de clase o tipo de objeto
    print(type(objeto_de_clase), objeto_de_clase)

    # isinstance(objeto, clase) permite saber si un objeto es instancia de una clase
    if isinstance(objeto_de_clase, Gerente):
        print("Es instancia de Gerente", end="\n\n")
    else:
        print("Es instancia de Empleado", end="\n\n")


empleado1 = Empleado('Gustavo', 3000000)
empleado2 = Empleado('Meliza', 500000)
imprimir_detalles(empleado1)
imprimir_detalles(empleado2)

empleado1 = Gerente('Gustavo', 3000000, 'Tecnologia')
imprimir_detalles(empleado1)
