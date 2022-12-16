## **Cadenas**

### *1. Ejercio probando todos los elemtos*

```
cadena1 = input("Introduzca la primera cadena:")
cadena2 = input("Introduzca la segunda cadena:")
cadena3 = input("Introduzca la tercera cadena:")

print("Longitud de la cadena2 (len):", len(cadena1))
print("Cadena3 todas a mayusculas (upper):", cadena3.upper())
print("Cadena3 todas a minusculas (lower):", cadena3.lower())
print("Cadena2 cambia de mayusuculas a minusculas y viceversa (swapcase):",cadena2.swapcase())
print("Cadena1 la primera a mayusuculas (capitalize):",cadena1.capitalize())
print("Cadena2 la primera de cada palabra a mayusculas (title):", cadena2.title())
print("¿Cadena1 todo minusculas? (islower):", cadena1.islower())
print("¿Cadena3 todo mayusculas? (isupper):", cadena3.isupper())
print("¿Cadena2 todo caracteres imprimibles? (isprintable):", cadena2.isprintable())
print("¿Cadena3 todo caracters alfanumericos? (isalnum):", cadena3.isalnum())
print("¿Cadena1 todo caracteres alfabeticos? (isalpha):", cadena1.isalpha())
print("¿Cadena3 la primera de cada palabra en mayusculaas y el resto en minusculas? (istitle):", cadena3.istitle())
print("Cadena2 todo los caracteres son espacios en blanco? (isspace):", cadena2.isspace())
print("¿Cadena1 todo digitos? (isdigit):", cadena1.isdigit())
print("¿Cadena2 todos los caracteres con representacion numerica?(isnumeric):", cadena2.isnumeric())
print("¿Cadena3 todos los caracteres son numeros con representacion decimal? (isdecimal):", cadena3.isdecimal())
print("Caracter mas alto de la cadena1 (max):", max(cadena1))
print("Caracter mas bajo de la cadena3 (min):", min(cadena3))
```

### *2. Eliminiar caracteres de espacios en blanco de la cadena solicitada al usuario*

```
cadena = input("Introduzca una cadena con espacios en blanco al principio y al final:")

print("Longitud de la cadena:", len(cadena))
cadenalstrip = cadena.lstrip()
print("Cadena (lstrip):", cadenalstrip, end='.')
print("\nLongitud de la cadena (rstrip):", len(cadenalstrip))
cadenastrip = cadena.strip()
print("Cadena (strip):", cadenastrip, end='.')
print("\nLongitud de la cadena (strip):", len(cadenastrip))
```

### *3. Comprobar si una cadena empieza y termina por otra y en contar cuantas veces aparece dicha cadena en la cadena base*

```
cadena = input("Introduzca una cadena:")
buscar = input("Introduzca una cadena para buscar:")
print("¿Comienza la cadena por la cadena a buscar? (startswith):", cadena.startswith(buscar))
print("¿Termina la cadena por la cadena a buscar? (endswith):", cadena.endswith(buscar))
print("¿Cuantas veces aparece la cadena a buscar en la cadena? (count):", cadena.count(buscar))
```

### *4. Consiste en realizar de una busqueda de izquierda a derecha y de derecha a izquierda de una cadena de texto en otra.*

```
cadena = input("Introduzca una cadena:")
buscar = input("Introduzca una cadena para buscar:")
print("La cadena aparece en la posicion (find):", cadena.find(buscar))
print("La cadena aparece en la posicion (rfind):", cadena.rfind(buscar))
```

### *5. Consite en el reemplazo de una cadena de texto de una cadena de texto base por otra cadena de texto.*

```
cadena = input("Introduzca una cadena:")
reemplazar = input("Introduzca una subcadena de la anterior para reemplazar:")

reemplazo = input("Introduzca la cadena por la que se reemplazara la anterior:")
print("Cadena original:", cadena)
print("Cadena nueva (replace):", cadena.replace(reemplazar, reemplazo))
```

### *6. Consite en crear una lista de cadenas de texto a partir de las palabras que componen la cadena de texto.*

```
cadena = input("Introduzca una cadena con varias palabras:")
print("Cadena dividida por espacios en blanco (split):", cadena.split())
```