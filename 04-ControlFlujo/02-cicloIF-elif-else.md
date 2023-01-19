## **IF / ELIF / ELSE**

La sentencia *if* forma parte de un conjunto de sentencias encargadas de bifurcar la ejecucion del codigo fuente dependiendo de una serie de condiciones.

- **if**
  - La sentencia *if* evaluará el resultado de la Operación Lógica, en casi de que el resultado de la operacion sea True se ejecutara *Bloque Instrucciones1*.
  
- **elif**
  - La sentencia *elif* evaluara el resultado de la Operacion Logica 2,en caso de que el resultado de la operacion sea True se Ejecutara BloqueInstrucciones2

- **else**
  - La sentencia *else* no realiza la evaluacion de ningun operación, simplemente ejecutara el Bloque3

```
numero1 = GenerarNumero

numero2 = GenerarNumero

if numero1 > numero2
  BloqueIntrucciones1

elif numero1 != numero2
  BloqueInstrucciones2

else
  BloqueInstrucciones3
```  

### Ejercicio1

```
numero = int(input("Escriba un numero del 1 al 1000: "))
if numero < 400:
  print("El numero que has escrito es menor que 400")
print("Has escrito el numero " + str(numero))
```


### Ejercicio2

```
cadena = input("Introduzca una cadena de texto: ")
if cadena.endswith("a")  or cadena.endswith("e") or cadena.endswith("i") or cadena.endswith("o") or cadena.endswith("u"):
  print("La cadena de texto acaba en vocal!")
print("Has escrito: " + cadena)
```

### Ejercicio3

```
numero = int(input("Escriba un numero del 1 al 1000: "))
if numero < 400:
  print("El numero que has escrito es menor que 400")
else:
  print("El numero que has escrito es mayor o igual a 400")
print("Has escrito el numero " + str(numero))
```

### Ejercicio4

```
sumando1 = int(input("Escriba el primer sumando: "))
sumando2 = int(input("Escriba el segundo sumando: "))
resultado = sumando1 + sumando2
print("El resultado de la suma es:" + str(resultado))
if resultado % 2 ==0:
  if resultado >= 1000:
    print("El resultado de la suma es par y mayor o igual que 1000")
  else:
    print("El resultado de la suma es par y menor que 1000")
else:
  if resultado >= 1000:
    print("El resultado de la suma es impar y mayor que 1000")
  else:
  print("El resultado de la suma es impar y menor que 1000")  
```

### Ejercicio5

```
numero1 = int(input("Escriba el primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))
if numero1 == numero2:
  print("Ambos numero son iguales")
elif numero1 > numero2:
  print("El primer numero es mayor que el segundo")
else:
  print("El primer numero es menor que el segundo")
```

### Ejercicio6

``` 
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

```