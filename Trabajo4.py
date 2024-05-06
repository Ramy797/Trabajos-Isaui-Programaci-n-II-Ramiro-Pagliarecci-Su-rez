#Ejercicio 4 Desarrolla un programa en Python que solicite al usuario que ingrese una frase y luego cuente y muestre el número de palabras en esa frase.

print("Contador de palabras en una frase")
frase = input("Ingresa una frase: ")
palabras = frase.split()
CantPalabras= len(palabras)
print("El número de palabras en la frase es:", CantPalabras)
