    #Santiago Yeomans
    #A01251000
    #Miercoles 10 de octubre
    #Este es un juego de ahorcado escrito en python
vidas = 6

def main():
    """
    Esta funcion es la funcion principal del juego que contiene todo el codigo
    """
    import random
    from os import system, name
    import time
    lista = ["jose", "santiago", "yeomans", "molina"]
    palabra_oculta = []
    vidas = 6


    def clear():
        """
        Esta funcion sirve para limpiar la terminal
        """
        if name == "posix":
            _ = system("clear")



    def palabra_aleatoria():
        """
        Esta funcion sirve para elegir una palabra alazar a partir de una lista
        de palabras. Esta palabra aleatoria sera la palabra que se utilice para
        jugar al ahorcado
        """
        palabra = random.choice(lista)
        return palabra


    def menu():
        """
        Esta funcion sirve para desplegar el menu con las opciones del juego
        """
        clear()
        print("\n\tBienvendio al juego de ahorcado\n")
        print ("\t\t[1] - Jugar")
        print("\t\t[2] - Salir")
        print("\t\t[3] - Instrucciones")
        print("\t\t[4] - Creditos\n")

        usuario = str(input("Selecciona la opcion que deseas realizar "))
        return usuario


    def monito():
        """
        Esta funcion sirve para imprimir el dibujo del monito del ahorcado en
        funcion de las vidas que tenga el jugador
        """
        global vidas
        if vidas == 6:
            print("\n  +-----+\n  |      \n  |      \n  |     \n  |     \n _|_")

        elif vidas == 5:
            print("\n  +-----+\n  |     | \n  |     O \n  |        \n  |        \n _|_")

        elif vidas == 4:
            print("\n  +-----+\n  |     | \n  |     O \n  |     |  \n  |        \n _|_")

        elif vidas == 3:
            print("\n  +-----+\n  |     | \n  |     O \n  |     |\ \n  |        \n _|_")

        elif vidas == 2:
            print("\n  +-----+\n  |     | \n  |     O \n  |    /|\ \n  |        \n _|_")

        elif vidas == 1:
            print("\n  +-----+\n  |     | \n  |     O \n  |    /|\ \n  |      \ \n _|_")

        elif vidas == 0:
            print("\n  +-----+\n  |     | \n  |     O \n  |    /|\ \n  |    / \ \n _|_")


    def juego():
        """
        Esta funcion es la funcion que se encargara de correr el ahorcado.
        Cuando el jugador decida en su menu la opcion de jugar
        """
        clear()
        global vidas
        palabra = palabra_aleatoria()
        palabra_juego = list(palabra)
        lista_intentos = []


        if palabra == "jose":
            palabra_oculta = ["X", "X", "X", "X"]
            print (lista)

        elif palabra == "santiago":
            palabra_oculta = ["X", "X", "X", "X", "X", "X", "X", "X"]


        elif palabra == "yeomans":
            palabra_oculta = ["X", "X", "X", "X", "X", "X", "X"]


        else:
            palabra_oculta = ["X", "X", "X", "X", "X", "X" ]


        while vidas > 0:
            clear()
            monito()
            print("La palabra es: ", " ".join(palabra_oculta))
            print("Tienes ", vidas, "vidas")
            letra_usuario = input("Letra: ")

            if letra_usuario not in palabra_juego and letra_usuario not in lista_intentos:
                print("Letra incorrecta, perdiste una vida")
                lista_intentos.append(letra_usuario)
                time.sleep(1)
                vidas = vidas - 1
                continue

            elif letra_usuario not in palabra_juego and letra_usuario in lista_intentos:
                   print("Ya usaste la letra", letra_usuario, ", pero no te bajare vidas")
                   time.sleep(1.5)
                   continue

            elif letra_usuario in palabra_juego and letra_usuario not in lista_intentos:
                    for n, x in enumerate(palabra_juego):
                        if x == letra_usuario:
                            palabra_oculta[n] = letra_usuario
                            lista_intentos.append(letra_usuario)
                            continue

            elif letra_usuario in palabra_juego and letra_usuario in lista_intentos:
                    print("Ya usaste la letra", letra_usuario, ", pero no te bajare vidas")
                    lista_intentos.append(letra_usuario)
                    time.sleep(1.5)
                    continue

            if vidas > 0 and palabra_oculta == palabra_juego:
                clear()
                monito()
                print("La palabra es: ", " ".join(palabra_oculta))
                print("Tienes ", vidas, "vidas")
                print("\nFELICIDADES GANASTE!!")
                break

        if vidas == 0:
            clear()
            monito()
            print("La palabra es: ", " ".join(palabra_oculta))
            print("Tienes ", vidas, "vidas")
            print("\nLo siento, Perdiste!\nLa palabra era: ", "".join(palabra_juego))

        while True:
            jugar_usuario = input("\nQuieres volver a jugar? ")

            if jugar_usuario == "si":
                vidas = 6
                clear()
                juego()
                break

            elif jugar_usuario == "no":
                regresar()
                break

            else:
                clear()
                monito()
                print("La palabra es: ", " ".join(palabra_oculta))
                print("Tienes ", vidas, "vidas")
                print("\nDato invalido. Las opciones son NO y SI")
                time.sleep(0.5)
                continue

    def salir():
        """
        Esta es la funcion que se ejecutara cuando el usuario decida salir del
        programa
        """
        clear()
        print("\nQue lastima que decidiste salir\n")
        print("----> Creador: Santiago Yeomans <----")
        exit()


    def regresar():
        """
        Esta es una funcion que le permitira al usuario regresar al menu
        """
        usuario = input("\nQuieres regresar al menu principal? ").lower()

        if usuario == "si":
            main()
            menu()

        elif usuario == "no":
            print("Gracias por jugar :)")
            time.sleep(1.5)
            exit()

        else:
            print("Dato invalido. Las opciones son NO y SI")
            time.sleep(2)
            regresar()



    def instrucciones():
        """
        Esta funcion es la encargada de mostrar las instrucciones del juego
        cuando el usuario Seleccione la opcion de ver las instrucciones de juego
        """
        print("\n\t\t--> REGLAS <--\n\n")
        print("1. El objetivo del jugador es adivinar una palabra aleatoria apartir de adivinar las letras que la componen")
        print("2. El jugador tiene 6 vidas")
        print("3. El jugador gana si adivina la palabra")
        print("4. El jugador tiene utilizar las letras del abecdario para adiviniar la palabra")
        print("5. Si el jugador repite las letras no se le penalizara")
        print("6. El jugador pierde si se queda sin vidas y no adivina la palabra")
        print("\n7. REGLA MAS IMPORTANTE: El jugador se debe divertir")


    def creditos():
        """
        Esta funcion se encarga de mostrar los creditos del juego cuando el
        jugador decida ver los creditos del juego
        """
        print("\n\t\t--> CREDITOS <--\n")
        print("\nCreado por: Santiago Yeomans")
        print("Fecha: Miercoles 10 de Octubre")
        print("Lugar: Guadalajara")
        print("Lenguaje: Python 3")


#-------------------------------------------------------------------------------

    usuario = menu() #Aqui a la variable usuario se le esta asigando el valor que retorne la funcion menu
    palabra_juego = palabra_aleatoria()

    if usuario == "1":
        juego()

    elif usuario == "2":
        salir()

    elif usuario == "3":
        clear()
        instrucciones()
        regresar()

    elif usuario == "4":
        clear()
        creditos()
        regresar()

    else:
        print("Seleccionaste una opcion invalida")
        time.sleep(1)
        clear()
        main()
        menu()

main() #Aqui es donde el prgrama comenzara ya que se esta llamando a la funcion main que contiene todo el codigo del juego
