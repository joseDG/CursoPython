def SumarMultiplicar(param1, param2):
    return  Sumar(param1, param2), Multiplicar(param1, param2)

def Sumar(sumando1, sumando2):
    return sumando1 + sumando2

def Multiplicar(multiplicando, multiplicar):
    return  multiplicando * multiplicar

numero1 = int(input("Introduce el primer numero: "))
numero2= int(input("Introduce el segundo numero: "))
resultadosuma, resultadomultiplicacion = SumarMultiplicar(numero1,numero2)
print("El resultado de la suma es: ", resultadosuma)
print("El resultado de la multiplicacion es: ", resultadomultiplicacion)