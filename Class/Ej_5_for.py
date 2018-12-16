#De una lista definida por el usuario, modifica sus números
#por el doble de su valor.

lista = []

datos = int(input("Cuantos numeros quieres agregar?"))
cont = 1

for x in range(datos):
    print ("Dato", cont)
    valor = int(input("Valor del dato "))
    cont = cont + 1
    valor_lista = valor * 2
    lista.append(valor_lista)

print("\nLa lista es: ", lista)
