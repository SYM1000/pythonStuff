#SantiagoYeomans
#A01251000

from random import randint

numero_aleatorio = randint(1,100)
intentos = 1
intentos_max = 7
vidas = 6

print("Bienvenido, Yo pensare un numero entre 1 y 100 y tu tendras 7 intentazos\npara adivinar el numero en el que estaba pensando")

while intentos <= intentos_max:
    try:
        numero_usuario = int(input("\n¿En que numero estoy pensando? "))
    except:
        print("Dato invalido")
        continue

    if numero_aleatorio < numero_usuario:
        print("Mi numero es menor ----> Te quedan ",vidas ,"intentos")
        intentos = intentos + 1
        vidas = vidas - 1
        continue

    elif numero_aleatorio > numero_usuario:
        print("Mi numero es mayor ----> Te quedan ", vidas,"intentos")
        intentos = intentos + 1
        vidas = vidas - 1
        continue

    else:
        print("¡Felicidades! adivinaste mi numero")
        exit()
        break

print("\nLo siento, no adivinaste mi numero\n mi numero era: ", numero_aleatorio)
exit()

#aprendi a desarollar un acumulador, a validar datos y a utilizar condicionales dentro de un while
