vocales = ["A","B","C","D","E","a","e","i","o","u"]
usuario1 = input("Cadena de texto ")
usuario2 = input("Segunda cadena de texto")
numero1 = 0
numero2 = 0

for x in usuario1:
     if x in vocales:
         numero1 = numero1 + 1
print (numero1)

for xi in usuario2:
     if xi in vocales:
         numero2 = numero2 + 1
print (numero2)

if numero1 > numero2:
    print("La cadena 1 tiene mas vocales que la 2")
elif numero1 < numero2:
    print("La cadena 2 tiene mas vocales")
else:
    print("tienen la misma cantidad de vocales")
