import matplotlib.pyplot as plt 

def main():
  eje_x = list(range(1,11))
  eje_y = [23,4,32,77,8,43,45,90,12,68]
  plt.subplot2grid((1,2),(0,0), colspan=1, rowspan=1)
  plt.xlim(0,11)
  plt.ylim(0,100)
  plt.bar(eje_x,eje_y, width=1, color='green', align='center')
  plt.subplot2grid((1,2),(0,1),colspan=1, rowspan=1)
  plt.xlim(0, 100)
  plt.ylim(0,11)
  plt.barh(eje_x, eje_y, height=1, color='red', align='center')
  plt.show()


if __name__ == '__main__':
  main()