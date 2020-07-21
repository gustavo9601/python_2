# Expresiones regulares
# Identificar busqueda de patrones en cadenas

# importa libreria
import re

texto = "En esta cadena se encuentra una palabra magica"

# re.search('valor de busqueda', 'cadena de texto)
# de encontrar algo retorna un valor en momoria, en caso contrario nada
encontrar_magica = re.search('magica', texto)
# .match("palabra buscar", texto)   // devuelve la posicion de memoria si encuentra el texto al prinicipio
print("encontrar_magica", encontrar_magica)

# .start() devuelve la posicion del string donde encontro la condicdencia
posicion_encuentra_conincidencia = encontrar_magica.start()
print("posicion_encuentra_conincidencia", posicion_encuentra_conincidencia)


# .end()  // posicion final de la palabra encontrada
# .span()  // retorna una tupla con la posicion inicial y final encontrada
# .string()  // devuelve la frase donde se encontro el patron
# .split(' ', texto)  // convierte el string a lista generada
# .sub('palabra',texto)  // sustituye el primer valor parametro en las coincidencias encontradas del texto
# .findall('palabra', texto)  // devuelve en un arreglo la palabra n cantidad de veces encontrada
    # .findall('palabra|palabra2', texto)  // devuelve en un arreglo la palabra n cantidad de veces encontradas


texto = "Hola hola HOoola hooola"

def buscar(patrones, texto):
    for patron in patrones:
        print("re.findall(patron, texto)", re.findall(patron, texto))

patrones = ['hola', 'hOLA', 'Hola']
buscar(patrones, texto)

# ho*  que empiecen o no en  ho y finalicen en ooo
# ho*la que empiecen en h con o sin ninguna conincdiencia de o, pero finalizado en la
patrones = ['ho', 'ho*', 'ho*la']
buscar(patrones, texto)



# ho+  que empiecen en ho
patrones = ['ho+']
buscar(patrones, texto)


# ho{0} la  que empiecen en h y que la o se repita 0 veces, luego que siga la
# ho{1,2} la  que empiecen en h y que la o se repita 1 a 2 veces y luego siga la
patrones = ['ho{0}la', 'ho{1,2}la']
buscar(patrones, texto)



# 'h[o]la' las que empiecen en h y seguido tengan los caracteres entre [] y finalice en la
# 'h[oui]la' las que empiecen en h y seguido tengan uno o mas caracteres dentro del [] y finalice en la
texto = 'hola hula hila Hila Hula hola HULA'
patrones = ['h[o]la', 'h[oui]la']
buscar(patrones, texto)

# 'h[ui]{1,3}la' que empiece en h y contenga alguna de los caracteres dentro del [] desde {1 hasta 3 veces}
texto = 'hola hula hila Hila Hula huuuuula huula HULA'
patrones = ['h[ui]{1,3}la']
buscar(patrones, texto)

# 'h[̂^u]la' que empiece en h pero que no le siga una u y que finalice en la
patrones = ['h[̂^u]la']
buscar(patrones, texto)

#/////////////////////
# Ranggos
# [A-Z] cualquier caracter alfabeto en mayuscula
# [a-z] cualquier caracter alfabeto en minuscula
# [A-Za-z] cualquier caracter alfabeto en mayuscula o minusucla
# [A-z] cualquier caracter alfabeto en mayuscula o minusucla
# [0-9] Cualquier caracter numerico
# [a-zA-Z0-9] Cualquier caracter alfanumerico

#Caracteres escapados
# \d numerico
# \D no numerico
# \s espacio en blanco
# \S no espacio en blanco
# \w alfanumerico
# \W no alfanuemrico
texto = 'hola hula hila Hila Hula huuuuula huula hUla h0la'
patrones = ['h[A-Z]la', 'h[0-9]la']
buscar(patrones, texto)

texto = 'hola hula hila Hila Hula huuuuula huula hUla h0la 123 s4s52s'
patrones = [r'\d']  # r permite decirle que el exto va en raw para soportar el back slas
buscar(patrones, texto)

#update.