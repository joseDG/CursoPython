### **Ejercicio Encapsulamiento**
```
class Coordenada:
  def __init__(self, x, y):
    self.__X = x
    self.__Y = y 

  #metodo privado
  def __getX(self):
    return self.__X 

  def setX(self, x):
    self.__X = x 

  def getY(self):
    return self.__Y

  def setY(self,y):
    self.__Y = y

coordenada = Coordenada(3,4)
print("(",coordenada.__getX(),",",coordenada.getY(),")")
```

### **Ejercicio Herencia**

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

  def MostrarProfesor(self):
    print("Profesor:")
    print("\tNombre:", self.getNombre())
    print("\tApellidos:", self.getApellidos())
    print("\tEdad:", self.getEdad())
    print("\tAntiguedad:", self.__Antiguedad)
    print("\tTutorias:", self.__Tutorias)
    print("\tTelefono:", self.__Telefono)

alumno = Alumno()
alumno.setNombre("Alfredo")
alumno.setApellidos("Moreno")
alumno.setEdad(35)
alumno.setCurso("Bachillerato")
alumno.setAsignaturas(["Matematicas","Tecnologia","Fisica"])
alumno.MostrarAlumno()


profesor = Profesor()
profesor.setNombre("Profesor")
profesor.setApellidos("Casa Papel")
profesor.setEdad(50)
profesor.setAntiguedad(15)
profesor.setTutorias([["Lunes","16-18"], ["Jueves","12-14"], ["Viernes","11-13"]])
profesor.setTelefono("721118")
profesor.MostrarProfesor() 
```