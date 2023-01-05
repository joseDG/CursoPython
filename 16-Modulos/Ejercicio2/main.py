import Alumno
import Profesor

alumno = Alumno.Alumno()
alumno.setNombre("Jose")
alumno.setApellidos("Diaz")
alumno.setEdad(35)
alumno.setCurso("Bachillerato")
alumno.setAsignaturas(["Matematicas","Tecnologia","Ingles"])
alumno.MostrarAlumno()

profesor = Profesor.Profesor()
profesor.setNombre("Pedro")
profesor.setApellidos("Salinas")
profesor.setEdad(40)
profesor.setAntiguedad(15)
profesor.setTutorias([["Lunes","16-18"],["Martes","16-18"],["Jueves","16-18"]])
profesor.setTelefono("96325814")
profesor.MostrarProfesor()