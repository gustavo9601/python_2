from typing import Dict, List, Tuple

"""
pip install mypy

# Validar archivo

mypy archivo.py --check-untyped-defs
 
"""

a: int = 5
b: float = 50.0
c: bool = True

print("a, b, c: ", a, b, c)
print("type(a), type(b), type(c): ", type(a), type(b), type(c))


def suma(a: int, b: float) -> float:
    return a + b


print(f"suma {a} + {b}: ", suma(a, b))

# Tipado de listas
list_positives: List[int] = [1, 2, 3]
print("list_positives:", list_positives)

numbers: Tuple[int, float, int] = (1, 0.5, 1)
print("numbers:", numbers)

# Especificando un diccionario especificando el tipo de datos de llaves y el de los valores
users: Dict[str, int] = {
    'country_code': 1,
    'test': 2
}
print("users:", users)

# Especificando una lista con un tipo de dato diccionario
countries: List[Dict[str, str]] = [
    {
        'name': 'Gustavo',
        'age': '25'
    },
    {
        'name': 'Meliza',
        'age': '23'
    }
]
print("countries:", countries)


def is_palindrome(text: str) -> bool:
    text = text.replace(" ", "").lower()
    return text == text[::-1]
print("is_palindrome()", is_palindrome('Ana'))