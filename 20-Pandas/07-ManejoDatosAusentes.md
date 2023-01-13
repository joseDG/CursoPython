## Manejo de datos Ausentes

Pandas toma a los calores NaN y None como valores ausentes La funcion *pandas.isnull()* se puede usar para determinar si existen valores ausentes en los datos.

``` 
import numpy as np
import pandas as pd
```

``` 
df = pd.DataFrame({
    'VarA': ['aa', None, 'cc'],
    'VarB': [20, 30, None],
    'VarC': [1234, 3456, 6789]
    }, 
    index = ['Caso1','Caso2','Caso3']
)

df

pd.isnull(df)
```
Debemos decidir si descartamos las filas que incluyen valores ausentes, esto lo conseguimos usando el metodo *.dropna()*

```
df.dropna(subset=["VarA",'VarB'])
```

Otra opcion es sustituir los valores *NaN* con un valor determinado, para esto usamos el metodo *.fillna()*

``` 
df.fillna("")

df.fillna(df.mean())

df.fillna(25)
```