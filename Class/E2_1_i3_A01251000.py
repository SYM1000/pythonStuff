#Santiago Yeomans
#A01251000

lista = ["santiago", "ulises", "paco", "jose"]

print("Bienvendio!")
print("Tenemos un lista definida de nombres: ", lista, "\ny este programa convertira los nombres de la lista de minusculas a mayusculas\n")

for n, nombre in enumerate(lista): #Aqui el for esta pasando por cada dato de la lista y le esta asignando un numero, numero que despues utilizaremos
                                   #para sustituir los nombres por su equivalente en mayusculas

    lista[n] = lista[n].upper()    #Aqui estamos convirtiendo el nombre en la posicion n por su equivalente en mayusculas

print("La nueva lista con los nombres en mayusculas es: ", lista)
