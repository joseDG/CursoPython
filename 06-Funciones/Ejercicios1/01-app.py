def Variables():
    global variable
    print("Valor dentro de la funcion: " + str(variable))
    variable = 3
    print("Valor dentro de la funcion: " + str(variable))

variable = 5
print("Variable en el programa principal: " + str(variable))
Variables()
print("Variable en el programa principal: " + str(variable))