def Multiplicar(param1, param2):
    return  param1 * param2

multiplicando = int(input("Introduce el multiplicando: "))
multiplicador = int(input("Introduzca el multiplicador: "))
resultado = Multiplicar(multiplicando,multiplicador)
print("El resultado de la multiplicacion es: ", resultado)