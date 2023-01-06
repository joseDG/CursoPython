## Bucles

En este capitulo vamos a explicarte todo lo referente a as estructuras de 
programacion conocidas como bucles. En programacion podemos definir un bucle
como la repeticion de la ejecucion de un conjunto de instrucciones donde cada
repeticion del conjunto de instrucciones se llama iteracion.

### Tomar en cuenta 
- Punto de inicio del bucle
- Punto de fin bucle
- Numero de iteraciones
- Bloque de instrucciones a ejecutar.

## For
El tipo de bucle for esta recomendado para contextos en los que se sabe el
numero de iteraciones exactas que se van a dar en su ejecucion, es decir , es un bucle
que se busca ejecutar un cojunto de instrucciones de forma repetitiva hasta llegar
al numero maximo de iteraciones.

En python los bulces *for* se ejecutan en elementos iterables
como puden ser listas , tuplas, cadenas, de texto , diccionarios.El numero de iteraicones
que se ejecutaran dependera del numero de elementos de lso que estan compuestos el
elemento iterable.

```
for Variable in Coleccioniterable:
    BloqueInstrucciones 
```

## While

El tipo de bucle while esta recomendado para contextos en los que no se sabe
exactamente el numero de iteraciones que se tienen que ejecutar pero si se sabe que 
hay que ejecutar iteraciones hasta que se deje de cumplir.

La condicion que se utiliza para comprobar si se tiene que ejecutar una
iteracion debera de ser *true* para que se ejecute, la ejecucion del bucle finalizara
si la condicion tiene el valor *false*.La condicion es comprobad en cada iteracion del 
bucle.

```
while Condicion:
    BloqueInstrucciones 
```
