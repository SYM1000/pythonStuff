def cuenta_pares(listaA):
    cont = 0
    for lista in listaA:
        for elemento in lista:
            if elemento%2 == 0:
                cont += 1
    return cont
