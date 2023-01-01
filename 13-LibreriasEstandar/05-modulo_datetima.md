## **Modulo Datetime**

El modulo *datetime* es probablemente uno de los mas grande incluidos dentro de la libreria estandar de Python y va a permitir manipular fechas de forma sencilla.

En este apartado vamos a ezplicarte una serie de funciones que son basicas para trabajar con fechas.Existen funciones mucho mas complejas pero que no se utilizan mucho

### **Funciones**

- **datetime.now**
  - funcion que retorna la fecha y la hora de hoy mismo.
- **date.today**
  - funcion que retorna el dia de hoy
- **date**
  - funciones que permiten crear un objeto de tipo fecha pasandole como parametro anos, meses
- **datetime**
  - funcion que permite crear un objeto de tipo Datetime pasandole parametros el ano, el mes y el dia y la hora los segundo de microsegundos.

### **Ejemplo 1**

```
import datetime

print("El dia y la hora de hoy es: ", datetime.datetime.now())
print("El dia de hoy es: ", datetime.date.today())
fecha = datetime.date(1984,5,10)
print(fecha)
fechahora = datetime.datetime(2017,11,29,23,19,00,123)
print(fecha) 
```
### **Ejemplo 2**

``` 
import datetime

fecha = datetime.datetime(2017,11,29,23,19,00,123)
print(fecha)
print("Ano: ", fecha.year )
print("Mes: ", fecha.month )
print("Dia: ", fecha.day )
print("Hora: ", fecha.hour )
print("Minutos: ", fecha.minute )
print("Segundos: ", fecha.second )
print("Microsegundos: ", fecha.microsecond )
```

### **Ejemplo 3**

``` 
import datetime

ahora =  datetime.datetime.now()
fecha =  datetime.datetime(2017,11,29,23,19,00,123)
print("Se va a realizar la resta de las siguientes fechas")
print("1. ", ahora)
print("2. ", fecha)
resultado = ahora - fecha
print('Resultado: ', resultado)
```