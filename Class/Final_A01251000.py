#Santiago Yeomans
#A01251000
import os
print(os.getcwd())
os.chdir("/Users/santiagoyeomans/developer/python")

def mayor_ingresado():
    lista = []

    usuario = int(input("Ingresar numero "))
    while usuario >= 0:
        usuario = int(input("Ingresar numero "))
        if usuario >= 0:
            lista.append(usuario)
            continue
        else:
            break
    final = max(lista)

    return final


def nomenclatura(edificio,piso,departamento):
    lista = []
    numero_piso = 0
    numero_departamento = 1
    for x in range(piso):
        sub_lista = []
        numero_departamento = 1
        for y in range(departamento):

            if numero_departamento < 10:
                numero_departamentox = "0",str(numero_departamento)
                numero_departamentox = "".join(numero_departamentox)
            else:
                numero_departamentox = numero_departamento

            cuarto = edificio,str(numero_piso),"-",str(numero_departamentox)
            cuarto = "".join(cuarto)
            sub_lista.append(cuarto)
            numero_departamento = numero_departamento + 1

        numero_piso = numero_piso + 1
        lista.append(sub_lista)

    return lista


def extension_frecuente(lista):
    from statistics import mode
    return mode(lista)


def triangular(numero):
    lista = []
    inicio = 0
    for x in range(numero):
        sub_lista = []
        for y in range(numero):
            if x == 0:
                sub_lista.append(1)
            else:
                numero = 0 * inicio
                sub_lista.append(1)
                inicio = inicio + 1
        lista.append(sub_lista)


    return lista

print(triangular(2))



def calcula():
    try:
        archivo = open("calificaciones.csv", "r")
    except:
        print("Error al abrir el archivo")

    else:
        lista = []
        archivo.readline()
        for linea in archivo:
            linea = linea.rstrip()
            lineap = linea.split(",")
            lista.append(lineap)
        archivo.close()
        final = (lista[0][1]*.30) + (linea[0][2]*.35) +(linea[0][3]*.15) + (linea[0][4]*.20)
        final = round(final,2)

        if final >= 70
            etiqueta = "APROVADO"
        else:
            etiqueta = "REPROBADO"

    try:
        file = open("semestreAD18.txt","w")
    except:
        print("Error al abrir el archivo")
    else:
        for x in lista:
            file.write(lista[0][0])
            file.write(final)
            file.write(etiqueta)
            file.write("\n")


        print(lista)
