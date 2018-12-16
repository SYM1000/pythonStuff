"""
lista1 = ["santiago", "jorge", "ulises"]
lista2 = [[13,14,18,45,9], [21,56,12,10,90], [80,5,8,70,80]]

#Ejercicio 1
def es_perfecto(numero):
    valor = False
    lista = []
    cont = numero - 1

    while cont > 0:
        if numero % cont == 0:
            lista.append(cont)
            cont = cont - 1

        else:
            cont = cont - 1

    if sum(lista) == numero:
        valor = True
        return valor
    else:
        return valor


#Ejercicio 2
def cuales_perfectos(lista_enteros):
    lista_perfectos = []

    for x in lista_enteros:
        lista = []
        cont = x - 1
        while cont > 0:
            if x % cont == 0:
                lista.append(cont)
                cont = cont - 1

            else:
                cont = cont - 1

        if sum(lista) == x:
            lista_perfectos.append(x)

    return lista_perfectos


#Ejercicio 3
def divide_matriculas(lista_matriculas):
    lista = [[], []] #la primera lista contiene las matriuclas pares

    for x in lista_matriculas:
        dato = int(x[-1])
        if dato % 2 == 0 or dato == 0:
            lista[0].append(x)
        else:
            lista[1].append(x)

    return lista
#print(divide_matriculas(["A01251000", "A01251001", "A01251002", "A01251003", "A01251004", "A01251005"]))

#Ejercicio 4
def frecuencia_entidad(lista_curps):
    lista = []
    for x in lista_curps:
        sub_lista = []
        dato = str(x[11:13:1])
        sub_lista.append(dato)


        lista.append(sub_lista)

    return lista
#print(frecuencia_entidad(["BADD110313HCMLNS09","BADD110313HJCLNS09","BADD110313HJCLNS09","BADD110313HJCLNS09","BADD110313HQTLNS09","BADD110313HQTLNS09","BADD110313HQTLNS09","BADD110313HQTLNS09","BADD110313HSRLNS09","BADD110313HSRLNS09","BADD110313HSRLNS09","BADD110313HSRLNS09","BADD110313HSRLNS09"]))


#Ejercio 5
def mezcla_ordenada(lista1, lista2):
    lista_ordenada = []

    for x in lista1:
        lista_ordenada.append(x)

    for x in lista2:
        lista_ordenada.append(x)

    return sorted(lista_ordenada)
#print(mezcla_ordenada([ 4, 6, 8, 12] , [1, 3, 10, 15]))


#Ejercicio 6
def ganador_etapa(lista1,lista2):
    etapas = []
    ganadores = []
    nombres = []
    cont = 0
    for w in range(5):
        sub_lista = []
        sub_lista.append(lista2[0][cont])
        sub_lista.append(lista2[1][cont])
        sub_lista.append(lista2[2][cont])
        etapas.append(sub_lista)
        cont = cont + 1

    for x in etapas:
        ganador = min(x)
        nombre = x.index(ganador)
        ganadores.append(nombre)

    for numero in ganadores:
         nombres.append(lista1[numero])

    return nombres

print(ganador_etapa(lista1,lista2))

#Ejercicio 7
def cuantas_frases(texto):
    lista = []
    lista = texto.split(". ")
    largo = len(lista)

    return largo
#print(cuantas_frases("el perro es verde. Donald Trump tiene prisa por cerrar por completo el otro gran frente comercial de los dos últimos años. sea un hecho necesita aún del visto bueno definitivo de todos los Congresos."))
"""



"""-------------------archivos---------------"""

# r para leer / w para escribir / a para añadr

#para leer archivos:
try:
    archivo = open("archivo.txt", "r")

except:
    print("no se pudo abrir el archivo")

else:
    for linea in archivo:
        print(linea.rstrip())
        archivo.close()

#para escribir archivos:
try:
    archivo = ("arvicho.txt", "w", encoding = "UTF-8")

except:
    print("Error al abrir el archivo")

else:
        else:
            lista = []
            file.readline()
            for linea in file:
                lineap = linea.rstrip()
                l = lineap.split(",")
                lista.append(l)
            file.close()
        return lista

    try:
        archivo = ("arvicho.txt", "w", encoding = "UTF-8")
    else:
    archivo.write("Se sobreescribio\n")
    archvio.write("todo el archvio")
    archivo.close()

#para añadir a un archivo:
try:
    archivo = open("archvio.txt","a", encoding="UTF-8")
except:
    print("Error al abrir el archivo")
else:
    archivo.write("se agregó")
    archivo.wirte("al fianl del archivo")
    archivo.close()


#de un archivo crear una lista anidad
try:
    archivo = open("archvio.txt", "r")

except:
    print("Error al abrir el archvio")

else:
    for linea in archivo:
        lineap = linea.rstrip()
        l = lineap.split(",")
        lineas.append(l)
print(lineas)
