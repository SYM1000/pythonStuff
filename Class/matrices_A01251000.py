#Santiago Yeomans
#A01251000

lista_anidada = [[0,1,2,3],[4,0,5,6],[7,8,0,9],[-3,-2,-1,0],[3,3,3,0]]
"""
Esta es la lista anidada de numeros que se utiliza en todos los ejercicios
"""

def imprimir_matriz(matriz):
    """
    Funcion para imprimir matrizes
    """
    for lista in matriz:
        print (lista)


#Ejercicio 1
def creamatriz1(n):
    """
    Esta funcion crea una matriz de nXn con solo numeros -1
    """
    lista = []
    sub_lista = []
    for x in range(0,n):
        sub_lista.append(-1)

    for x in range(0,n):
        lista.append(sub_lista)
    return lista


#Ejercicio 2
def creamatriz2(n):
    """
    Esta funcion crea una matriz de nxn donde se indica el numero de la columna
    """
    lista = []
    sub_lista = []
    columna = 1

    for x in range(0,n):
        sub_lista.append(columna)
        columna = columna + 1

    for x in range(0,n):
        lista.append(sub_lista)
    return lista


#Ejercicio 3
def creamatriz3(n):
    """
    Esta fucnion crea una matriz nXn donde se indica el numero de la fila
    """
    lista = []

    for x in range(n):
        sub_lista = []
        for y in range(n):
            sub_lista.append(x + 1)
        lista.append(sub_lista)
    return lista


#Ejercicio 4
    """
    Esta función devuelve una lista que representa una matriz de nXn y cada
    localidad de la matriz tiene asignado un número consecutivo a partir de uno.
    """
def creamatriz4(n):
    lista = []
    for x in range(n):
        sub_lista = []
        x = x + 1
        for y in range(n):
            sub_lista.append(x)
            x = x + n
        lista.append(sub_lista)
    return lista


#Ejercio 5
    """
    Esta funcion cuenta los numeros pares en una lista anidada
    """
def cuentaPares(lista_anidada):
    cont = 0
    for x in lista_anidada:
        for y in x:
            if y % 2 == 0:
                cont = cont + 1
    return cont


#Ejercico 6
    """
    Esta funcion regresa la suma de sumar cada localidad de la lista
    """
def sumaMatriz(lista_anidada):
    lista_sumada = []
    for x in lista_anidada:
        lista_sumada.append(sum(x))

    return sum(lista_sumada)


#Ejercio 7
    """
    Esta funcion cuenta cuantos numeros son positivios en una lista anidada
    """
def cuentaPositivos(lista_anidada):
    cont_positivos = 0
    for x in lista_anidada:
        for y in x:
            if y >= 0:
                cont_positivos = cont_positivos + 1

    return cont_positivos


#Ejercicio 8
    """
    Esta funcion cuenta cuantos numeros son negativos
    """
def cambiaNegativos(lista_anidada):
    for n, x in enumerate(lista_anidada):
        for i, y in enumerate(x):
            if y < 0:
                lista_anidada[n][i] = 0
    return lista_anidada


#Ejercico 9
    """
    Esta funcion cuenta cuantos numeros se repiten
    """
def cuentaRepeticiones(lista_anidada, n):
    cont = 0
    for x in lista_anidada:
        for y in x:
            if y == n:
                cont = cont + 1
    return cont


#Ejercicio 10
def busca(lista_anidada, n):
    """
    Esta funcion busca un numero n en una lista anidada y si existe devuelve True
    """
    valor = False
    for x in lista_anidada:
        for y in x:
            if y == n:
                valor = True
    return valor


#Ejercicio 11
def sumaMayores5(lista_anidada):
    """
    Esta funcion cuenta cuantos numeros son mayores a 5
    """
    lista_mayores_a_5 =[]
    for x in lista_anidada:
        for y in x:
            if y > 5:
                lista_mayores_a_5.append(y)
    return sum(lista_mayores_a_5)


#Ejercicio 12
def cambiaCeros(lista_anidada):
    """
    Esta funcion cambia un numero 0 por la suma de su fila y columna
    """
    for n, x in enumerate(lista_anidada):
        for i, y in enumerate(x):
            if y == 0:
                lista_anidada[n][i] = (n + 1) + (i + 1)
    return lista_anidada
