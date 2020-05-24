class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empresa:
    def __init__(self, company, nit):
        self.company = company
        self.nit = nit


#class NombreClase(ClaseAHeredar)
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        #super() accede a todas las propieades del padre
        #le pasamamos los parametors que recibe el padre, para que se inicialice correctamente
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    # sobrescribiendo el metodo __str__  el cual por default retorna la posicion de moemira de la clase
    def __str__(self):
        return "nombre => " + self.nombre + ", edad => " + str(self.edad) + ", sueldo => " + str(self.sueldo)


class Empleado2(Empresa, Persona):
    def __init__(self, company, nit, nombre, edad):
        # Cuando es herencia multiple se pueden pasar parametro llamando directamente a la clase
        # es necesario enviar el self, como el this de clase cuando hace referencia directa a las clases padre
        Empresa.__init__(self, company, nit)
        Persona.__init__(self, nombre, edad)


    def __str__(self):
        return self.company + " " + str(self.nit) + " " + self.nombre + " " + str(self.edad)

empleado1 = Empleado('Gustavo', 24, 3500000)
print(empleado1.nombre)
print(empleado1)

empleado2 = Empleado2('Microsft', 1212121, 'Meliza', 21)
print(empleado2)