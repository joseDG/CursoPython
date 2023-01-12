``` 
import numpy as np
import pandas as pd
```

``` 
df = pd.DataFrame(
                  np.random.randint(low=0, high=10, size=(10, 2)),
                  index=['a','b','c','d','e','f','g','h','i','j'],
                  columns=["Cod_empleado","Calificacion"]
                 )
df
```

```
df['Calificacion']
```

### Seleccionar con *.loc*

``` 
df.loc['a']

#2
df.loc['b':'f']

#3
df.loc[df.index[3:7],'Cod_empleado']
```
### Seleccionar con *.iloc*

``` 
df.iloc[0:3]

#
df.iloc[3:]
```