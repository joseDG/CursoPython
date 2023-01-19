## **Modulo Random**

El modulo *random* va a permitir hacer elecciones de forma aleatoria, tanto elegir al azar un valor de una lista como generar numeros aleatorios u obtener un numero al azar dentro de un rango.

## Funciones Importantes
- **randrage**
  -devuleve un numero aleatorio en un rango especifico por parametro.
- **sample**
  - devulve una lista de numeros aleatorios dentro de un rango establecido por parametro.

- **random**
  - devulve un numero en coma flotante.

- **choice**
  - selecciona un elemento de la lista que recibe por parametro al azar.

## *Ejercicios*

```
import random

print("Numero aleatorio del 1 al 1000: ", random.randrange(1000))
print("Lista alaeatoria de numeros entre el 1 y el 1000:", random.sample(range(1000), 3))
print("Numero aleatorio en coma flotante: ", random.random())
print("Eleccion aleatoria [Python, Java, C#, Ruby]: ", random.choice(['Python','Java','C#','Ruby','Go'])) 
```