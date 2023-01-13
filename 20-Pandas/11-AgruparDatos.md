## Agrupar datos

``` 
import numpy as np
import pandas as pd
```

``` 
data = pd.read_csv(r'C:\Users\ldavidr\Desktop\data_celular.csv',
                   header=0,
                   index_col=0,
                   names=['indice', 'fecha','duracion','item','mes','red','tipo_red'],
                   parse_dates=['fecha'])
data.head()
```

Podemos obtener informacion basica seleccionado columnas y aplicando algunas de las operaciones que ya conocemos.

``` 
print('Cuántas filas tiene el DataFrame: ')
print(data['item'].count())
```

```
print('El tiempo total (en segundos) registrado en llamadas es:')


print(data['duracion'][data['item'] == 'call'].sum()) 
```

```
print('Con cuántas redes telefónicas se contactó en el período de 2014/11 al 2015/03: ')
print(data['red'].nunique()) 
```

### *groupby()*

Este metodo nos permite agrupar nuestros datos para obtener informacion segregada.

``` 
data.groupby('mes')
```

```
data.groupby('mes').groups.values()
```

```
data.groupby('mes').sum() 
```

```
print('En el siguiente cuadro vemos la cantidad de entradas por mes \n segregadas en llamadas, sms y datos: \n \n')

print(data.groupby(['mes','item'])["duracion"].count()) 
```

```
print('La duración total de las llamadas realizadas a cada una de las operadoras es: ')

data[data['item'] == 'call'].groupby('red')['duracion'].sum() 
```

```
print('¿Cuántas llamadas, sms y datos son enviados a cada operadora por mes? : ')

data.groupby(['mes', 'tipo_red'])['fecha'].count() 
```