"""
Nested functions

Funciones anidadas dentro de otras
"""

def main():
    a = 1
    def nested():
        print(a)
    nested()
main()

"""
Clousures 
Acceso a variables de alcances superiores dedes niveles inferiores

- Debe tener un nested function
- La nested function debe referenciar un valor de un scope superior
- La funcion que envuelve al nested debe retornarla tambien
"""

def main_2():
    a = 2
    def nested():
        print(a)
    return nested

call_closure = main_2()
call_closure()

# Ejemplo
# Hola 3 -> HolaHolaHola

def make_repeater_of(n_times):
    def repeater(string):
        # assert // verifica la condicion y continua la ejecucion en caso contrario devolvera como error el
        # segundo parametro
        assert type(string) == str, "Only type strings are allowed"
        return string * n_times
    return repeater


# Pasa el primer parametro de la funcion
repeat_5 = make_repeater_of(5)
# Llamando a la variable que ya tiene en memoria el primer parametro, se envia
# el segundo parametro de la funcion nested
print(repeat_5('gus'))