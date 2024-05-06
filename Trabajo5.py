print("Conversor de Temperatura")
print("1. Convertir de Celsius a Fahrenheit")
print("2. Convertir de Fahrenheit a Celsius")

opcion = int(input("Seleccione una opción (1 o 2): "))

if opcion == 1:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en grados Fahrenheit es:", fahrenheit)
elif opcion == 2:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("La temperatura en grados Celsius es:", celsius)
else:
    print("Opción no válida. Por favor seleccione 1 o 2.")
