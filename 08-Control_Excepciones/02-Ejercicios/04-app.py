print("Inciando programa")
try:
    print(str(17/0))
except ZeroDivisionError:
    print("EROR: Division de cero")
except:
    print("No se han producido errores")
finally:
    print("Programa acabado")