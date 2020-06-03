from random import randint


def lanzamiento_dados():
    print("***Bienvenido***")
    option = int(input(
        """
        Por favor seleccione una de las siguientes opciones
        1. Lanzar los dados
        2. Finalizar programa
        """))
    while option != 2:
        if option == 1:
            lanzamiento()
        option = int(input(
            """
            Por favor seleccione una de las siguientes opciones
            1. Lanzar los dados
            2. Finalizar programa
            """))


def lanzamiento():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    suma_dados = dado1 + dado2

    print(f"""*Resultado lanzamiento*
          Dado 1: {dado1}
          Dado 2: {dado2}
          Sumatoria lanzamiento: {suma_dados}""")


lanzamiento_dados()
