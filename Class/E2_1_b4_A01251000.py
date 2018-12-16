#Santiago Yeomans
#A01251000

lista = ["paco", "pedro", "pepe", "manuel", "abraham", "luis", "santiago", "ana", "sofia", "jorge", "eben", "hector"]
cont = 0
cont_palabras = 0

print ("Bienvendio!\nTu escribiras una letra y yo comparere esa letra con una")
print ("lista de nombres y te dire cuantos de esos nombres empiezan con la letras que ingresaste")
print ("\nLa lista de nombres es: ", lista)

letra_usuario = input("\nEscribe la letra que quieres que compare ")

for x in lista:
    nombre = lista[cont] #Aqui el programa esta obteniendo un nombre de la lista en funcion de las veces que se ha repetido el ciclo
    primera_letra = nombre[0] #Aqui se esta obteniendo la primera letra de un nombre, para posteriormente compararla con la del usuario
    cont = cont + 1

    if primera_letra == letra_usuario:
        cont_palabras = cont_palabras + 1


if cont_palabras == 0:
    print("\nDe la lista de nombres ningun nombre empieza con la letra", letra_usuario)

elif cont_palabras == 1:
    print("\nDe la lista de nombres solo", cont_palabras, "nombre empieza con la letra", letra_usuario)

else:
    print("\nDe la lista de nombres", cont_palabras, "nombres empiezan con la letra", letra_usuario)
