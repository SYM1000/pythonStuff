#Santiago Yeomans
#A01251000

print("Bienvenido!")
print("Con este programa tu escribiras una palabra y yo transformare las letras e por 3,las o por h y las letras a por 4")

usuario = input("\nEscribe una palabra: ")
usuario = list(usuario)

for n, letra in enumerate(usuario): #Aqui se esta usando la funcion enumerate para para asignarle un valor a cada letra del string

    if letra == "e":
        usuario[n] = "3"

    elif letra == "o":
        usuario[n] = "h"

    elif letra == "a":
        usuario[n] = "4"

nueva_palabra = "".join(usuario) #Aqui se esta usando la funcion join para juntar la lista en una string
print("\nLa palabra nueva despues de la transormacion es: ", nueva_palabra)
