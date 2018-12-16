#Santiago Yeomans
#A01251000

print("Con este programa calcularemos el promedio de un grupo de estudiantes\nsolo ingresa el numero de estudiantes y 3 calificaciones por estudiante\n")

estudiantes = int(input("¿Cuantos estudiantes hay en el grupo? "))
cont = 0
estudiante = 1

for x in range(0,estudiantes): #Aqui se está creando un ciclo de tipo for que se va repetir por cada estudiante, en el que se le pedira sus 3 calificaciones

    print ("\nCalificaciones del estudiante", estudiante,":")
    cal1 = float(input("Calificacion 1 "))
    cal2 = float(input("Calificacion 2 "))
    cal3 = float(input("calificacion 3 "))
    promedio = (cal1 + cal2 +cal3) / 3
    promedio = round(promedio,2)

    print ("El promedio del estudiante ", estudiante, "es de: ",promedio)
    cont = cont + promedio
    estudiante = estudiante +1

general = cont / estudiantes #aqui se calcula la calificacion final del grupo
general = round(general,2)

print ("\nEl promedio general del grupo es de:", general)
