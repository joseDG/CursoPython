## Series

Las funcionalidades de pandas se basan en dos estructuras de datos fundamentales: Series y DataFrames.

Una **Serie** es un objeto que contiene un **array** unidimencional de datos y un **array** de etiquetas, conocido como *indice*.Si no se especifica un indice o etiquetas, este se genera internamente como una secuencia ordenada de numeros enteros.

```
#Crear un serie con indice automaticos
serie = pd.Series([1979,1980,1981,1982])
serie 
```

```
serie.values.sum()
serie.index 
```

Podemos definir explicitamento un **array** indice y pasarlo como argumento

```
serie = pd.Series([1989, 1990, 1991, 1992,1993], index=['daniela', 'valentina', 'andrea', 'sherezade', 'genesis'])

serie 

serie.index
```
Tambien se pueden crear **Series** a partir de diccionarios,**arrays**, etc

``` 
serie = pd.Series(np.random.rand(10))
serie
```

```
dicci = {'cuadrado de {}'.format(i) : i*i for i in range(11)}
dicci 
```

```
serie_dic = pd.Series(dicci)
serie_dic
```