## Funciones 

Una funcion es un bloque de codigo fuente que contiene un conjunto de
instrucciones que realiza algo concreto y que puede ser utilizada desde el codigo
fuente que escribes tantas veces como necesitas.

*Caracteristicas de las funciones*
- Tiene un nombre para ser identificadas
- Ejecutan un a tarea concreta
- Puede recibir parametros para su ejecucion
- Puede devolver un resultado como resultado de su ejecucion.

Las funciones pertenecen a un tipo de programacion que se llama
programacion estructurada, tiene las siguientes ventajas:

- **Modularizacion:**
  - Permiten segmentar el codigo fuente complejo en un conjunto
    de modulos que hace que el codigo fuente sea mas sencillo
    de leer , depurar y mantener.

- **Reutilizacion:**
  - Permiten reutilizar las funciones en otros programas o 
    modulos del mismo programa.

### *Sintaxis de las funciones*

```
def NombreFuncion(parametros):
    BloqueInstrucciones
    return ValorRetorno 
```

### *Otra forma de expresar las funciones*

```
Variable = NombreFuncion(parametros)
```

### *Funciones con variables globales*

Existen una forma para que las variables que se utilizan dentro de la funcion
sea las variables del programa principal.Para ello es necesario anadir una sentencia
dentro de la funcion y antes de definir la variable.

- *globalNombreVariable*
- *nonlocalNombreVariable*

