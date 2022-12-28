## **Herencia** 👪 

tal como te hemos comentado durante el capitulo, la programacion orientada a objetos tiene uno de sus objetivos principales la reutilizacion de codigo.

La herencia consiste en la definicion de una clase utilizando como base una clase ya existente, la nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliara el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.

```
Clase base:Persona
  -Atributos:
    - Nombre
    - Apellidos
    - Edad

Clase derivada:Alumno
  -Atributos:
    - Curso
    - Asignaturas

Clase derivada:Profesor
  -Atributos:
    - Antiguedad
    - Tutorias
    - Telefono
```
La herencia en Python se especifica de la siguiente manera:
``` class NombreClase(ListaDeClasesBase)```


### **Ejemplo1**

```
class Persona:
  def __init__(self):
    self.__Nombre = ""
    self.__Apellidos = ""
    self.__Edad = 0

  def getNombre(self):
    return self.__Nombre

  def setNombre(self, nombre):
    self.__Nombre = nombre

  def getApellidos(self):
    return self.__Apellidos

  def setApellidos(self, apellidos):
    self.__Apellidos = apellidos

  def getEdad(self):
    return self.__Edad

  def setEdad(self, edad):
    self.__Edad = edad

class Alumno(Persona):
  def __init__(self):
    super().__init__()
    self.__Curso = ""
    self.__Asignaturas = ""

  def getCurso(self):
    return self.__Curso

  def setCurso(self, curso):
    self.__Curso = curso

  def getAsignaturas(self):
    return self.__Asignaturas

  def setAsignaturas(self, asignaturas):
    self.__Asignaturas = asignaturas

  def MostrarAlumno(self):
    print("Alumno:")
    print("\tNombre:", self.getNombre())
    print("\tApellidos:", self.getApellidos())
    print("\tEdad:", self.getEdad())
    print("\tCurso:", self.__Curso)
    print("\tMatriculas:", self.__Asignaturas)

alumno = Alumno()
alumno.setNombre("Alfredo")
alumno.setApellidos("Moreno")
alumno.setEdad(35)
alumno.setCurso("Bachillerato")
alumno.setAsignaturas(["Matematicas","Tecnologia","Fisica"])
alumno.MostrarAlumno() 
```

## **Herencia Multiple** 🎶 

La herencia multiple, consiste que vamos a poder tener un objeto que herede de más de una clase.

En el presente ejercicio vamos a utilizar una parte de los ejercicios anteriores, las clases *Persona* y *ProfesorUniversitario* que heredara de la clase *Profesor* y de la clase *Investigador*.

```
Clase:Persona
  -Atributos:
    - Nombre
    - Apellidos
    - Edad

Clase:Profesor
  -Hereda de: Persona
  -Atributos:
    - Antiguedad
    - Tutorias
    - Telefono

Clase: Investigador
  -Hereda de: Persona
  -Atributos:
    - Especialidad
    - Anos

Clase: ProfesorUniversitario
  -Hereda de: Persona e Investigador
  -Atributos:
    - Universidad
    - Departamento
```

## **Ejemplo1 Herencia Multiple**

```
class Persona:
  def __init__(self):
    self.__Nombre = ""
    self.__Apellidos = ""
    self.__Edad = 0

  def getNombre(self):
    return self.__Nombre

  def setNombre(self, nombre):
    self.__Nombre = nombre

  def getApellidos(self):
    return self.__Apellidos

  def setApellidos(self, apellidos):
    self.__Apellidos = apellidos

  def getEdad(self):
    return self.__Edad

  def setEdad(self, edad):
    self.__Edad = edad


class Profesor(Persona):
  def __init__(self):
    super().__init__()
    self.__Antiguedad = ""
    self.__Tutorias = ""
    self.__Telefono = ""

  def getAntiguedad(self):
    return self.__Antiguedad

  def setAntiguedad(self, antiguedad):
    self.__Antiguedad = antiguedad

  def getTutorias(self):
    return self.__Tutorias

  def setTutorias(self, tutorias):
    self.__Tutorias = tutorias

  def getTelefono(self):
    return self.__Telefono

  def setTelefono(self, telefono):
    self.__Telefono = telefono 

class Investigador(Persona):
  def __init__(self):
    super().__init__()
    self.__Especialidad = ""
    self.__Anos = ""

  def getEspecialidad(self):
    return self.__Especialidad 

  def setEspecialidad(self, especialidad):
    self.__Especialidad = especialidad

  def getAnos(self):
    return self.__Anos

  def setAnos(self, anos):
    self.__Anos = anos

class ProfesorUniversitario(Profesor, Investigador):
  def __init__(self):
    super().__init__()
    self.__Universidad = ""
    self.__Departamento = ""

  def getUniversidad(self):
    return self.__Universidad

  def setUniversidad(self, universidad):
    self.__Universidad = universidad

  def getDepartamento(self):
    return self.__Departamento

  def setDepartamento(self, departamento):
    self.__Departamento = departamento

  def MostrarProfesorUniversitario(self):
    print("Profesor Universitario:")
    print("\tNombre:", self.getNombre())
    print("\tApellidos:", self.getApellidos())
    print("\tEdad:", self.getEdad())
    print("\tAntiguedad:", self.getAntiguedad())
    print("\tTutorias:", self.getTutorias())
    print("\tTelefono:", self.getTelefono())
    print("\tEspecialidad:", self.getEspecialidad())
    print("\tAnos:", self.getAnos())
    print("\tUniversidad:", self.__Universidad)
    print("\tDepartamento:", self.__Departamento)




profesor = ProfesorUniversitario()
profesor.setNombre("Alfredo")
profesor.setApellidos("Moreno")
profesor.setEdad(50)
profesor.setAntiguedad(15)
profesor.setTutorias([["Lunes","16-18"], ["Jueves","12-14"], ["Viernes","11-13"]])
profesor.setTelefono("721118")
profesor.setEspecialidad("Desarrollo de Software")
profesor.setAnos(15)
profesor.setUniversidad("Universidad de Extremadura")
profesor.setDepartamento("Lenguajes y Sistemas Informaticos")
profesor.MostrarProfesorUniversitario() 
```