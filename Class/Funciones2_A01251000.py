#Santiago Yeomans
#A01251000
def main():


    import time
    def energia(masa):
        energia = masa * (299792458)**2
        return energia


    def multiplos_comunes(num1,num2,num3):
        lista = []
        maximo = num3 - 1
        for x in range(1,maximo):
            if x % num1 == 0 and x % num2 == 0:
                lista.append(x)
        return lista


    def ofertas(monto):
        dolares_extra = 0
        if monto == 5 or monto == 10:
            dolares_extra = 0
            return monto

        elif monto == 25:
            dolares_extra = 3
            return monto + dolares_extra

        elif monto == 50:
            dolares_extra = 8
            return monto + dolares_extra

        elif monto == 100:
            dolares_extra = 20
            return monto + dolares_extra
        else:
            print("\nIngresaste una cantidad invalida. Las cantidades disponibles son: 5,10,25,50 y 100")
            return 0


    def barra_progreso(segundos):
        import time
        cont = 10

        while cont <= segundos:
            print("x", end = "")
            time.sleep(10)
            cont = cont + 10


    def menu():
        print("[1] - Programa para caluclar la energia mediante E=mc2")
        print("[2] - Programa para encontrar los multiplos comunes de 2 numeros dentro de un limite")
        print("[3] - Programa para saber si te tocan promociones a partir de la cantidad que quieras recargar")
        print("[4] - Programa que muestra una barra de progreso ")
        print("[5] - Salir")

        usuario = int(input("\nQue programa quieres usar?"))
        return usuario

    #-------------------------------------------------------------------------------
    usuario = menu()

    if usuario == 1:
        masa = int(input("\nCual es la masa del objeto en kilogramos?"))
        print("Su energia es de: ", energia(masa), "Joules")

    elif usuario == 2:
        num1 = int(input("\nIngresa el primer numero para encontrar su multiplo: "))
        num2 = int(input("Ingresa el segundo numero para encontrar su multiplo: "))
        num3 = int(input("Ingresa el limite de los de los mutliplos: "))

        print("\nLa lista de numeros que son multiplos de ", num1, "y ", num2, "y menores a ",num3, "es: ", multiplos_comunes(num1,num2,num3))

    elif usuario == 3:
        monto = int(input("\nIngresa la cantidad de dinero a recargar: "))
        print("Tu recarga total es de: ", ofertas(monto),"pesos")

    elif usuario == 4:
        segundos = int(input("\nIngresa la cantidad de segundos que quieres que dure la barra de progreso: "))
        print(barra_progreso(segundos))

    elif usuario == 5:
        print("\nGracias por jugar")
        exit()

    else:
        print("\n--> Ingresaste una opcion invalida del menu <--\nVuelve a intentar\n")
        time.sleep(1.5)
        main()

main()


#Con esta practica aprendi a utilizar los parametros de las funciones, a definir funciones, crear una menu con funciones y a utilizar el formato print("", end = "")
