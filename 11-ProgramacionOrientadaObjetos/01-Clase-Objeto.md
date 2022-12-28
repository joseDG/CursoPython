## **Clase y Objeto***

Antes de empezar vamos a hacer una simil  de la programacion orientada a objetos con el mundo real.Mira a tu alrededor La repuesta es : Objetos.

Estamos rodeados de objetos, como puede ser carros, lamparas, telefonos, mesas ect... El nuevo paradigma de programacion orientada a objetos esta basado en una abtraccion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como veamos en el mundo.


**Una clase** es un tipo de dato cuyas variables llaman objetos o instancias, es decir la clase es la definicion del concepto del mundo real y los objetos o instancias son propios del "objeto".


La clase esta compuesta por dos elementos:
  - **Atributos**
    - informacion que almacena la clase.
  - **Metodos**
    - operaciones que pueden realizarse con la clase.


Pensemos como un ejemplo el carro , la clase carro podria tener atributos tales como numero de marcha, numero de asientos, cilindrada... y podria realizar las operaciones tales como subir marcha, barjar marcha acelerar o frenar *un objeto es un modelo de carro*

*Escritura en Python*

```
class NombreClase:
  def __init__(self, variable1, variable2):
    self.Atributo1 = valor1
    self.Atributo2 = valor2

  def NombreMetodo(self):
    BloqueCodigo
```

- **class**
  - palabra reservada en Python para definir una clase
- **NombreClase**
  - nombre de la clase que quieres crear
- **def**
  - palabra reservada en Python que se utiliza para definir tanto el constructor de la clase *(Metodo que se ejecuta la primera vez que usas la clase)*
- **__init__**
  - palabra reservada en Python para definir el metodo constructor de la clase. El metodo __init__ es lo primero que se ejecuta cuado creas un objeto de una clase
- **self(variable1)**
  - parametro del constructor de la clase. El parametro self es obligatorio y despues puedes tener tanto un parametro.
- **NombreMetodo**
  - nombre del metodo de la clase
- **(self)**
  - parametros del metodo. El parametro self es obligatorio depues puedes tener mas datos.

### ***Ejercicio1**
```
class Persona:
  def __init__(self, nombre, apellidos, edad):
    self.Nombre = nombre
    self.Apellidos = apellidos
    self.Edad = edad

  def MostrarPersona(self):
    print("Nombre :" + self.Nombre)
    print("Apellidos :" + self.Apellidos)
    print("Edad :" + self.Edad)

p1 = Persona("Alfredo", "Moreno", 35)
p1.MostrarPersona() 
```

### ***Ejercicio2**
```
class Persona:
  def __init__(self, nombre, apellidos, edad):
    self.Nombre = nombre
    self.Apellidos = apellidos
    self.Edad = edad

  def MostrarPersona(self):
    print("Nombre :" + self.Nombre)
    print("Apellidos :" + self.Apellidos)
    print("Edad :" + self.Edad)

print("Objetos Originales")
p1 = Persona("Alfredo", "Moreno", 35)
p1.MostrarPersona()

p2 = Persona("Valeria","Moreno",1)
p2.MostrarPersona()

p1 = p2

print("Objetos tras asignacion")
p1.MostrarPersona()
p2.MostrarPersona()
```