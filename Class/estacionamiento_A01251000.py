#Santiago Yeomans
#A01251000

lista_anidada = [ [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1], [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], [1,1,0,1,1,1,0,1,1,1,1,1,1,1,1], [0,1,0,1,1,1,1,0,1,1,0,1,1,1,0] ]

def vacios(lista_anidada):
    """
    Esta funcion recibe una lista anidada de unos y ceros que corresponden a los
    lugares disponibles y ocupados de un estacionmiento y la funcion te devuelve
    los lugares que estan disponibles
    """
    lista_vacios = [ ]
    letras = ["A","B","C","D","E","F","G","H","I","J"]

    for n, x in enumerate(lista_anidada):
        for i, y in enumerate(x):
            if y == 0:
                fila = letras[n]
                lugar = str(i+1)
                estacionamiento = fila,lugar
                lista_vacios.append("".join(estacionamiento))
    return lista_vacios

print(vacios(lista_anidada))
