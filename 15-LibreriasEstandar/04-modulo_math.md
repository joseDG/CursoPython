## **Modulo Math**

El modulo *math* nos va a dar acceso a una serie de funciones matematicas y constantes matematicas que te seran utiles en algun programa que desarrolles.

El modulo math es muy amplio, aqui vamos a ponerte aquellas funciones y constantes mas importantes y relevantes, si quieres ver todas las funciones y constantes incluidas

## **Las funciones siguientes**

- **fabs:**
  - Funciones que retornan el valor absoluto de un numero.
- *Factorial***
  - Funciones que calcula el factorial de un numero
- **isnan**
  - Funcion que comprueba si el parametro
- **log**
  - funcion que calcula el algoritmo en base x
- **pow**
  - funcion que calcula la potencia de un numero
- **sqrt**  
  - funcion que calcula la raiz cuadrada de un numero
- **acos**
  - funcion que calcula el arcocoseno en radianes
- **asin**
  - funcion que calcula el arcoseno en radianes
- **atan**
  - funcion que calcula la arcontagente en radianes
- **cos**
  - funcion que calcula el coseno en radianes
- **sin**
  - funcion que calcula el seno en radianes
- **tan**
  - funcion que calcula la tangente en radianes
- **degress**
  - funcion que convierte un angulo en radianes en grados
- **radians**
  - funcion que convierte un angulo en grados

### *Ejercicios*

```
import math
print("El valor absoluto de -123 es", math.fabs(-123))
print("El factorial de 7 es:", math.factorial(7))
print("El maximo comun divisor de 9 y 15  es: ", math.gcd(9,15))
print("isnan(3):",math.isnan(3))
print("El logaritmo en base 10 de 100 es: ", math.log(89,10))
print("El valor de 3 elevado a 4 es: ", math.pow(3,4))
print("La raiz cuadrada de 49 es: ", math.sqrt(49))
print("El angulo 1.23 es gardo es: ", math.radians(90))
print("El seno de un angulo de 90 es", math.sin(math.radians(90)))
print("El arcoseno de 1 es: ", math.degrees(math.asin(1)))


print("El valor de pi es: ", math.pi)
print("El valor de e es: ", math.e)
print("El valor de tau es: ", math.tau)
print("El valor de infinito es: ", math.inf)
print("El valor de NaN es: ", math.nan)
```