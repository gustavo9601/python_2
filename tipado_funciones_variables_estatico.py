"""
Las funcionts anotaciones, permiten definir el tipo de dato que recibe los parametros
y el que retornara, pero es solo a modo de documentacion, ya que no es estricto
Es util como documntacion

"""


def alimento(tipo: str, cantidad: int, valor: int) -> str:
    print("Anotaciones", alimento.__annotations__)
    print("Argumentos", tipo, cantidad, valor)
    return f'Tipo {tipo}'


alimento('lacteo', 15, 500)



from typing import Dict, List, Tuple

# Lista de solo enteros
positives: List[int] = [1, 2, 3]

# Diccionario especificando la llave y el valor
countries: Dict[str, int] = {
    'colombia': 2,
    'ecuador': 10
}

users: List[Dict[str, str]] = [
    {
        'name': 'Gustavo',
        'age': 25
    }, {
        'name': 'Meliza',
        'age': 24
    }
]

class Human():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(f"Nombre: {self.name}")


humans : List[Human] = [
    Human('Gustavo'),
    Human('Meliza')
]

print(type(users))
print(type(humans))

# mypy

def is_palindrome(text: str) ->bool:
    text = text.replace(' ', '').lower()
    return text == text[::-1]

is_palindrome('s')

"""
Probando la validacion del tipado 
mypy tipado_funciones_variables_estatico.py --check-untyped-defs
"""