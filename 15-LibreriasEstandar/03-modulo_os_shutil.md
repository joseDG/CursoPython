## **Modulo OS y Shutil**

El modulo *os* nos va a permitir interactuar con el sistema operativo y manejar todas aquellas funcionalidades que ofrece.

El modulo *os* es un modulo muy amplio y algunas de sus funcionalidades requiren conocimientos profundos de sistemas operativos, por lo que en este punto vamos hacer un pequeno ejercicio simplemente para mostrarte como se utilizan con una serie de funciones.

### **Funciones Principales**

- **getwd**
  - devulve al directorio actual de trabajo de la aplicacion
- **chdir**
  - cambia el directorio de trabajo de la aplicacion pasada por parametro
- **getpid**
  - devulve el identificador del proceso del aplicativo
- **getuid**
  - devuelve el identificador del usuario del proceso del aplicativo


### **Ejercicio**

```
import os

print("Director de trabajo actual: ", os.getcwd())
os.chdir("/Users/jose/Desktop/")
print("Nuevo direcctorio de trabajo: ", os.getcwd())
print("Id del proceso: ", os.getpid())
print("Id del usuario del proceso: ",os.getuid())
```

En el segundo ejercicio vamos aprender a utilizar el modulo *shutil* que nos va a permitir administrar ficheros de forma sencilla

### **Modulos *os* vamos aprender **

- **listdir:**
  - lista el contenido del directorio de trabajo actual
- **mkdir:**
  - crea un nuevo directorio dentro del directorio de trabajo actual
- **rename:**
  - renombra un fichero
- **copy:**
  - realizar la copia del fichero parameterizado en un nuevo con el nombre especificado por parametro
- **move:**
  - mueve el fichero especificos por parametros a la ruta especificada por parametro

```
import os 
import shutil

print("Cmabiando directorio de trabajo")
os.chdir("/Users/alfredo/Desktop")
print("Nuevo directorio de trabajo:", os.getcwd())
print("Contenido del directorio: ", os getcwd())
```