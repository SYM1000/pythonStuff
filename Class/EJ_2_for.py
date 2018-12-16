#De una lista de números definida. Determinar cuántos están entre -5 y 5 (sin incluirlos),
#cuántos menores o iguales a -5 y cuántos mayores o iguales a 5.

lista = [-10,-5,-4,-3,-2,-1,0,1,2,3,4,5,10]
ma5 =0
me5 =0
for x in lista:
    if x >=5:
        ma5 +=1
    elif x < 5:
        me5 +=1
print(ma5,me5)
