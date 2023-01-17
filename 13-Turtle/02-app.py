import turtle as t
import random

tim = t.Turtle()
colores = ["cyan", "chartreuse", "brown", "cornflower blue", "dark violet", "sandy brown", "lawn green"]

def dibujar_forma(num_lados):
    angulo = 360 / num_lados
    for _ in range(num_lados):
        tim.forward(100)
        tim.right(angulo)

for forma_lados_n in range(3, 11):
    tim.color(random.choice(colores))
    dibujar_forma(forma_lados_n)