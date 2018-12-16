lista = [0,1,2,3,4,5]
print(lista)

for num in range(len(lista)):
    lista[num] = lista[num]**2

print(lista)
