#Santiago Yeomans
#A01251000
def main():

    def a_musulman(año_gregoriano):
        """
        Esta funcion convierte una cantidad de años gregorianos a años musulmanes
        """
        año_musulman =int(((33 * año_gregoriano) - 20526) / 32)

        return año_musulman


    def riman(lista_1,lista_2):
        """
        Esta funcion recibe 2 listas de strings y regresara una nueva lista con
        numeros dependiendo de las codiciones que cumplan las listas
        """

        lista_resultado = []

        for n, x in enumerate(lista_1):
            if lista_1[n] == lista_2[n]:
                lista_resultado.append("1")

            elif lista_1[n][len(lista_1[n]) - 3: len(lista_1[n])] == lista_2[n][len(lista_2[n]) - 3: len(lista_2[n])]:
                lista_resultado.append("3")

            elif lista_1[n][len(lista_1[n]) - 2: len(lista_1[n])] == lista_2[n][len(lista_2[n]) - 2: len(lista_2[n])]:
                lista_resultado.append("2")

            else:
                lista_resultado.append("0")

        return lista_resultado


    def quita_negativos(lista_numeros):
        """
        Esta funcion recibe una lista de numeros(positivos y negativos) y nos
        devuelve la misma lista, pero sin los numeros negativos
        """
        while min(lista_numeros) < 0:
            for x in lista_numeros:
                if x < 0:
                    lista_numeros.remove(x)
                    continue

        return lista_numeros


    def menu():
        """
        Esta funcion desplegara el menu al usuario donde podra ver las opciones del
        menu y despues podra seleccionar una opcion
        """
        print("\nBienvendio\n")
        print("[1] - Gregoriano a Musulman")
        print("[2] - Riman")
        print("[3] - Quita negativos")
        print("[4] - Salir")

        usuario = input("\n Selecciona una opcion ")

        return usuario


    usuario = menu()

    if usuario == "1":
        usuario_a_musulman = float(input("ingresa la cantidad de años gregorianos "))
        print("La cantidad de años musulmanes son:", a_musulman(usuario_a_musulman))
        main()
        menu()

    elif usuario == "2":
        print(riman(["corazon","libre","peso","cochinito","paz"],["retozon","pez", "caso", "niñito", "paz"]))
        main()
        menu()

    elif usuario == "3":
        print(quita_negativos([3,-1,-2,5,6,7,-8]))

        main()
        menu()
    elif usuario == "4":
        exit()

    else:
        print("\nDato invalido")
        main()
        menu()

main()
