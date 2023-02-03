# with open("a_file.txt") as file:
#     file.read()

#Key Error
# a_dictyonary = {"key": "value"}
# value = a_dictyonary["non_existent_key"]

#IndexError
# fruits_list = ["Apple", "Banana", "Orange"]
# fruit = fruits_list[3]

#Excepciones que exsiten en pYthon
#try:
#except:
#else:
#finally:

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key", "value"}
#     print(a_dictionary["asdasd"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} dos not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was close")

#Cerate example self
heigth = float(input("Height: "))
weight = float(input("Weight: "))

if heigth > 3:
    #sirve para hacer excepctios propias 
    raise ValueError("Human height should not be over 3 meters. ")

bmi = weight / heigth ** 2
print(bmi)