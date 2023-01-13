## Muestas Aleatorias

```
import numpy as np
import pandas as pd
```

``` 
def CrearDataSet(Num=1):
    
    Output = []
    
    for i in range(Num):
        
        # Crear un rango de fechas semanal (De lunes a lunes)
        rng = pd.date_range(start='1/1/2016', end='12/31/2020', freq='W-MON')
        
        # Crear valores aleatorios
        data = np.random.randint(low=25,high=1000,size=len(rng))
        
        # Estatus posibles
        status = [1,2,3]
        
        # Lista de estatus aleatorios
        random_status = [status[np.random.randint(low=0,high=len(status))] for i in range(len(rng))]
        
        # Locales posibles
        locales = ['Libertador','El Hatillo','El hatillo','Chacao','Baruta','Sucre']
        
        # Crear una lista aleatoria de estatuses
        random_locales = [locales[np.random.randint(low=0,high=len(states))] for i in range(len(rng))]
    
        Output.extend(zip(random_locales, random_status, data, rng))
        
    return Output
```

``` 
dataset = CrearDataSet(4)

df = pd.DataFrame(data=dataset, 
                  columns=['Local','Estatus_local','Cantidad_Clientes','Fecha_Status'])
df
```

### *np.random.choice()*

Esta funcion extrae una muestra aleatoria a partir de un array unidimencional.

```
filas = np.random.choice(df.index, 10, replace=False)

filas


df.loc[filas]
```