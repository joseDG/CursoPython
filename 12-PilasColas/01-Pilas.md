## **Pilas** ⏰ 

Las pilas son estructuras de datos que podemos asemejarlas a una pila de platos.
La pila esta compuesta por elementos en los que el primer elemento es el elemento mas nuevo en la misma.

## **Operaciones Principales**

- **Apilar:**
  - Coloca un elemento en la pila.
- **Retirar:**
  - Retira el ultimo elemento apilado.

[Pilas](/assets/img/1.png)]()

## **Implementación**

Es este apartado vamos a ver como implementar la pila y vamos a realizar un ejercicio que simule el funcionamiento de una pila.

### *Ejercicio*

Para implementar la pila vamos a de finir una clase que se llama pila y tendra los siguientes metodos:

**Constructor:**
  -Inicialiara la lista de elementos que compoenen la pila.
**Apilar:**
  -Insertar un elemento en la cima de la pila
**Retirar:**
  -Retirar el elemento que se encuentra en la cima de la pila
**LeerCima:**
  -Devuelve el elemento que se encuentra encima de la pila sin retirarlo
**EstaVacia:**
  -Devuelve True en caso de que la pila este vacia y False en caso contrario
**NumeroElementos:**
  -Devuelve el numero de elementos que tiene la pila
**MostrarPila:**
  -Muestra la pila por pantalla

```
class Pila:

  def __init__(self):
    self.__items =[]

  def EstaVacia(self):
    if len(self.__items) == 0:
      return True
    else:
      return False

  def Apilar(self, item):
    self.__items.append(item)

  def Retirar(self):
    return self.__items.pop()

  def LeerCima(self):
    return self.__items[len(self.__items)-1]

  def NumeroElementos(self):
    return len(self.__items)

  def MostrarPila(self):
    print("Pila: ", self.__items,"<-- CIMA")

def SimuladorPila():
  fin = False
  pila = Pila()
  while not(fin):
    opc = input("Opcion:")
    if(opc == "1"):
      item = input("Introduzca elemento a pilar: ")
      pila.Apilar(item)
      print("Elemento apilado: ",item)
    elif(opc=='2'):
      if pila.EstaVacia():
        print("La pila esta vacia, no puede retirarse ningun elemento")
      else:
        item = pila.LeerCima()
        pila.Retirar()
        print("Elemento retirado: ", item)
    elif(opc == '3'):
      if pila.EstaVacia():
        print("La pila esta vacia, no puede leerse la cima")
      else:
        print("La cima es:", pila.LeerCima())
    elif(opc == '4'):
      print("La pila tiene", pila.NumeroElementos(), "elementos")
    elif(opc == '5'):
      if pila.EstaVacia():
        print("La pila no esta vacia")
      else:
        print("La pila esta vacia")
    elif(opc=='6'):
      pila.MostrarPila()
    elif(opc=='7'):
      fin = 1


print("""=================
Simulador de Pila
==========================
Menu
1) Apilar
2) Retirar
3) Leer Cima
4) Nuemero de elementos
5) ¿Esta Vacia?
6) Mostrar pila
7) Salir""")
SimuladorPila()

```