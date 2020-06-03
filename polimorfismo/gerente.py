from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    def __str__(self):
        # usando super().nombreFuncion  accedemos a todas los metodos o atributos de la clase padre
        return super().__str__() + " , Departamento: " + self.departamento