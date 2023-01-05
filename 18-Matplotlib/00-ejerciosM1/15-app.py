import matplotlib.pyplot as plt 

def main():
  plt.figure(figsize=(14,8)) #cambiar
  eje_x = list(range(1,13))
  eje_y = [23,4,32,77,48,93,75,90,32,28,21,18]#notas
  plt.xlim(0.5, 12.5)
  plt.ylim(0, 100)
  meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto", "Septiembre","Octubre","Noviembre","Diciembre"]#alumnos
  plt.xticks([x for x in range(1,13)], meses, fontsize=7, rotation=25)
  plt.yticks([10*x for x in range(11)])
  plt.bar(eje_x, eje_y, color='cyan', align='center', width=1)#c=green
  plt.show()

if __name__ == '__main__':
  main()