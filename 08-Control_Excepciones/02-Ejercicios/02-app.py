print("Iniciamos el programa")
print("\nComenzando primera parte del programa")

try:
    print(str(17/0))
except:
    print("Error: Divisor por cero")
finally:
    print("\nComienzo segundo parte del programa")

print("\n Comenzando segundo parte del programa")

try:
    print(str(17/1))
except:
    print("Eror: Divisor por cero")
finally:
    print("Segunda parte de programa acabada!")