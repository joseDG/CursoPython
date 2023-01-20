## Variables

Las variables son datos que utilizarás en todas los programas y que almacenarán información util para su ejecución.

Las variables estan compuestas por tres componentes:
- Nombre: Identificador dentro del código fuente que utilizamos para usarlas.
- Tipo: tipo de dato que almacena la variable.
- Valor: valor que almacena. Al declarar una variable tienes que indicarle un valor inicial, que puede verse modificado a medida que se vaya ejecutando.

Un ejemplo de uso de variables puede ser la necesidad de almacenar en tu programa algún tipo de información de los usuarios, por ejemplo el teléfono.

En python las variables se definen utilizando las letras de la A a la Z, tanto en mayusculas como en minúsculas, los números del 0 al 9 ademas puedes utilizar los caracteres "_".

Los valores con asignados a las variables con el operador asignacion "=" lo que esta ala derecha del operador será asignado.

```
#varaibles 
nombre = "Jose Diaz"
nombre 
```

```
print("Day 1 - Funcion para imprimir")
print('La funcion se declara asi')
print("print('cual imprime')") 
```

```
#crear un salto de linea
print("una mesa \nuna silla")
```
```
#creacion del input
print("Hola "+ input("Cual es tu nombre")) 
```

```
#verificar el tamano de las letras
ciudad = "Ecuador"
length = len(ciudad)
print("Tamaño de letras {1}, Palabra {0}".format(ciudad,length)) 
```

``` 
edad = 35
ciudad = "Loja"
precio = 3.13
```

## **Errores de sintaxis**
Solemos aveces poner tipos de variables de esta forma lo cual debemos de tener mucho cuidado.

``` 
xca" = 6
```

## **Palabras reservadas en *Python***
```
import keyword
keyword.kvlist  
```

## **Declaracion multiples variables en una sola linea***

```
age, name = 22, "Maria"
```

## **Formas de imprimir valores**
``` 
x = x + 2
x += 2
```

## **Formateado la salida**

El comando **print** dispone de dos parametros que nos van a permitir darle formato al mensaje.

### Ejemplo

- **sep**
  Permite modificar el caracter por defecto de espacio en blanco que se introduce de forma automatica como separador

  ```
  print(1,2,3, sep=',') 
  ```

- **end**
  permite anadir una cadena de texto como elemento final del conjunto de cadenas de texto.

  ```
  print(1,2,3, sep=',', end='.') 
  ``` 
  
```
#ejercicio completo
print("Bienvenido a tu band name genreator")
city = input("Cual es tu ciudad")
pet = input("Cual es el nombre de mascota")
print("Tu datos podrian ser: {0}, y tu mascota {1}".format(city,pet)) 
```