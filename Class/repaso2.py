"""
def busquda_binaria(lista, elemento):

    lista = lista.sort()
    inicio = lista [0]
    end = lista [len(lista)]

    while inico <= end:
        numero = int((end - incio) / 2)

        if lista[numero] == elemento:
            break

        else:
            if elemento > lista[numero]:
                inicio = lista[numero]
                continue
            else:
                end = lista[numero]

    return lista[numero]


print(busquda_binaria([1,2,3,4,5,6,7,8,9,10],7))
"""
