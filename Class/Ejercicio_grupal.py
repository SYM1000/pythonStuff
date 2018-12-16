vocales = ["A","B","C","D","E","a","e","i","o","u"]
usuario = input("Cadena de texto ")
numero = 0

for x in usuario:
     if x in vocales:
         numero = numero + 1

print (numero)
