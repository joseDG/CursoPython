## Fechas y tiempo

```
import numpy as np
import pandas as pd
import datetime 
```

Para trabajar con valores de fecha y tiempo debemos utilizar el modulo **datetime.**

``` 
from datetime import date

d1 = date(2013,5,20)

print(d1)

print(type(d1))
```

### *datetime.date*

La clase datetime.date tiene atributos para obtener el dia, mes y el ano de la fecha.

``` 
print(d1)

# Día
print('Día :',d1.day)

# Mes
print('Mes :',d1.month)

# Año
print('Año :',d1.year)
```

El metodo date.today() nos devuelve la fecha del dia

``` 
d1 = date.today()
print(d1)

# Día
print('Día :',d1.day)

# Mes
print('Mes :',d1.month)

# Año
print('Año :',d1.year)
```

### *datetime.time*

Un objetivo de clase datetime.time tiene atributos para obtener la hora, los minutos y segundos de una hora

``` 
from datetime import time

t1 = time(15,20,13,40)

print(t1)

print(type(t1))

# Hora
print('Hora :',t1.hour)

# Minuto
print('Minuto :',t1.minute)

# Segundo
print('Segundo :',t1.second)

# Microsegundo
print('Microsegundo :',t1.microsecond)
```

### *datetime.datetime*

La clase datetime.datetime contiene tanto la informacion de fecha como de hora

``` 
import datetime

d1 = datetime.datetime.now()
d1
```

```
d1 = datetime.datetime(2020,4,23,11,20,30,40)

print(d1)

# Día
print('Día :',d1.day)

# Mes
print('Mes :',d1.month)

# Año
print('Año :',d1.year)

# Hora
print('-------------- \n Hora :',d1.hour)

# Minuto
print('Minuto :',d1.minute)

# Segundo
print('Segundo :',d1.second)

# Microsegundo
print('Microsegundo :',d1.microsecond) 
```
### *weekday()*

Este metodo nos devuelve un numero correspondiente al dia de la semana.

``` 
print(d1)
print(d1.weekday())

d1 = datetime.datetime.now()
d1

print(d1.weekday())

print(d1.isoweekday())
```

### *isocalendar()*

Este metodo nos devuelve una tupla (valor_1,valor_1,valor_1) que representa una fecha:

- **valor_1** indica el ano en formato ISO
- **valor_1** indica el semana del ano en formato ISO
- **valor_1** indica el dia de la semana en formato ISO

``` 
d1.isocalendar()
```

### Obtener fechas con otros metodos

``` 
d1_datetime = date.fromisoformat('2020-04-23')
print(d1_datetime)
print(type(d1_datetime))
```

```
d1_ISO = date(2020,4,23).isoformat()

print(d1_ISO)
print(type(d1_ISO)) 
```

### *strtime()*

Este metodo nos permite leer una cadena de texto con una fecha en un formato indeterminado como un objeto de clase
**.datetime**

### *to_datetime()*

``` 
fecha = pd.to_datetime('24th April, 2020')

print(fecha)
print(type(fecha))
```

### *to_timedelta()*
Esta funcion nos permite calcular los dias antes o despues de una fecha determinada

```
fecha = datetime.datetime.now()

print(fecha)
```

#La fecha del dia siguiente

```
 print('La fecha de hoy es: ', fecha)

print('Y la fecha en 4 días será: ', fecha + pd.to_timedelta(4,unit='D'))
```

### *date_range()*
Este metodo nos permite generar un rango de fechas.

``` 
fechas_inicio = pd.date_range(start='24/4/2020', end='24/5/2020', freq='D')
fechas_inicio
```

``` 
fechas_fin = pd.date_range(start='24/5/2020', end='24/6/2020', freq='D')
fechas_fin
```

```
lista_equis = []

for i in range(15):
    lista_equis.append(np.random.randint(2))


df = pd.DataFrame()

df['Inicio_campaña'] = fechas_inicio[:15]
df['Fin_campaña'] = fechas_fin[:15]
df['Target'] = lista_equis

df
```

```
df['Día de inicio'] = df['Inicio_campaña'].dt.day


df['Mes de inicio'] = df['Inicio_campaña'].dt.month


df['Año de inicio'] = df['Inicio_campaña'].dt.year


df['Hora_inicio'] = df['Inicio_campaña'].dt.hour


df['Minuto_inicio'] = df['Inicio_campaña'].dt.minute


df['Segundo_inicio'] = df['Inicio_campaña'].dt.second


df['Nombre del día de inicio'] = df['Inicio_campaña'].dt.weekday


df['Semana del año de inicio'] = df['Inicio_campaña'].dt.week


df['Duración'] = df['Fin_campaña']-df['Inicio_campaña'] 
```

```
df.columns = ['Inicio_campaña', 'Fin_campaña', 'Target','Día de inicio','Mes de inicio','Año de inicio','Hora_inicio',
              'Minuto_inicio','Segundo_inicio','Día de la semana del inicio','Semana del año de inicio','Duración']

df 
```

