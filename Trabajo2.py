#Ejercicio 2 Conversor de monedas con Euro de valor fijo 0.93
print("Conversor de moneda: Dólar a Euro (valor 0.93)")
dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
tipo_cambio = 0.93
conversion = dolares * tipo_cambio
print("Usted convirtió", dolares, "Dólares a", conversion, "Euros")
