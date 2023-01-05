class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return  self.__Nombre

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