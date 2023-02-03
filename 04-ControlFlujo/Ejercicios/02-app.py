#leap year
year = int(input("Cual es el ano que tu quieres agregar? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")