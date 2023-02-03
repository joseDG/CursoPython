#Montana rusa
print("¡Bienvenido a la montaña rusa!")
altura = int(input("¿Cuál es tu altura en cm?"))
factura = 0

if altura >= 120:
    print("¡Puedes subir a la montaña rusa!")
    edad = int(input("¿Cuál es tu edad?"))
    if edad < 12:
        factura = 5
        print("Los boletos para niños cuestan $ 5")
    elif edad <= 18:
        factura = 7
        print("Los boletos para jovenes cuestan $ 7")
    elif edad >= 45 and edad <= 55:
        print("Todo va a estar bien. ¡Disfruta de un viaje gratis con nosotros!")
    else:
        factura = 12
        print("Los boletos para adultos cuestan $ 12")

    quire_foto = input("¿Quieres que te saquen una foto? Y o N.")
    if quire_foto == "Y":
        factura += 3

    print(f"Tu factura final es de $ {factura}")
else:
    print("Lo sentimos, tienes que crecer más alto antes de poder montar")