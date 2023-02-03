numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Jose"
letter_list = [letter for letter in name]
print(letter_list)

range_list = [num*2 for num in range(1,2)]
print(range_list)

#Compresion de Condiciones
names = ["Alez", "Beth", "  Carolina", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
long_names = [name for name in  names if len(name) > 5]
print(long_names)