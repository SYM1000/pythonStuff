import math

def segundos(segundos):

    segundos_h = int(segundos / 3600)
    segundos_m = ((segundos / 3600) - segundos_h) * 60
    segundos_s = (segundos_m - int(segundos_m)) * 60
    segundos_s = round(segundos_s, 0)

    print("--->", segundos, "segundos son: ", segundos_h, "horas,", int(segundos_m), "minutos,", segundos_s,"segundos")


def convertir_pies_a(pies,medida):
    if medida == "y":
        resultado = pies/3

    elif medida == "p":
        resultado = pies * 12

    elif medida == "m":
        resultado = pies/3.281

    return resultado


def volumen_esfera(radio):
    volumen = (4/3) * pi * (radio)**3

    return volumen


def multiplo_de(numero_a_comprobar, divisor):

    return numero_a_comprobar%divisor == 0


def compara(a,b):
    if a < b:
        return -1

    elif a == b:
        return 0

    else:
        return +1


def menu():
    print ("Programa para funciones")
    print ("1. Equivalencia de segundos")
    print ("2. Conversion de pies a otras medidas")
    print ("3. Volumen de esfera")
    print ("4. Multiplo de...")
    print ("5. Compara numeros")
    print ("6. salir")
    opcion = input("Teclea el numero de la opcion que desees: ")
    return opcion

    opc = "0"
    while opc != "6":
        opc=menu()
        if opc == "1":
            seg = int(input("Cuantos Segundos: "))
            segundos(seg)
            input("Presiona enter para continuar...\n")

        elif opc == "2":
            medida = input("Teclea p o m o y para pulgadas, metros o yardas respectivamente")
            medida = medida.lower()
            pies = float(input("Cantidad de pies: "))
            if medida == "p" or medida == "m" or medida == "y":
                resultado = convertir_pies_a(pies,medida)
                print(f"{pies} pies son {resultado} {medida}")
            else:
                print("medida no valida")
            input("presiona enter para continuar")

        elif opc == "3":
            radio = float(input("Ingrese el radio: "))
            volumen_esfera(radio)
            print("el volumen de la esfera es: ", volumen)

        elif opc == "4":
            n1 = float(input("Numero 1: "))
            n2 = float(input("Numero 2: "))
            if multiplo_de(n1,n2):
                print(f"{n1} es multiplo de {n2}")
            else:
                print(f"{n1} no es multiplo de {n2}")
            input("presiona enter para continuar")

        elif opc == "5":
            n1 = float(input("Numero 1: "))
            n2 = float(input("Numero 2: "))
            comparacion = compara(n1,n2)
            if comparacion == -1:
                print(f"{n1} es menor que {n2}")
            elif comparacion == 0:
                print(f"{n1} es igual que {n2}")
            else:
                print(f"{n1} es mayor que {n2}")
