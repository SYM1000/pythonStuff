#Santiago Yeomans
#A01251000
def main():
    from os import system, name

    """
    Este es la funcion que se iniciara cuando se inicie el programa
    """
    def menu():
        """
        Esta funcion muestra el menu y pide al usuario que opcion correr
        """
        clear()
        print("\nBIENVENIDO\n")
        print("[1] - Sumar matrices")
        print("[2] - Restar matrices")
        print("[3] - Multiplicar una matris por un numero")
        print("[4] - Multiplicar matrices")
        print("[5] - Matriz traspuesta")
        print("[6] - Salir\n")

        usuario = input("Selecciona la opcion que deseas correr: ")

        return usuario


    def suma_matrices(lista_anidada1,lista_anidada2):
        """
        Esta funcion suma 2 matrices definidas
        """
        lista_sumada = []
        for n, x in enumerate(lista_anidada1):
            sub_lista = []
            for i, y in enumerate(x):
                suma = lista_anidada1[n][i] + lista_anidada2[n][i]
                sub_lista.append(suma)
            lista_sumada.append(sub_lista)
        return lista_sumada


    def resta_matrices(lista_anidada1,lista_anidada2):
        """
        Esta funcion resta 2 matrices definidas
        """
        lista_restada = []
        for n, x in enumerate(lista_anidada1):
            sub_lista = []
            for i, y in enumerate(x):
                resta = lista_anidada1[n][i] - lista_anidada2[n][i]
                sub_lista.append(resta)
            lista_restada.append(sub_lista)
        return lista_restada


    def escalar(lista_anidada1,numero):
        """
        Esta funcion toma una matriz y la multiplica por un numero
        """
        lista = []
        for n, x in enumerate(lista_anidada1):
            sub_lista = []
            for i, y in enumerate(x):
                multi = lista_anidada1[n][i] * numero
                sub_lista.append(multi)
            lista.append(sub_lista)
        return lista


    def multiplica_matrices(lista_anidada1,lista_anidada2):
        """
        Esta funcion multiplica 2 matrices definidas
        """
        lista_multiplicada = []
        for x in range(len(lista_anidada1)):
            sub_lista = []
            for y in range(len(lista_anidada1)):
                valor2 = 0
                for z in range(len(lista_anidada1)):
                    valor = lista_anidada1[x][z]*lista_anidada2[z][y]
                    valor2 = valor2 + valor
                sub_lista.append(valor2)
            lista_multiplicada.append(sub_lista)
        return lista_multiplicada


    def traspuesta(lista_anidada1):
        """
        Esta funcion obtiene la matriz traspuesta de una matriz definida de nXm
        """
        traspuesta = []
        for x in range(0,len(lista_anidada1[0])):
            sub_lista = []
            for y in range(0,len(lista_anidada1)):
                posicion = lista_anidada1[y][x]
                sub_lista.append(posicion)
            traspuesta.append(sub_lista)
        return traspuesta


    def imprimir_matriz(matriz):
        """
        Funcion para imprimir matrizes
        """
        for lista in matriz:
            print (lista)


    def clear():
        """
        Esta funcion sirve para limpiar la terminal
        """
        if name == "posix":
            _ = system("clear")


    #-------------------------------------------------------------------------------
    lista_anidada1 = [ [0,1,2], [3,4,5], [6,7,8] ]
    lista_anidada2 = [ [3,3,3], [4,4,4], [5,5,5] ]
    lista_traspuesta = [ [1,2,3,4,5], [6,7,8,9,0] ]

    usuario = menu()

    if usuario == "1":
        clear()
        print("\nLas matrices son:\nmatriz 1:", lista_anidada1, "\nmatriz 2:", lista_anidada2,"\n")
        print("\nLa matriz sumada es: ")
        imprimir_matriz(suma_matrices(lista_anidada1,lista_anidada2))
        input("\npresiona enter para continuar")
        main()
        menu()


    elif usuario == "2":
        clear()
        print("\nLas matrices son:\nmatriz 1:", lista_anidada1, "\nmatriz 2:", lista_anidada2,"\n")
        print("\nLa matriz restada es: ")
        imprimir_matriz(resta_matrices(lista_anidada1,lista_anidada2))
        input("\npresiona enter para continuar")
        main()
        menu()


    elif usuario == "3":
        clear()
        print("\nLas matriz es:\nmatriz:",lista_anidada1)
        numero = int(input("\nIngresa un numero para multiplicarlo por la matriz "))
        print("\nLa matriz multiplicada es")
        imprimir_matriz(escalar(lista_anidada1,numero))
        input("\npresiona enter para continuar")
        main()
        menu()


    elif usuario == "4":
        clear()
        print("\nLas matriz es:\nmatriz 1:",lista_anidada1,"\nmatriz 2:", lista_anidada2,"\n")
        print("\nLa matriz multiplicada es")
        imprimir_matriz(multiplica_matrices(lista_anidada1,lista_anidada2))
        input("\npresiona enter para continuar")
        main()
        menu()


    elif usuario == "5":
        clear()
        print("\nLas matriz es:\nmatriz:")
        imprimir_matriz(lista_traspuesta)
        print("\nLa matriz traspuesta es")
        imprimir_matriz(traspuesta(lista_traspuesta))
        input("\npresiona enter para continuar")
        main()
        menu()


    elif usuario == "6":
        clear()
        print("\nsaliste del programa")
        exit()

    else:
        clear()
        print("\nOpcion invalida")
        main()
        menu()

main()

"""
Referencias:
https://www.youtube.com/watch?v=7QlrzV1f5c0
"""
