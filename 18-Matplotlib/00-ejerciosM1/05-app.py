import matplotlib.pyplot as plt 

def main():
  X = list(range(10))
  Y1 = [x**0.5 for x in X]
  Y2 = [x for x in X]
  Y3 = [x**1.5 for x in X]
  Y4 = [x**2 for x in X]

  plt.suptitle("Ejemplo de funciones simultaneas", fontsize=10)

  plt.subplot2grid((2,2),(0,0), colspan=2)
  plt.title("Dos funciones representadas simultaneamente", fontsize=10)
  plt.plot(X, Y1)
  plt.plot(X, Y2)
  plt.plot(X, Y3)
  plt.plot(X, Y4)

  plt.subplot2grid((2,2),(0,0), colspan=2)
  plt.title("Dos funciones representadas simultaneamente", fontsize=10)
  plt.plot(X, Y1)
  plt.plot(X, Y2)
  plt.show()

if __name__ == '__main__':
  main()