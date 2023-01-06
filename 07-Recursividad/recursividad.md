## Recursividad

El uso de funciones recursivas se utilizan mayormente para dividir una tarea
en subtareas de menor tamano de forma que se mas facil abordar el problema y solucionarlo.
Nosotros te recomendamos que cuando hables de funciones recursivas pienses en bucles, 
ya que el codigo permite una y otra vez hasta llegar a la solucion final.

Las funciones o algoritmos recursivos tienen que cumplir las siguientes tres reglas:

- 1. Un algoritmo recursivo debe tener un caso base.
- 2. Un algoritmo recursivo debe cambiar su estado y moverse hacia el caso base.
- 3. Un algoritmo recursivo debe llamarse a su mismo, recursivamente.

**Existen dos casos:**

El **caso base** de un algoritmo recursivo es aquel que nos permite terminar
la funcion en algun momento.Su objetivo es que se dejen de realizar llamadas
recursivas de forma infinita.

El **caso recursivo** de un algoritmo recursivo es aquel en el que se llama de nuevo
a si mismo. Cada llamada recursiva qeu se haga implicara que se esta mas cerca de llegar al caso
base del algoritmo recursivo

Es importante tener claro el caso base y saber que el caso recursivo se va
acercando a este y no entra en un estado de llamadas infinitas, es un error comun cuando se comienza
con recursividad.

