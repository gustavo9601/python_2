

"""
Las funcionts anotaciones, permiten definir el tipo de dato que recibe los parametros
y el que retornara, pero es solo a modo de documentacion, ya que no es estricto
Es util como documntacion

"""
def alimento(tipo: str, cantidad: int, valor: int ) -> str:
    print("Anotaciones", alimento.__annotations__)
    print("Argumentos", tipo, cantidad, valor)
    return f'Tipo {tipo}'

alimento('lacteo', 15, 500)