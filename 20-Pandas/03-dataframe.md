## DataFrames

Un **DataFrame** es un estructura de datos que almacena datos de forma tabular, es decir, ordena en filas y columnas etiquetas.Cada fila **(row)** contiene una observacion y cada columna **(columna)** una variable.

un **DataFrame** acepta datos heterogeneos, o se, las variables pueden ser de distintos tipos (numerico, string, boolean, etc).

Ademas de contener datos, un **DataFrame** contiene el nombre de las variables y sus tipos, y metodos que permiten acceder y modificar los datos.

```
import numpy as np
import pandas as pd  
```

``` 
data = {
    'ciudades': ['Caracas', 'Guadalajara', 'La Habana', 'Cancún', 'Guasdalito'],
    'poblacion': [100000, 200000, 340000, 210000, 300000],
    'infectados': [6000, 4000, 35000, 4300, 3002]
}

df = pd.DataFrame(data)
df
```

``` 
df.ciudades
df.dtypes
```


