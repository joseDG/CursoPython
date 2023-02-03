#Calcular cuantos dias semanas y meses tienes hasta ahora

age = input("Cual es tu edad actual? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"Tu tienes {days} dias, {weeks} semanas, y {months} meses.")
