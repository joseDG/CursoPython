print("Bienvenido ala calculadora de propinas!")
propina = float(input("Cuanto es el total de la propina $"))
porcentaje = int(input("Cual seria el porcentaje de la propina? 10, 12, or 15? "))
personas = int(input("Cuantas personas nos dividimos?"))

tipo_porcentaje = porcentaje / 100
total_porcentaje = propina * tipo_porcentaje
total_propina = propina + total_porcentaje
dividir_personas = total_propina = propina / personas
final = round(dividir_personas, 2)

print(f"Valor que da cada persona para pgar: ${final}")