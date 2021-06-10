import math

"""
Constantes
"""
# Numero pi
print("math.pi", math.pi)

# Numero e
print("math.e", math.e)

"""
Redondeos
"""
x = 2.75
# remueve la parte decimal
cortar_decimales = math.trunc(x)
print("cortar_decimales", cortar_decimales)
round_low = math.floor(x)
print(f'redondeo inferior', round_low)
round_upper = math.ceil(x)
print(f'redondeo superior', round_upper)

"""
Potencia, raices, logaritmos
"""
potencia = math.pow(2, 5)
print(f'potencia: {potencia}')
raiz_cuadrada = math.sqrt(16)
print(f'raiz_cuadrada: {raiz_cuadrada}')
log_natarual = math.log(math.e)
print(f'log_natural: {log_natarual}')

"""
MCD (Maximo comun divisor) y MCM (Minimo comun multiplo)
"""
x = 250
y = 100

# Maximo comun divisor
print("math.gcd", math.gcd(x, y))


def lcm(x, y):
    # fabs() // valor absolute
    return math.trunc(math.fabs(x * y) // math.gcd(x, y))


# Minimo comun multiplo
print("math.lcm", lcm(x, y))

"""
Combinatorias
"""

num_factorial = 5
print("factorial: ", math.factorial(num_factorial))


def choose(n, k):
    if (n >= k and k >= 0):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    else:
        return "No se puede calcular el numero factorial indicado"


# Ejemplo
# De un grupo de 10 personas, se escogen aletaroiamente parejas, cuantas parejas posibles se pueden formar
print("choose", choose(10, 2))

"""
Valor absoluto y Signo
"""
x = -500
# removueve valores absolutos para enteors y float
print("math.fabs", math.fabs(x))

# obtiene el valor absoluto del primer parametro y el signo del segundo parametro
# funcion de trasnferencia
x = 60
y = -100
print("math.copysign", math.copysign(x, y))

"""
Funciones Trigonometricas
# Math usa radianes, pero se puede trasnformar de grados a radianes
"""

n_grados = 90
n_radianes = math.radians(n_grados)
print("n_grados > ", n_grados, " | n_radianes > ", n_radianes)

n_radianes_to_grados = math.degrees(n_radianes)
print("n_radianes_to_grados", n_radianes_to_grados)

print("math.sin", math.sin(n_radianes))
print("math.cos", math.cos(n_radianes))
print("math.tan", math.tan(n_radianes))

print("math.asin", math.asin(1))
print("math.acos", math.acos(1))
print("math.atan", math.atan(1))

"""
Funcione shiperbolicas
# Se debe pasar en radianes
"""
# math.sinh // seno hiperbolico
print("math.sinh", math.sinh(math.pi))
print("math.cosh", math.cosh(math.pi))
print("math.tanh", math.tanh(math.pi))
print("math.asinh", math.asinh(math.pi))
print("math.acosh", math.acosh(math.pi))
# print("math.atanh", math.atanh(math.pi))

"""
Funciones de aproximaciones
"""
# Es cercano el primer parametro al segundo paraemtro
print("math.isclose", math.isclose(4, 4.0000001))
# rel_tol // [0 a 1] indicara el nivel de tolerancia minima
print("math.isclose with rel_to", math.isclose(4, 4.0000001, rel_tol=0.5))
# devuelve si es un numero infinito
print("math.isinf", math.isinf(math.inf))
# devuelve si es nan
print("math.isnan", math.isnan(math.nan))

"""
Funciones especiales
"""

# Funcion de error
print("math.erf", math.erf(25 / math.sqrt(2)))

# Funcion complementario del error
print("math.erfc", math.erfc(25 / math.sqrt(2)))

# Funcion gamma de euler
print("math.gamma", math.gamma(3))

# Funcion logaritmo neperiano del valor de la funcion de Gamma
print("math.lgamma", math.lgamma(3))
