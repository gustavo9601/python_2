# importamos la libreria
import unittest


class NegativeValueError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeValueError("Numero negativo")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


class FactorialTest(unittest.TestCase):
    def test_factorial_negative(self):
        # .assertRaises(ClaseExpecion, funcion, parametro_function)  // comprobara si lanza un exepcnion
        self.assertRaises(NegativeValueError, factorial, -1)   # devolvera ok, ya que se le pasa un numero menor a 0

    def test_factorial_of_0(self):
        # .assertEqual(valor_que_debe_retornar, funcion)  // compara que el resultado sea el que se pasa por primer y segundo parametro
        self.assertEqual(0, factorial(1))

    def test_factorial_of_1(self):
        self.assertEqual(1, factorial(10))  # retornara false, ya que no cumple la condicion

if __name__ == '__main__':
    # llamamos la funcion propia de unitest para ejecutarlas
    unittest.main()