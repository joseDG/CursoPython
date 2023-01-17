import turtle as t
import  random

tim = t.Turtle()

colores = ["cyan", "chartreuse", "brown", "cornflower blue", "dark violet", "sandy brown", "lawn green"]
direcciones = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colores))
    tim.forward(30)
    tim.setheading(random.choice(direcciones))