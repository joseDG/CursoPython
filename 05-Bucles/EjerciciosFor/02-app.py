lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","n",
         "o","p","q","r","s","t","u","v","w","x","y","z"]

listaiteraciones = [1,2,3,4,5]

for item in listaiteraciones:
    print("Iteraciones numero: " + str(item))
    for letra in lista:
        print(letra, end=" ")
    print("\n")