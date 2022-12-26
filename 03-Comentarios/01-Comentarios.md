## **Comentarios de código** ☑ 

En este apartado vamos a adentranos en los comentarios de codigo fuente, explicando para que sirve, como se utilizan en Python y una serie de recomendaciones a la hora de utilizar.

### **¿Que Son?**

Los comentarios de codigo son una utilidad de programacion que permiten explicar el codigo fuente.Los usos mas comunes qeu se le dan a los comentarios son para explicar el funcionamiento de una porcion de codigo fuente, los parametros de entrada y salida de una funcion o metodo.

*Existen dos formas diferentes*

- **Comentarios de una unica linea:**
  - El comentario es escrito unicamente en una unica linea y normalmente hace referencia a una instruccion de codigo.
- **Bloque de comentarios:**
  - El comentario es escrito en varias lineas y normalmente hacen referencia a un bloque e instruccion.


## ** Comentarios de Codigo Python** 🐍 

En python podemos utilizar los dos tipos de comentarios de codigo fuente que hemos visto en el punto anterior, veamos como utilizar.

#### ** Comentarios de una unica linea **

Hay que poner el caracter '#' al comienzo de la linea para indicarle que esa linea es un comentario.

```
# Peticion de los numeros a restar
minuendo = float(input("Introduzca ek minuendo"))

#Muestra por pantalla la resta de los numeros solicitados
print("Resultado del minuendo: ", minuendo)
```

#### **Bloque de comentarios **

Hay que poner los caracteres ''' (triple comilla doble) al comienzo de la primera linea del bloque y al final de la ultima linea del bloque.

```
"""Pide el minuendo y el sumando y muestra por pantalla el resultado de la resta"""

```

## ** Recomendaciones y Buenas Practicas

Una vez hemos entendido que son los comentarios, para que sirven y como se utilizan, tenemos que tener presente una serie de recomendaciones a la hora de utilizarlos:

- **1. No llenar todo el codigo fuente de comentarios:**
    -  la documentacion dentro del codigo fuente es importante pero es necesario seguir una serie de buenas practicaas.

- **1. No llenar todo el codigo fuente de comentarios:**
    -  la documentacion dentro del codigo fuente es importante pero es necesario seguir una serie de buenas practicaas.

- **2. Utilizacion de comentarios utiles:**
    -  siempre que uses comentarios es porque realmente se necesita, si no lo haces asi llenaras el codigo.

- **3. Manatenimiento de comentarios:**
    -  al igual que el codigo fuente, los comentarios hay que irlos maneteniendo por lo tanto cada vez que se canbie algo.

- **4. Anadir comentarios mientras codificas:**
    -  nunca dejes para el final el anadir comentarios al codigo.

- **5. No comentar codigo eliminado:**
    -  una practica muy comun en el mundo del desarrollo es meter dentro de comenraios.

- **6. Mismo estilo:**
    -  sigue siempre el mismo estilo a la hora de anadir comentarios al codigo fuente.


- **7. Utiliza etiquetas dentro de los comentarios:**
    -  una buena practica dentro de los comentarios es andair etiquetas, no solo para buscar mas rapidamente el comentario..