def EsParOImpar(param):
    if param%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

numero = int(input("Introduce un numero:"))
EsParOImpar(numero)