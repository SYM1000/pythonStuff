#De una lista definida de strings, determinar cuántas de éstas empiezan con
#la letra que te indique el usuario.

#Santiago Yeomans
#A01251000

lista = ["paco", "pedro", "pepe", "manuel", "abraham", "luis", "santiago", "eben", "hector"]
cont = 0
cont_palabras = 0

print ("Bienvendio!\nTu escribiras una letra y yo comparere esa letra con una")
print ("lista de nombres y te dire cuantos de esos nombres empiezan con la letras que ingresaste")
print ("\nLa lista de nombres es: ", lista)

letra_usuario = input("\nEscribe la letra que quieres que compare ")

for x in lista:
    i = lista[cont]
    primera_letra = i[0]

    cont = cont + 1

    if primera_letra == letra_usuario:
        cont_palabras = cont_palabras + 1

if cont_palabras == 0:
    print("\nDe la lista de nombres ningun nombre empieza con la letra", letra_usuario)

elif cont_palabras == 1:
    print("\nDe la lista de nombres solo", cont_palabras, "nombre empieza con la letra", letra_usuario)

else:
    print("\nDe la lista de nombres", cont_palabras, "nombres empiezan con la letra", letra_usuario)
