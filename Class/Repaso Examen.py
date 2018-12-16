#Repaso Examen
main()
    lista_si = ["si", "claro"]
    lista_no = ["No", "negativo"]

    print ("\nBienvenido a este menu bien freson")
    print ("[1] - Una calculadora que multiplica numeros")
    print ("[2] - Contar un chiste")
    print ("[3] - A caunto esta el dolar?")
    print ("[4] - Salir")

    def salir():
        while True:
            usuario_salir = input("Quieres salir?")
            try:
                usuario_salir in lista_si or usuario_salir in lista_no
                break
            except:
                print("Dato Invalido")
                continue

        if usuario_salir in lista_si:
            exit()

        elif usuario_salir in lista_no:
            main()

    while True:
        try:
            usuario = int(input("Que programa bien freson quieres correr?"))
            break
        except:
            print ("Dato invalido")


    if usuario == 1:
        print("Multiplicare los numeros que me des")
        while True:
            try:
                numero1 = int(input("Primer numero "))
                break
            except:
                print ("Dato invalido")
                continue

            try:
                numero2 = int(input("Segundo numero "))
                break
            except:
                print ("Dato Invalido")
                continue

            resultado = numero1*numero2
            print(resultado)







main()
