import matplotlib.pyplot as plt 

def main():
  eje_x = list(range(1,11))
  eje_y = [23,4,32,77,8,43,45,90,12,60]
  plt.suptitle("Grafico de disperción")
  plt.xlim(0, 11)
  plt.ylim(0,100)
  plt.scatter(eje_x,eje_y)
  plt.show()

if __name__ == "__main__":
  main()