"""
Uso de breakpoints para ir analizando los valores y ejecucion del programa


Comando Descripción
h(elp) Muestra la ayuda de todos los comandos que provee pdb.
s(tep) Ejecuta la línea actual. Si en la línea actual hay una llamada de función se
mete dentro del código de la función para poder seguir la ejecución de la
misma.
n(ext) Continúa la ejecución hasta la próxima línea.
r(eturn) Continúa la ejecución hasta el return de la función actual.
c(ont(inue)) Continúa la ejecución hasta le próximo breakpoint. Si no hay otro
breakpoint. Ejecutará hasta el fin del programa.
l(ist) Muestra el código del archivo actual.
p Evalúa la expresión pasada como parámetro, la evalua en el contexto
actual e imprime su valor.
q(uit) Sale del depurador. El programa es abortado.

"""

import pdb


print("hola")

# pdb.set_trace() generera el break point
pdb.set_trace()
print("mundo")