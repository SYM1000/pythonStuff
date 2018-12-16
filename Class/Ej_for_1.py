
datos = [int(i) for i in input("Escribe los datos de la lista: ").split(",")]
n = int(input("Escribe un numero "))
#list(datos)

mayores_N = 0

print(datos)

for x in datos:

    if x > n:
        mayores_N = mayores_N + 1


print("Hay ", mayores_N, "numeros mayores a ", n)
