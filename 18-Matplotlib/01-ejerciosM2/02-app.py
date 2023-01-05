import matplotlib.pyplot as plt 

def main():
  plt.rcParams['toolbar'] = 'None'
  plt.rcParams['font.size'] = '10'
  X = list(range(1,11))
  Y1 = [x**0.5 for x in X]
  Y2 = [x**1.5 for x in X]

  fig = plt.figure(figsize=(12,5), frameon= False, facecolor="yellow")
  #fig.canvas.set_window_title("Ventana con dos tipos de graficos distintos")
  fig.suptitle("Titulo superior", fontsize= 15, color='red')

  ax1 = fig.add_subplot(121)
  ax1.set_xlim(0.5,10.5)
  ax1.set_ylim(0, max(Y1) * 1.05)
  ax1.grid(True, axis="y", ls = "-", color='0.3')
  ax1.set_xticks([i for i in range(1, 11)])
  ax1.set_xlabel("Eje x primer grafico", color="magenta")
  ax1.set_ylabel("Eje y primer grafico", color="magenta")
  ax1.set_title("Primer grafico", color="blue")
  ax1.bar(X,Y1, width= 1, color ="green", align="center")

  ax2 = fig.add_subplot(122)
  ax2.set_xlim(0.5,10.5)
  ax2.set_ylim(0, max(Y2) * 1.05)
  ax2.grid(True, axis="x", ls="-", color='0.3')
  ax2.set_xticks([i for i in range(1, 11)])
  ax2.set_xticklabels(['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez',], fontsize=9, color="b")
  ax2.set_xlabel("Eje x segundo grafico", color="r")
  ax2.set_ylabel("Eje y segundo grafico", color="r")
  ax2.set_title("Segundo grafico", color="green")
  ax2.scatter(X, Y2)
  
  plt.show()

if __name__ == '__main__':
  main()
