#CALCULADORA BMI
#calcular el peso corporal de las personas
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

bmi = peso / altura ** 2
print(f"tu peso corporal :",round(bmi, 2),"kg/m2")




