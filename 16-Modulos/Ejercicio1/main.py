import operaciones

def Sumar():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print("La suma es: ", operaciones.Sumar(sum1, sum2))

def Restar():
    minuendo = int(input("Minuendo:"))
    sustraendo = int(input("Sustraendo:"))
    print("La resta es: ", operaciones.Restar(minuendo,sustraendo))

def Multiplicar():
    multiplicando = int(input("Multiplicando:"))
    multiplicador = int(input("Multiplicador:"))
    print("La Multiplicacion es: ", operaciones.Multiplicar(multiplicando,multiplicador))

def Dividir():
    dividendo = int(input("Dividendo:"))
    divisor = int(input("Divisor:"))
    print("La Division es: ", operaciones.Dividir(dividendo,divisor))

def Factorial():
    factorial = int(input("Introduzca el numero del que quiere calcular el factorial: "))
    print("El factorial de " + str(factorial) + " es: " + str(operaciones.Factorial(factorial)))

def Potencia():
    base = int(input("Introduzca la base de la potencia: "))
    exponente = int(input("Introduzca el exponente de la potencia: "))
    print("El valor de " + str(base) + " elevado a " + str(exponente) + " es: " + str(operaciones.Potencia(base,exponente)))

def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opcion:"))
        if (opc == 1):
            Sumar()
        elif (opc == 2):
            Restar()
        elif (opc == 3):
            Multiplicar()
        elif (opc == 4):
            Dividir()
        elif (opc == 5):
            Factorial()
        elif (opc == 6):
            Potencia()
        elif (opc == 7):
            fin = 1
print("""==========
|   Calculadora   |
================
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Factorial
6) Potencia
7) Salir""")
Calculadora()
