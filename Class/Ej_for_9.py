#De una lista de Strings definida, contabilizar cuántos de ellos tienen algún
#carácter numérico.

lista = ["santiago", "Santiago2", "ulises", "ulises2", "a", "5"]
cont = 0
palabra = 0

for x in lista:
    y = any(x.isdigit() for x in lista[palabra])
    palabra = palabra + 1

    if y == True:
        cont = cont +1

print("Hay ", cont, "datos con numeros")
