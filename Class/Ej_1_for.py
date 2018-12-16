#Se recibe del usuario el número de estudiantes a procesar,
#recibe 3 calificaciones por estudiante y debe calcular el promedio por estudiante,
#se imprime a pantalla. Al final se despliega el promedio del grupo.

alumnos = int(input("Numero de estudiantes "))
cont = 0
estudiante = 1
for x in range(0,alumnos):
    print ("\nEstudiante", estudiante)
    cal1 = int(input("Calificacion 1 "))
    cal2 = int(input("Calificacion 2 "))
    cal3 = int(input("calificacion 3 "))
    promedio = (cal1 + cal2 +cal3) / 3
    print (promedio)
    cont = cont + promedio
    estudiante = estudiante +1

print ("\nEl promedio general es de", cont / alumnos)
