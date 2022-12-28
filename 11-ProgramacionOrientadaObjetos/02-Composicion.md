## **Composicion** 🎨 

La primera tecnica que vamos a explicarte referentemente a la reutilizacion de codigo fuente en la programacion orientada a objetos es la **composicion**, que consiste en la creacion de nuevas clases apartir de otras clases existentes que actuan como elementos compositores de la nueva.


En programacion orientada a objetos la composicion significa que entre las dos clases existe una relacion del tipo *tiene un*.

### **Ejercicio 1**

Pongamos un ejemplo del mundo real para luego hacerlo en codigo: una coordenada en dos dimensiones esta compuesta por dos valores, el valor en el eje de las X y el valor en el eje de las Y. esto podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que son cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada.

```
Class Coordenada:
  - Valor eje de las X
  - Valor eje de las Y

Clase Cuadrado:
  - Coordenada vertice 1
  - Coordenada vertice 2
  - Coordenada vertice 3
  - Coordenada vertice 4
```

```
class Coordenada:
  def __init__(self,x, y):
    self.X = x
    self.Y = y

  def MostrarCoordenada(self):
    print("(",self.X,",",self.Y,")")

class Cuadrado:
  def __init__(self,v1,v2,v3,v4):
    self.V1 = v1
    self.V2 = v2
    self.V3 = v3
    self.V4 = v4

  def MostrarVertices(self):
    print("El cuadrado esta compuesto por los siguientes vertices:")
    self.V1.MostrarCoordenada()
    self.V2.MostrarCoordenada()
    self.V3.MostrarCoordenada()
    self.V4.MostrarCoordenada()
 
```
Para ambas clases hemos definido un metodo que muestra la informacion por pantalla de los atributos de la misma.Puedes observar que el metodo de mostrar por pantalla los vertices del cuadrado no accede a los atributos de las coordenadas y utiliza el metodo MostrarCoordenada de la clase Coordenada.