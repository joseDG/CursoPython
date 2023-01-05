#Importamos la libreria para utilizar SQLite
import sqlite3

#Conecta a la base de datos
con = sqlite3.connect('Coches.db')

#Crar los registros de fabricantes
register1 = (1, 'Honda', '911234567', 'Calle Japon 3', 'hello@honda.es')
register2 = (2, 'Seat', '919287567', 'Calle Espana 1', 'info@seat.es')
register3 = (3, 'Mercedez','919292987','Calle Cuenca 1','info@mercedes.ec')

#Aperturando de un cursor e insercion de los fabricantes
cursor = con.cursor()
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register1)
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register2)
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register3)

#Commit de las operaciones
con.commit()

#Lectura de todos los fabricantes
cursor.execute("SELECT * FROM Fabricante")
print("Mostrando  todos los fabricantes:")
for f in cursor:
    print(f)

#Actualizacion de un Fabricante
query = "UPDATE Fabricante SET Email = 'nuevoemail@honda.es' WHERE id = 1"
cursor.execute(query)
con.commit()
#Lectua actualizada
cursor.execute("SELECT * FROM Fabricante")
print("Mostrando  todos los fabricantes:")
for f in cursor:
    print(f)

#Eliminar registros
query = "DELETE FROM Fabricante WHERE id = 1"
cursor.execute(query)
con.commit()
#Lectua actualizada
cursor.execute("SELECT * FROM Fabricante")
print("Mostrando  todos los fabricantes:")
for f in cursor:
    print(f)

#Cierre la conexion ala base de datos
con.close()