print("Inciando el programa")
print("Comenzando primera parte del programa")
try:
    print(str(17/0))
except:
    print("ERROR: Division por cero")
else:
    print("INFO: no se han producido errores")
finally:
    print("Primera parte de programa acabada")

print("Comenzando segunda parte del programa")
try:
    print(str(17/1))
except:
    print("ERROR: Divisor por cero")
else:
    print("INFO: nose han producido erroes")
finally:
    print("Segunfa parte de programa acabada!")