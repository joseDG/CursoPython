def SumarMultiplicar(*valores):
    resultadosuma = 0
    resultadomultiplicacion = 1
    for item in valores:
        resultadosuma = resultadosuma + item
        resultadomultiplicacion = resultadomultiplicacion + item
    return resultadosuma, resultadomultiplicacion

ressuma, resmult = SumarMultiplicar(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es: ", ressuma)
print("El resultado de la Multiplicacion es: ", resmult)