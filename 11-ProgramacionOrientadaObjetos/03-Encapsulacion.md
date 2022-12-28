## **Encapsulacion** 🔕 

Uno de los objetivos que tiene la programacion orientada a objetos es proteger los datos de acceso o usos no controlados, y esto es lo que se conoce como *encapsulacion*.

Los datos (atributos) que se componen una clase pueden ser de dos tipos:

- **Publicos:**
  - Los datos son accesibles sin control, es decir, los datos pueden ser usados sin ningun tipo de mecanismo que proteja.

- **Privados:**
  - Los datos no pueden ser accedidos sin control  y para acceder a ellos se deberan implementar un metodo que acceda a ellos.

La encapsulacion no solo puede realiarse sobre los atributos de la clase, tambien es posible realizarla sibre los metodos, es decir, aquellos metodos que indiquemos que son privados no podran ser utilizados por elementos externos al propio objeto.

La clase privada va a tener dos metodos por cada atributo de clase que tiene, uno para realizar la lectura del atributo *(GET)* y otro para realizar la escritura del mismo con *(SET)*. Esto es algo comun que se hace en programacion orientada a objetos.

```
class PersonaPublica:
  def __init__(self, nombre, apellidos, edad):
    self.Nombre = nombre
    self.Apellidos = apellidos
    self.Edad = edad

class PersonaPrivada:
  def __init__(self,nombre, apellidos, edad):
    self.__Nombre = nombre
    self.__Apellidos = apellidos
    self.__Edad = edad

  def GetNombre(self):
    return self.__Nombre

  def SetNombre(self, nombre):
    self.__Nombre = nombre

  def GetApellidos(self):
    return self.__Apellidos

  def SetApellidos(self, apellidos):
    self.__Apellidos = apellidos

  def GetEdad(self):
    return self.__Edad

  def SetEdad(self, edad):
    self.__Edad = edad

publico  = PersonaPublica("Jose","Diaz",30)
privado = PersonaPrivada("Valeria","Diaz",25)

print("PERSONA PUBLICA")
print("Nombre: " + publico.Nombre)
print("Apellidos: " + publico.Apellidos)
print("Edad: " + publico.Edad)

print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))

print("Modificacion de objetos Publico")
publico.Apellidos = "Diaz Gonzalez"
print("Nombre: " + publico.Nombre)
print("Apellidos: " + publico.Apellidos)
print("Edad: " + publico.Edad)

print("Modificacion de objetos Privados")
privado.SetApellidos("Guarnizo Perez")
print("Nombre: " + privado.GetNombre())
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))
```