# Al multiplicar un string, genera n veces el mismo string
text_espacios = " " * 10
print( text_espacios + "text_espacios")

name = "Gustavo"
msm = "El nombre es %s" % name
print(msm)

numero = 5.2
msm = "El numero es %.5f" % numero
print(msm)

texto = "Hello world"
msm = "{}".format(texto)
print(msm)

# formateando a decimal   {:f}  {:10f}  cantidad_decimales F
msm_decimal = "{:f} + {:10f} = {result:0f}".format(5, 10, result=15)
print("msm_decimal", msm_decimal)

# Formateando un texto, y agregando espacios si no cumple con el valor
# {name:15}  # variable:cantidad_espacios a completar
# {name:<15}  <15  indica hacia donde pondra los espacios
# {name:*>15-}  *>  indica hacia donde pondra los espacios y con que caracter o letra rellenara
msm_espacios = "Hola {name:15}".format(name='Gustavo')
print("msm_espacios", msm_espacios)
msm_espacios = "Hola {name:*>15}".format(name='Gustavo')
print("msm_espacios", msm_espacios)
"""
Concatenando los elementos de una lista
'separador'.join(lista[])
"""
msm = ' '.join(['Hola', name])
print("msm", msm)

""" 
Trasnformaciones de strings
"""

s2 = " Prueba Full"
print("capitalize", s2.capitalize())
print("lower", s2.lower())
print("upper", s2.upper())
print("strip", s2.strip())
print("strip", s2.strip("-"))
print("split", s2.split(" "))
print("swapcase", s2.swapcase())
print("title", s2.title())
print("replace('u', 's')", s2.replace('u', 's'))
print("center(16)", s2.center(16))
print("zfill(16)", s2.zfill(16))

"""
Analizar cadenas de texto
"""
texto = "Hello World 2020"
print('texto.count("o")', texto.count("o"))
print('texto.startswith("H")', texto.startswith("H"))
print('texto.endswith("h")', texto.endswith("h"))
print('texto.find("llo")', texto.find("llo"))
print('texto.index("l")', texto.index("l"))
print('texto.rfind("l")', texto.rfind("l"))
print('texto.rindex("l")', texto.rindex("l"))
print('texto.isdecimal()', texto.isdecimal())
print('texto.isdigit()', texto.isdigit())
print('texto.islower()', texto.islower())
print('texto.isupper()', texto.isupper())
print('texto.isspace()', texto.isspace())
print('texto.isalpha()', texto.isalpha())
print('texto.isalnum()', texto.isalnum())
