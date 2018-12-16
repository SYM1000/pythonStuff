#Repaso Examen
def main():
        lista_si = ["si", "claro"]
        lista_no = ["no", "negativo"]

        print ("\nBienvenido a este menu bien freson")
        print ("[1] - Una calculadora que multiplica numeros")
        print ("[2] - Contar un chiste (o no)")
        print ("[3] - A caunto esta el dolar?")
        print ("[4] - Salir")

        def salir():
            while True:
                usuario_salir = input("\nQuieres salir?")
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
                usuario = int(input("\nQue programa bien freson quieres correr? "))
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
            while True:
                try:
                    numero2 = int(input("Segundo numero "))
                    break
                except:
                    print ("Dato Invalido")
                    continue

            resultado = numero1*numero2
            print(resultado)
            salir()

        elif usuario == 2:

            #print("Formato original: un año tine: %2.2f dias, %2.3f meses y cada mes tiene %2d dias % (365.250, 12, 30 ) ")

            print ("un año tine: %2.2f dias, %2.3f meses y cada mes tiene %2d dias" % (365.250, 12, 30 ))
            salir()

        elif usuario == 3:

            #print("Formato original: un año tiene {0:2.2f} dias, {1:2d} meses y cada mes tiene {2:2d} .format(365.250,12,30) ")

            print ("un año tiene {0:2.2f} dias, {1:2d} meses y cada mes tiene {2:2d} dias" .format(365.250,12,30))
            salir()


        elif usuario == 4:
            a = "elegiste "
            b = "la opcion de "
            c = "salir"
            print (str(a) + str(b) + str(c))
            salir()

        else:
            salir()








main()
