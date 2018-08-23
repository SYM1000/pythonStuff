#Santiago Yeomans
#A01251000

import time #Aqui estamos importanto la funcion de esperar
def main():

    si_lista = ["si", "Si", "SI", "claro", "Claro", "porfavor", "smn","Smn", "a darle", "yes" ]
    no_lista = ["no", "No", "NO", "nunca", "Negativo", "negativo", "Nel", "nel"]

    def restart(): #cada ves que se llame esta funcion se iniciara el protocolo de reinicio
        time.sleep(1.5)        
        restart = str(input("\n¿Quieres ir al menu principal? "))
        
        if restart in si_lista:
            main()
        elif restart in no_lista:
            salir = str(input("\n¿Deseas salir? "))

            if salir in si_lista:
                exit()
            elif salir in no_lista:
                print("\nGracias por utilizar mi programa :)")
        else:
            exit()

    print("¡BIENVENIDO!, Por favor selecciona la opcion del programa que deseas ejecutrar\n")
    print("[1] - Convertidor de grados")
    print("[2] - Calculadora de IMC")
    print("[3] - Calculadora de IMC en libras y metros")
    print("[4] - Calculadora de interes simple")
    print("[5] - Convertidor de segundos a horas, minutos y segundos")
    print("[6] - Calculadora de nacimientos y muertes ")
    print("[7] - Calculadora del area del triangulo con formula de heron")
    print("[8] - Calculadora de resistencias combinadas")
    print("[9] - Calculadora del area de un trapezoide \n")

    usuario = int(input("Escribe el numero del programa que deseas ejecutar "))

    if usuario == 1:
            temp_c = float(input("¿Cual es la temperatura en grados celsius que deaseas convertir ? "))
            temp_f = float(temp_c*9/5+32)
            temp_k = float(temp_c + 273.15)

            print ("\nLa temperatura en kelvin es:%8.2f°K y en Fahrenheit es de %8.2f°F" % (temp_f,temp_k))            
 
            restart()


    elif usuario == 2:
            peso = float(input("Escribe tu peso en Kg "))
            altura = float(input("Escribe tu altura en metros "))
            imc = peso/(altura)**2
            imc = round(imc,2)

            print ("Tu peso es: ", peso, "kg y ", "tu altura es ", altura, "m,", "por lo tanto tu imc es de:", imc, "puntos")

            if imc < 18.5:
                    print ("Lo siento, Tienes desnutricion")
            elif imc > 24.9:
                    print ("¡¡UPS!! Tenemos un problema. Tu IMC esta arriba de lo normal")
            elif imc >= 18.5:
                    print ("¡FELICIDADES! Tu IMC es normal")
            elif imc <= 24.9:
                    print ("¡FELICIDADES! Tu IMC es normal")

            restart()


    elif usuario == 3:
            peso_l = float(input("Escribe tu peso en Libras "))
            altura_p = float(input("Escribe tu altura en pulgadas "))

            peso_k = peso_l * 0.45
            altura_m = altura_p * 0.0254

            imc = peso_k/(altura_m)**2
            imc = round(imc, 2)
            peso_k = round(peso_k, 2)
            altura_m = round(altura_m, 2)

            print ("\nTu peso es: ", peso_k, "kg y ", "tu altura es ", altura_m, "m,", "por lo tanto tu imc es de:", imc, "puntos")

            if imc < 18.5:
                    print ("--> Lo siento, Tienes desnutricion <--")
            elif imc > 24.9:
                    print ("--> ¡¡UPS!! Tenemos un problema. Tu IMC esta arriba de lo normal <--")
            elif imc >= 18.5:
                    print ("--> ¡FELICIDADES!Tu IMC es normal <--")
            elif imc <= 24.9:
                    print ("--> ¡FELICIDADES!Tu IMC es normal <--")

            restart()

                    
    elif usuario == 4:
            capital = float(input("\n¿Cuanto es el capital? "))
            años = float(input("¿Cuantos son los años a calcular? "))
            interes = float(input("¿Cuanto es el interes en porcentaje? "))

            interes_simple = ((capital * interes * años) / 100)
            interes_simple = round(interes_simple, 2)

            print("\nEl interes simple es de: " + str(interes_simple) + " pesos")         

            restart()
            

    elif usuario == 5:
            print ("\nVamos a calcular el tiempo a partir de los segundos")
            segundos = float(input("\n¿Cuantos son los segundos que deaseas convertir? "))

            if segundos > 86400:
                
                print("-->La cantidad de segundos es demasiado grande. El maximo es de 86400")
                
            elif segundos < 1:
                print("-->La cantidad de segundos es demasiado pequeña. El minimo es de 1")

            else:
                segundos_h = int(segundos/3600)
                segundos_m = ((segundos/3600) - segundos_h) * 60
                segundos_s = (segundos_m - int(segundos_m)) * 60
                segundos_s = round(segundos_s,0)

              
            print("--->",segundos, "segundos son: ", segundos_h, "horas,", int(segundos_m), "minutos,", segundos_s, "segundos")

            restart()

            
    elif usuario == 6:
            
            print("Con este programa encontraremos la cantidad de muertes y nacimiento en un tiempo determinado \n")

            años = float(input("Escribe la cantidad de años "))

            segundos_en_un_año = 3600 * 24 * 365
            años_en_segundos = años * segundos_en_un_año

            nacimientos = años_en_segundos / 7
            nacimientos = round(nacimientos, 1)
            muertes = años_en_segundos / 13
            muertes = round(muertes, 1)
            personas = nacimientos - muertes
            personas = round(personas, 1)
            
            print("La cantidad de muertes en ", años, "años", "es de:", muertes, "personas", "y la cantidad de nacimientos en", años, "años", "es de:", nacimientos, " personas") 
            print("por la tanto, la poblacion crecio:", personas, "personas")

            restart()

            
    elif usuario == 7:
        from math import sqrt
        print("Mediante este programa encontraremos el area de un triangulo utilizando la formula de heron\n ")

        a = float(input("¿Cual es la medida del lado a? "))
        b = float(input("¿Cual es la mediada del lado b? "))
        c = float(input("¿Cual es la medida del lado c? "))

        s = (a + b + c)/2

        area = sqrt(s*(s-a)*(s-b)*(s-c))
        area = round (area,2)

        print("\nEl area del triangulo es de: ",area," unidades ^ 2")

        restart()

        
    elif usuario == 8:
            print("Con este programa calcularemos las resistencias combinada de 3 diferentes resistencias en omhios\n")

            res_1 = float(input("Escribe el valor de la 1era resistencia en ohmios "))
            res_2 = float(input("Escribe el valor de la 2da resistencia en ohmios "))
            res_3 = float(input("Escribe el valor de la 3era resistencia en ohmios "))

            rt = 1/((1/res_1)+(1/res_2)+(1/res_3))
            print("\nLa resitencia total es de {0:5.2f} ohmios".format(rt))

            restart()


    elif usuario == 9:

            print("Con este programa conoceremos el area de un trapezoide a partir de la medida de sus partes \n")

            lado_b = float(input("Ingresa el largo de la base menor "))
            lado_B = float(input("Ingresa el largo de la base mayor "))
            lado_H = float(input("Ingresa el largo de la altura "))

            area = (lado_B + lado_b) / 2 * lado_H
            area = round(area,2)

            print("\nEl area de tu trapezoide es de: ", area, "unidades ^ 2")

            restart()
            

    else:
            print("\nNo seleccionaste ninguna opcion valida :( \n")

            restart()

#Aqui es donde el codigo empezara
main()
