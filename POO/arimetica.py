class Arimetica:
    """Clase arimetica para realizar las operaciones # sirve para documentar la clase"""
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def sumar(self):
        return self.val1 + self.val2

    def restar(self):
        return self.val1 - self.val2


arimetica1 = Arimetica(10, 50)
print("arimetica1.sumar()", arimetica1.sumar())
print("arimetica1.restar()", arimetica1.restar())
