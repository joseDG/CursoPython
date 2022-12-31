## **Colas** ☣ 

Las colas son estructuras de datos que funcionalmente son iguales alas colas que pueden encontrar en el mundo real: aeropuerto, supermercados, etc

Funcionalmente hablando, en las colas la primera persona o el primer elemento que entra sera el primero en salir, son estructuras tipo *FIFO*, en ingles "First in First Out" Priemro en entrar primero en salir.

### **Operaciones Principales**
**Encolar:**
 - Introduce un elemento en la ultima posicion de la cola. 
**Desencolar:**
 - Retira el primer elemento de la cola

[Pilas](/assets/img/2.png)]()

En este apartado vamos a ver como implementar la cola y vamos a realizar un ejercicio qeu simulara el funcionamiento de una cola.


### *Ejercicio <code>*

```
class Cola:
  def __init__(self):
    self.__items = []

  def EstaVacia(self):
    if len(self.__items) == 0:
      return True
    else:
      return False

  def Encolar(self, item):
    self.__items.insert(0, item)

  def Desencolar(self):
    return self.__items.pop()

  def LeerPrimerElemento(self):
    return self.__items[len(self.__items)-1]

  def NumeroElemento(self):
    return len(self.__items)

  def MostrarCola(self):
    print("Cola: ", self.__items, "<-- Primer elemento")

def SimularCola():
  fin = False
  cola = Cola()
  while not(fin):
    opc = input("Opcion:")
    if(opc == '1'):
      item = input("Introduzca elemento a encolar: ")
      cola.Encolar(item)
      print("Elemento encolado:",item)
    elif(opc == '2'):
      if cola.EstaVacia():
        print("La cola esta vaciam no puede desencolar ningun elemento")
      else:
        item = cola.LeerPrimerElemento()
        cola.Desencolar()
        print("Elemento desencolado: ", item)
    elif(opc == '3'):
      if cola.EstaVacia():
        print("La cola esta vacia, no puede leerse ningun elemento")
      else:
        print("El primer elemento es: ", cola.LeerPrimerElemento())
    elif(opc == '4'):
      print("La cola tiene", cola.NumeroElemento(), "elementos")
    elif(opc == '5'):
      if cola.EstaVacia():
        print("La cola esta vacia")
      else:
        print("La cola no esta vacia")
    elif(opc=='6'):
      cola.MostrarCola()
    elif(opc=='7'):
      fin = 1

print("""=================
Simulador de Cola
==========================
Menu
1) Encolar
2) Desencolar
3) Leer primer elemento
4) Nuemero de elementos
5) ¿Esta Vacia?
6) Mostrar cola
7) Salir""")
SimularCola() 
```