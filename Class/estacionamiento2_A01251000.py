#Santiago Yeomans
#A01251000

def genera_vacios(lista_anidada):
    """
    Esta funcion recibe una lista anidada de unos y ceros que corresponden a los
    lugares disponibles y ocupados de un estacionmiento y la funcion te devuelve
    los lugares que estan disponibles
    """
    lista_vacios = [ ]
    letras = ["A","B","C","D","E","F","G","H","I","J"]

    for n, x in enumerate(lista_anidada):
        for i, y in enumerate(x):
            if y == "0":
                fila = letras[n]
                lugar = str(i+1)
                estacionamiento = fila,lugar
                lista_vacios.append("".join(estacionamiento))
    return lista_vacios


def simulacion():
    """
    Esta funcion genera un archivo de 15 números separados por comas en cada
    línea, 10 líneas. Los números son 0 o 1
    """
    from random import randint

    try:
        file = open("simulacion.txt", "w")
    except:
        print("No se puede abrir el archivo o no existe")
    else:
        for x in range(10):
            for y in range(15):
                numero = randint(0,1)
                numero = str(numero)
                file.write(numero)
                if y == 14:
                    break
                file.write(",")
            file.write("\n")
        file.close()


def lee_archivo():
    """
    Esta funcion lee los datos escritos en el archivo simulacion.txt y nos
    devuelve una lista anidad para operar con ella
    """
    try:
        file = open("simulacion.txt","r")
    except:
        print("No se puede abrir el archivo o no existe")
    else:
        lista = []
        file.readline()
        for linea in file:
            lineap = linea.rstrip()
            l = lineap.split(",")
            lista.append(l)
        file.close()
    return lista


def escribe_varios(lista_vacios):
    """
    Esta funcion recibe los datos de los lugares vacios en el estacionamiento y
    los escribe en un documento llamado vacios.txt
    """
    try:
        file = open("vacios.txt","w")
    except:
        print("No se puede abrir el archivo o no existe")
    else:
        for n, x in enumerate(lista_vacios):
            file.write(x)
            if n + 1 < len(lista_vacios):
                file.write(",")
        file.close()

#-------------------------------------------------------------------------------

simulacion()
print("Datos recibidos del sistema de sensores...")

listaEst=lee_archivo()
print("Lectura del archivo completada")

lista_vacios = genera_vacios(listaEst)
print("Lista de vacios generada...")

escribe_varios(lista_vacios)
print("Escritura del archivo vacios.txt completada")
