## Control de excepciones

### *¿Que son las excepciones?*

Una excepcion es un error logico que ocurre mientras se ejecuta el programa
y que provoca su detencion.La detencion puede ser controlada y no producirse si se
realiza un control de excepciones correcto en el codigo fuente.

Controlar una excepcion no es otra cosa que guardar el estado en el que se
encontraba el programa en el momento justo del error e interrumpir el programa
para ejecutar un codigo fuente concreto.

El proceso de controlar excepciones es similar en todos los lenguajes de 
programacion.En primer lugar, es necesario incluir el codigo fuente de ejecucion
normal dentro de un bloque con la sentencia *try*.
Posteriormente , se crea un bloque de codigo dentro de una
sentecia *except* que es la se ejecutara en caso de error.

```
try:
    BloqueIntruccionesPrograma
except TipoError1:
    BloqueIntruccionesError1
    
except TipoError2:
    BloqueIntruccionesErro1
    
except TipoErrorN:
    BloqueIntruccionesErrorN
    
finally:
    BloqueCodigoFinally
```

### Detalles de cada elemento

- **try:**
  - indicador de comienzo del bloque de codigo fuente que se controlara.
- **BloqueIntruccionesPrograma:**
  - Conjunto de instrucciones que componen el programa
- **except:**
  - indicador de comienzo de excepciones
- **TipoError:**
  - indicador del tipo de eror que se controla la except.El parametro es opcional.
- **BloqueInstruccionesError:**
  - conjunto de instrucciones que se ejecutan si se produce el error.
- **finally:**
  - indicador de comienzo del bloque de codigo final.
- **BloqueCodigoFinally:**
  - conjunto de instrucciones que se ejecutan al acbar cualquier de los bloques.

### Tipos de Excepciones

En python existen diferentes tipos de excepciones qeu pueden controlarse
todas ellas derivan de una serie de expcepciones base.

- **Excepcion:**
- **AritmeticError:**
- **BufferError:**
- **LookUpError:**