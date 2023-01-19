import  Persona

class Alumno(Persona.Persona):
    def __init__(self):
        self.__Curso =""
        self.__Asignaturas = ""

    def getCurso(self):
        return  self.__Curso

    def setCurso(self,curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return  self.__Asignaturas

    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def MostrarAlumno(self):
        print("Alumno:")
        print("\tNombre:",self.getNombre())
        print("\tApellidos:",self.getApellidos())
        print("\tEdad:",self.getEdad())
        print("\tCurso:", self.__Curso)
        print("\tMatriculas:", self.__Asignaturas)