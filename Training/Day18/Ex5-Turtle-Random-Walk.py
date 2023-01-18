import random
from turtle import Screen
from random import randint
import turtle as t

rotation = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)  # needed to use rgb
t.pensize(10)
t.speed(0)


def my_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)

    return rand_color


for _ in range(1000):
    t.pencolor(my_random_color())
    t.right(random.choice(rotation))
    t.forward(20)

screen.exitonclick()
