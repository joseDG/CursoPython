name1 = input("Ingrese el nombre de estudiante 1: ")
id1 = input("Ingrese ID del estudiante 1: ")
grade1 = float(input("Ingrese la nota del estudiante 1: "))
print("\n")
name2 = input("Ingrese el nombre de estudiante 2: ")
id2 = input("Ingrese ID del estudiante 2: ")
grade2 = float(input("Ingrese la nota del estudiante 2: "))

print('\n\nInformacion de los estudiantes grado Matematicas:')
msg = "(ID " + id1 + ")",name1 + " Nota: " + str(grade1)
print(msg)

msg = "(ID " + id2 + ")",name2 +" Nota: " + str(grade2)
print(msg)

print("\n")
promedio = (grade1 + grade2) / 2.0
print("El promedio del grado es", promedio)