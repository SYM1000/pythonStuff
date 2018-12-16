#De una lista de Strings definida, cambiar todos sus elementos por los mismos
#strings pero con mayúsculas.

lista = ["santiago", "ulises", "paco"]

for n, x in enumerate(lista):
    if x == x:
        lista[n] = lista[n].upper()

print(lista)
lista2 = ", ".join(lista)
print(lista2)
