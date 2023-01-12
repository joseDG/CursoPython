## Operaciones con DataFrames

``` 
import numpy as np
import pandas as pd
```

``` 
d = [np.random.randint(50,size=(10))]
d
```

```
df = pd.DataFrame(d).T
df 
```

### *Anadir una nueva columna*

```
df['nueva_col'] = 10

```

``` 
df['experiencia'] = 5

df
```

```
df['perdidas'] = [(i+2)*np.e for i in range(10)]

df 
```

```
df['columna'] = df['perdidas']*100
df 
```
### *Cambiar el nombre de una columna*

``` 
df.columns
```

```
 df.columns = ['codigo_id','años_exp', 'indice', 'eficiencia','eficiencia_agregada']

df


df['codigo_id']
```

### *Modificar una columna*

```
df['indice'] = df['indice'] / 200

df
```

### *Eliminar una columna o una fila*
``` 
del df['eficiencia']

df
```

``` 
c = df.drop([2,3,5], axis=0)
c

df
```

``` 
df.drop(['eficiencia_agregada'], axis=1, inplace =  True)

df.head()

df
```
### *Modificar el indice*

``` 
i = ['a','b','c','d','e','f','g','h','i','j']

df.index = i

df


df["codigo_id"].mean()


df["codigo_id"].sum()


df["codigo_id"].min()


df["codigo_id"].max()
```