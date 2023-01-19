import Persona

class Profesor(Persona.Persona):
    def __init__(self):
        self.__Antiguedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""

    def getAntiguedad(self):
        return  self.__Antiguedad

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
        print("\tEdad: ", self.getEdad())
        print("\tAntiguedad:", self.__Antiguedad)
        print("\tTutorias:",self.__Tutorias)
        print("\tTelefono:",self.__Telefono)