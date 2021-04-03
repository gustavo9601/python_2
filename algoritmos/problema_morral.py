def morral(tamano_morral, pesos, valores, n):


    print(f"tamano_morral: {tamano_morral} | pesos {pesos} | | valores {valores}")

    if n == 0 or tamano_morral == 0:
        return 0

    # Verifica si en la posicion actual, supera el limite del morral, entonces
    # Verifica en la siguiente posicion de forma recursiva
    if pesos[n - 1] > tamano_morral:
        # pasand n - 1 se va a la posicion anterior
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
               morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print("Los valores maximos a escoger en la maleta son", resultado)
