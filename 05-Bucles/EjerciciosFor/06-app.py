total_height = 0
students_heading = input("ingrese la lista de estudiantes altos: ").split()
for h in students_heading:
    total_height += int(h)
total = total_height / len(students_heading)
print(total)