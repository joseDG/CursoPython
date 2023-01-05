import matplotlib.pyplot as plt 

def main():
  calificaciones = [23,12,32,77,38]
  plt.pie(calificaciones)
  plt.pie(calificaciones, labels=['Ana','Eva','David','Jose','Marta'], shadow=True, labeldistance=0.7)
  plt.show()

if __name__ == '__main__':
  main()