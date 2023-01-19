## **Bases de datos Python**

En esta apartado se van a explicar los conceptos basicos para entender que es una base de datos, por qeu es beneficioso utilizarlas, tipos de base de datos existentes, el modelo relacional.

### **¿Que es una base de datos?**

Las bases de datos son uno de los elementos informaticos mas importantes que existen en la actualidad y juegan un papel fundamental en la sociedad moderna e informatizada.

Una base de datos es un cojunto de datos de cualquier tipo que pertenecen a un mismo contexto y que son almacenados para ser usados posteriormente.Una base de datos debe permitir alamcenar para ser utilizado.

### **Tipos de bases de datos**

- **Bases de datos jerarquicas**
  - alamacenan la informacion en una estructura jeraquica es decir almacenar la informacion de arbol en el que un nodo padre tiene as hijos.
- **Bases de datos en red**
  - es una evolucion de las bases de datos jerarquicas pero permitiendo que un nodeo puede tener 1 o mas padres.
- **Bases de datos relacionales**
  - es el modelo mas utilizado en la actualidd
- **Bases de datos orientada a objetos**
  - es un tipo de base de datos de reciente creacion y se surgiere a partor de la aparcicion de la programacion.
- **Bases de datos documentales**
  - son bases de datos especializadas en el almacenamiento
- **Bases de datos transaccionales**
  - es un tipo de base de datos optimizada par ael envio y recepcion continuo
- **Bases de datos deductivas/logicas**
  - son bases de datos capaces de deducir informacion mediante el uso de inferencia contra los datos.
- **Bases de datos distribuidas**
  - es una base de datos que parece ser unica pero que esta compuesta.

### **Modelo entidad-realcion**

El modelo entidad-relacion es el modelo de representacion de la estructura de las bases de datos relacionales. El modelo representa la base de datos con un a serie de diagramas.

Entidad
- libros
- Autor
- Biblioteca

Atributos
- titulo
- editorial
- Isbn

### **Relacion**
 Las relaciones son los conceptos mas dificiles de crear en una base de datos ya que tienen cardinalidad como veremos mas adelante.Existen diferencias formas de implementar en una base de datos, en algunas casos se utilizara una tabla para relacionar.


**Uno a uno**
![uno a varias](/assets/img/1.png)

**Uno a varios**
![uno a varias](/assets/img/2.png)

**Varios a varios**
![uno a varias](/assets/img/3.png)