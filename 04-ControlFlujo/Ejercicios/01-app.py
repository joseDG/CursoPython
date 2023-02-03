#Calculadora BMI
#"your BMI is 18, you are underweight"
#"your BMI is 22, you have a normal weight"
#"your BMI is 28, you are slightly overweight"
#"your BMI is 33, you are obese"
#"your BMI is 40, you are clinically obese"

altura = float(input("Ingresa tu altura en m: "))
peso = float(input("Ingrese tu peso en kg: "))

bmi = round(peso / altura ** 2)
if bmi < 18.5:
    print(f"Tu BMI es {bmi}, tu tienes underweight.")
elif bmi < 22.5:
    print(f"Tu BMI es {bmi}, tu tienes peso normal.")
elif bmi < 28:
    print(f"Your BMI es {bmi}, tu slight overweight")
elif bmi > 33:
    print(f"Tu BMI es {bmi} tu eres obeso")
else:
    print("Opcion incorrecta")

