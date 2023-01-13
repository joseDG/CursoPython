## Operaciones sobre datos agrupados

```
import numpy as np
import pandas as pd
```

```
ratings = pd.read_csv(r'C:\Users\ldavidr\Desktop\ratings.csv')

peliculas = pd.read_csv(r'C:\Users\ldavidr\Desktop\peliculas.csv')

usuarios = pd.read_csv(r'C:\Users\ldavidr\Desktop\usuarios.csv') 
```

```
ratings.head() 
```


```
peliculas.head() 
```

Un ratinf requiere un usuario y una pelicula, y los DataFrame estan vinculados por una clave (en este caso la clave es *user_id* y *peli_id*)

Es posible que un usuario este asociado con 0 o varios ratings y peliculas. de las misma forma, una pelicula puede teern muchos ratings o ninguno po un numero de diferentes usuairos.

```
peli_ratings = pd.merge(peliculas, ratings)

clasif = pd.merge(peli_ratings, usuarios)
```

```
mas_ratings = clasif.groupby('titulo').size().sort_values(ascending=False)[:25]

mas_ratings 
```

## *.agg()*

Este metodo nos permite aplicar una lista de funciones en columna especificas del DataFrame

Deseamos conocer el rating promedio de cada pelicula

```
peli_stats = clasif.groupby('titulo').agg({'rating': [np.size, np.mean]})

peli_stats.head()
```

```
peli_stats.sort_values([('rating', 'mean')], ascending=False).head()
```

```
minimo_100 = peli_stats['rating']['size'] >= 100

minimo_100
```

```
peli_stats[minimo_100].sort_values([('rating', 'mean')], ascending=False)[:15]
```